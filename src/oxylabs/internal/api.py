import base64
import logging
import requests
import aiohttp
import asyncio
from platform import python_version, architecture
from oxylabs._version import __version__
from oxylabs.utils.defaults import ASYNC_BASE_URL, SYNC_BASE_URL
from oxylabs.utils.utils import ensure_session, close_session

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class APICredentials:
    def __init__(self, username: str, password: str) -> None:
        """
        Initializes an instance of the ApiCredentials class.

        Args:
            username (str): The username for API authentication.
            password (str): The password for API authentication.
        """
        credentials = f"{username}:{password}"
        self.encoded_credentials = base64.b64encode(credentials.encode()).decode()

class BaseAPI:
    def __init__(self, base_url: str, api_credentials: APICredentials, **kwargs) -> None:
        """
        Initializes an instance of the BaseAPI class.

        Args:
            base_url (str): The URL of the API.
            api_credentials (APICredentials): An instance of APICredentials used for authentication.
        """
        self._base_url = base_url
        bits, _ = architecture()
        sdk_type = kwargs.get("sdk_type", f"oxylabs-sdk-python/{__version__} ({python_version()}; {bits})")
        self._headers = {
            "Content-Type": "application/json",
            "Authorization": f"Basic {api_credentials.encoded_credentials}",
            "x-oxylabs-sdk": sdk_type,
        }

class RealtimeAPI(BaseAPI):
    def __init__(self, api_credentials: APICredentials, **kwargs) -> None:
        """
        Initializes an instance of the RealtimeAPI class.

        Args:
            api_credentials (APICredentials): An instance of APICredentials used for authentication.
        """
        super().__init__(SYNC_BASE_URL, api_credentials, **kwargs)

    def get_response(self, payload:dict, config:dict) -> dict:
        """
        Sends the payload synchronously and fetches the response.

        Args:
            payload (dict): The payload for the request.
            config (dict): The configuration for the request.

        Returns:
            dict: The response from the server after the job is completed.
        """
        # Remove empty or null values from the payload
        payload = {k: v for k, v in payload.items() if v is not None}

        return self._get_http_response(payload, "POST", config)

    def _get_http_response(self, payload: dict, method: str, config: dict) -> dict | None:
        """
        Sends an HTTP request to the specified URL with the given payload
        and method.

        Args:
            payload (dict): The payload to be sent with the request.
            method (str): The HTTP method to be used for the request
            (e.g., "POST", "GET").
            config (dict): Additional configuration options for the
            request.

        Returns:
            dict: The JSON response from the server, if the request is
            successful.
                  None, if an error occurs during the request.

        Raises:
            requests.exceptions.Timeout: If the request times out.
            requests.exceptions.HTTPError: If an HTTP error occurs.
            requests.exceptions.RequestException: If a general request
            error occurs.
        """
        try:
            if method == "POST":
                response = requests.post(
                    self._base_url,
                    headers=self._headers,
                    json=payload,
                    timeout=config["request_timeout"],
                )
            else:
                logger.error(f"Unsupported method: {method}")
                return None

            response.raise_for_status()

            if response.status_code == 200:
                return response.json()
            else:
                logger.error(f"Error occurred: {response.status_code}")
                return None

        except requests.exceptions.Timeout:
            logger.error(
                f"Timeout error. The request to {self._base_url} with method {method} has timed out."
            )
            return None
        except requests.exceptions.HTTPError as err:
            logger.error(f"HTTP error occurred: {err}")
            logger.error(response.text)
            return None
        except requests.exceptions.RequestException as err:
            logger.error(f"Error occurred: {err}")
            return None

