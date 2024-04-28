import asyncio
import base64

import aiohttp
import requests


class APICredentials:
    def __init__(self, username: str, password: str) -> None:
        """
        Initializes an instance of ApiCredentials.

        Args:
            username (str): The username for API authentication.
            password (str): The password for API authentication.
        """
        self.username = username
        self.password = password

    def get_encoded_credentials(self) -> str:
        """
        Returns the Base64 encoded username and password for API authentication.
        """
        credentials = f"{self.username}:{self.password}"
        return base64.b64encode(credentials.encode()).decode()


class Client:
    def __init__(self, base_url: str, api_credentials: APICredentials) -> None:
        """
        Initializes an instance of the Internal class.

        Args:
            base_url (str): The base URL of the API.
            api_credentials (ApiCredentials): The API credentials.

        Returns:
            None
        """
        self.base_url = base_url
        self.api_credentials = api_credentials
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Basic {self.api_credentials.get_encoded_credentials()}",
        }

    def req(self, payload: dict, method: str, config: dict) -> dict:
        """
        Sends a HTTP request to the specified URL with the given payload and method.

        Args:
            payload (dict): The payload to be sent with the request.
            method (str): The HTTP method to be used for the request (e.g., "POST", "GET").
            config (dict): Additional configuration options for the request.

        Returns:
            dict: The JSON response from the server, if the request is successful.
                  None, if an error occurs during the request.

        Raises:
            requests.exceptions.Timeout: If the request times out.
            requests.exceptions.HTTPError: If an HTTP error occurs.
            requests.exceptions.RequestException: If a general request error occurs.
        """
        try:
            if method == "POST":
                response = requests.post(
                    self.base_url,
                    headers=self.headers,
                    json=payload,
                    timeout=config["request_timeout"],
                )
            else:
                print(f"Unsupported method: {method}")
                return None

            response.raise_for_status()

            if response.status_code == 200:
                return response.json()
            else:
                print(f"Error occurred: {response.status_code}")
                return None

        except requests.exceptions.Timeout:
            print(
                f"Timeout error. The request to {self.base_url} with method {method} has timed out."
            )
            return None
        except requests.exceptions.HTTPError as err:
            print(f"HTTP error occurred: {err}")
            print(response.text)
            return None
        except requests.exceptions.RequestException as err:
            print(f"Error occurred: {err}")
            return None


class ClientAsync:

    def __init__(self, base_url: str, api_credentials: APICredentials) -> None:
        """
        Initializes an instance of the Internal class.

        Args:
            base_url (str): The base URL of the API.
            api_credentials (ApiCredentials): The API credentials used for authorization.

        Returns:
            None
        """
        self.base_url = base_url
        self.api_credentials = api_credentials
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Basic {self.api_credentials.get_encoded_credentials()}",
        }

    async def get_job_id(
        self, payload: dict, user_session: aiohttp.ClientSession, request_timeout: int
    ) -> str:
        try:
            async with user_session.post(
                self.base_url,
                headers=self.headers,
                json=payload,
                timeout=request_timeout,
            ) as response:
                data = await response.json()
                response.raise_for_status()
                return data["id"]
        except aiohttp.ClientResponseError as e:
            print(f"HTTP error occurred: {e.status} - {e.message} - {data['message']}")
        except aiohttp.ClientConnectionError as e:
            print(f"Connection error occurred: {e}")
        except asyncio.TimeoutError:
            print(f"Timeout error. The request to {self.base_url} has timed out.")
        except Exception as e:
            print(f"Error occurred: {str(e)}")
            return None

    async def poll_job_status(
        self,
        job_id: str,
        poll_interval: int,
        user_session: aiohttp.ClientSession,
        timeout: int,
    ) -> bool:
        job_status_url = f"{self.base_url}/{job_id}"
        end_time = asyncio.get_event_loop().time() + timeout
        while asyncio.get_event_loop().time() < end_time:
            try:
                async with user_session.get(
                    job_status_url, headers=self.headers, timeout=poll_interval
                ) as response:
                    data = await response.json()
                    response.raise_for_status()
                    if data["status"] == "done":
                        return True
                    elif data["status"] == "faulted":
                        raise Exception("Job faulted")
            except Exception as e:
                print(f"Error occurred: {str(e)}")
                return False
            await asyncio.sleep(poll_interval)
        print("Job completion timeout exceeded")
        return False

    async def get_http_resp(
        self, job_id: str, user_session: aiohttp.ClientSession
    ) -> dict:
        """
        Retrieves the HTTP response for a given job ID.

        Args:
            job_id (str): The ID of the job.
            user_session (aiohttp.ClientSession): The client session used for making the request.

        Returns:
            dict: The JSON response data.

        Raises:
            aiohttp.ClientResponseError: If a client response error occurs.
            aiohttp.ClientConnectionError: If a client connection error occurs.
            asyncio.TimeoutError: If the request times out.
            Exception: If any other error occurs.
        """
        result_url = f"{self.base_url}/{job_id}/results"
        try:
            async with user_session.get(result_url, headers=self.headers) as response:
                data = await response.json()
                response.raise_for_status()
                return data
        except aiohttp.ClientResponseError as e:
            print(f"HTTP error occurred: {e.status} - {e.message} - {data['message']}")
        except aiohttp.ClientConnectionError as e:
            print(f"Connection error occurred: {e}")
        except asyncio.TimeoutError:
            print(f"Timeout error. The request to {result_url} has timed out.")
        except Exception as e:
            print(f"An error occurred: {e} - {data['message']}")
        return None

    async def execute_with_timeout(
        self, payload: dict, config: dict, user_session: aiohttp.ClientSession
    ) -> dict:

        request_timeout = config["request_timeout"]
        job_completion_timeout = config["job_completion_timeout"]
        poll_interval = config["poll_interval"]

        job_id = await self.get_job_id(payload, user_session, request_timeout)
        if not job_id:
            print("Failed to get job ID")

        job_completed = await self.poll_job_status(
            job_id, poll_interval, user_session, job_completion_timeout
        )
        if not job_completed:
            print("Job did not complete successfully")

        result = await self.get_http_resp(job_id, user_session)
        return result
