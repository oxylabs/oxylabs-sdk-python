import asyncio
import oxylabs.utils.utils as utils
from src.oxylabs.internal import APICredentials, Client, ClientAsync
from src.oxylabs.utils.defaults import ASYNC_BASE_URL, SYNC_BASE_URL

from . import (
    Bing,
    Baidu,
    Yandex,
    Google,
    BingAsync,
    BaiduAsync,
    YandexAsync,
    GoogleAsync,
)


class SERP:
    def __init__(self, username: str, password: str) -> None:

        api_credentials = APICredentials(username, password)
        self.client = Client(SYNC_BASE_URL, api_credentials)
        self.bing = Bing(self)
        self.baidu = Baidu(self)
        self.yandex = Yandex(self)
        self.google = Google(self)

    def get_resp(self, payload: dict, config: dict) -> dict:
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

        return self.client.req(payload, "POST", config)


class SERPAsync:

    def __init__(self, username: str, password: str) -> None:
        """
        Initializes an asynchronous SERP client.

        Args:
            username (str): The username for API authentication.
            password (str): The password for API authentication.
        """
        self.api_credentials = APICredentials(username, password)
        self.client = ClientAsync(ASYNC_BASE_URL, self.api_credentials)
        self.bing_async = BingAsync(self)
        self.baidu_async = BaiduAsync(self)
        self.yandex_async = YandexAsync(self)
        self.google_async = GoogleAsync(self)
        self.session = None
        self.requests = 0

    async def get_resp(self, payload: dict, config: dict) -> dict:
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
        self.requests += 1

        try:
            self.session = await utils.ensure_session(self.session)

            result = await asyncio.wait_for(
                self.client.execute_with_timeout(payload, config, self.session),
                timeout=config["timeout"],
            )
            return result
        except asyncio.TimeoutError:
            print("The request timed out")
        except Exception as e:
            print(f"An error occurred: {e}")

        finally:
            self.requests -= 1
            if self.requests == 0:
                await utils.close(self.session)
        return None