class AsyncAPI(BaseAPI):
    def __init__(self, api_credentials: APICredentials, **kwargs) -> None:
        """
        Initializes an instance of the AsyncAPI class.

        Args:
            api_credentials (APICredentials): An instance of APICredentials used for authentication.
        """
        super().__init__(ASYNC_BASE_URL, api_credentials, **kwargs)
        self._session = None
        self._requests = 0

    async def get_response(self, payload: dict, config: dict) -> dict | None:
        """
        Processes the payload asynchronously and fetches the response.

        Args:
            payload (dict): The payload for the request.
            config (dict): The configuration for the request.

        Returns:
            dict: The response from the server after the job is completed.
        """
        # Remove empty or null values from the payload
        payload = {k: v for k, v in payload.items() if v is not None}

        result = None
        self._requests += 1

        try:
            self._session = await ensure_session(self._session)

            result = await self._execute_with_timeout(
                payload, config, self._session
            )
            return result

        except Exception as e:
            logger.error(f"An error occurred: {e}")

        finally:
            self._requests -= 1
            if self._requests == 0:
                await close_session(self._session)
        return None

    async def _get_job_id(
        self,
        payload: dict,
        user_session: aiohttp.ClientSession,
        request_timeout: int,
    ) -> str | None:
        try:
            async with user_session.post(
                self._base_url,
                headers=self._headers,
                json=payload,
                timeout=request_timeout,
            ) as response:
                data = await response.json()
                response.raise_for_status()
                return data["id"]
        except aiohttp.ClientResponseError as e:
            logger.error(
                f"HTTP error occurred: {e.status} - {e.message} - {data['message']}"
            )
        except aiohttp.ClientConnectionError as e:
            logger.error(f"Connection error occurred: {e}")
        except asyncio.TimeoutError:
            logger.error(
                f"Timeout error. The request to {self._base_url} has timed out."
            )
        except Exception as e:
            logger.error(f"Error occurred: {str(e)}")
            return None

    async def _poll_job_status(
        self,
        job_id: str,
        poll_interval: int,
        user_session: aiohttp.ClientSession,
        timeout: int,
    ) -> bool:
        job_status_url = f"{self._base_url}/{job_id}"
        end_time = asyncio.get_event_loop().time() + timeout
        while asyncio.get_event_loop().time() < end_time:
            try:
                async with user_session.get(
                    job_status_url,
                    headers=self._headers,
                    timeout=poll_interval,
                ) as response:
                    data = await response.json()
                    response.raise_for_status()
                    if data["status"] == "done":
                        return True
                    elif data["status"] == "faulted":
                        raise Exception("Job faulted")
            except Exception as e:
                logger.error(f"Error occurred: {str(e)}")
                return False
            await asyncio.sleep(poll_interval)

        logger.info("Job completion timeout exceeded")
        return False

    async def _get_http_response(
        self, job_id: str, user_session: aiohttp.ClientSession
    ) -> dict | None:
        """
        Retrieves the HTTP response for a given job ID.

        Args:
            job_id (str): The ID of the job.
            user_session (aiohttp.ClientSession): The client session used for
            making the request.

        Returns:
            dict: The JSON response data.

        Raises:
            aiohttp.ClientResponseError: If a client response error occurs.
            aiohttp.ClientConnectionError: If a client connection error occurs.
            asyncio.TimeoutError: If the request times out.
            Exception: If any other error occurs.
        """
        result_url = f"{self._base_url}/{job_id}/results"
        try:
            async with user_session.get(
                result_url, headers=self._headers
            ) as response:
                data = await response.json()
                response.raise_for_status()
                return data
        except aiohttp.ClientResponseError as e:
            logger.error(
                f"HTTP error occurred: {e.status} - {e.message} - {data['message']}"
            )
        except aiohttp.ClientConnectionError as e:
            logger.error(f"Connection error occurred: {e}")
        except asyncio.TimeoutError:
            logger.error(
                f"Timeout error. The request to {result_url} has timed out."
            )
        except Exception as e:
            logger.error(f"An error occurred: {e} - {data['message']}")
        return None

    async def _execute_with_timeout(
        self, payload: dict, config: dict, user_session: aiohttp.ClientSession
    ) -> dict:

        request_timeout = config["request_timeout"]
        job_completion_timeout = config["job_completion_timeout"]
        poll_interval = config["poll_interval"]

        job_id = await self._get_job_id(payload, user_session, request_timeout)
        if not job_id:
            logger.error("Failed to get job ID")

        job_completed = await self._poll_job_status(
            job_id, poll_interval, user_session, job_completion_timeout
        )
        if not job_completed:
            logger.error("Job did not complete successfully")

        result = await self._get_http_response(job_id, user_session)
        return result