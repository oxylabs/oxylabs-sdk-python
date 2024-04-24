import oxylabs.utils.utils as utils
from src.oxylabs.internal import APICredentials, Client, ClientAsync
from src.oxylabs.utils.defaults import ASYNC_BASE_URL, SYNC_BASE_URL

from .bing.bing import Bing, BingAsync
from .google.google import Google, GoogleAsync


class SERP:
    def __init__(self, username: str, password: str) -> None:

        api_credentials = APICredentials(username, password)
        self._client = Client(SYNC_BASE_URL, api_credentials)
        self.bing = Bing(self)
        self.google = Google(self)

    def _get_resp(self, payload: dict, config: dict) -> dict:
        """
        Processes the payload synchronously and fetches API response.

        Args:
            payload (dict): The payload for the request.
            config (dict): The configuration for the request.

        Returns:
            dict: The response from the server after the job is completed.
        """
        # Remove empty or null values from the payload
        payload = {k: v for k, v in payload.items() if v is not None}

        return self._client.req(payload, "POST", config)


class SERPAsync:

    def __init__(self, username: str, password: str) -> None:
        """
        Initializes an asynchronous SERP client.

        Args:
            username (str): The username for API authentication.
            password (str): The password for API authentication.
        """
        self.api_credentials = APICredentials(username, password)
        self._client = ClientAsync(ASYNC_BASE_URL, self.api_credentials)
        self.bing_async = BingAsync(self)
        self.google_async = GoogleAsync(self)
        self._session = None
        self._requests = 0

    async def _get_resp(self, payload: dict, config: dict) -> dict:
        """
        Processes the payload asynchronously and fetches API response.

        Args:
            payload (dict): The payload for the request.
            config (dict): The configuration for the request.

        Returns:
            dict: The response from the server after the job is completed.
        """
        # Remove empty or null values from the payload
        payload = {k: v for k, v in payload.items() if v is not None}

        result: dict = None
        self._requests += 1

        try:
            self._session = await utils.ensure_session(self._session)

            result = await self._client.execute_with_timeout(
                payload, config, self._session
            )
            return result

        except Exception as e:
            print(f"An error occurred: {e}")

        finally:
            self._requests -= 1
            if self._requests == 0:
                await utils.close(self._session)
        return None
