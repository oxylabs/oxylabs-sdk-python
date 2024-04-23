from src.oxylabs.internal import Client, APICredentials, ClientAsync
from src.oxylabs.utils.defaults import SYNC_BASE_URL, ASYNC_BASE_URL
import asyncio
import oxylabs.utils.utils as utils
from . import (
    Amazon,
    AmazonAsync,
    GoogleShopping,
    GoogleShoppingAsync,
    Universal,
    UniversalAsync,
    Wayfair,
    WayfairAsync,
)


class Ecommerce:
    def __init__(self, username: str, password: str) -> None:
        """
        Initializes an instance of the Ecommerce class.

        Args:
            username (str): The username for API authentication.
            password (str): The password for API authentication.
        """
        api_credentials = APICredentials(username, password)
        self.client = Client(SYNC_BASE_URL, api_credentials)
        self.amazon = Amazon(self)
        self.google_shopping = GoogleShopping(self)
        self.universal = Universal(self)
        self.wayfair = Wayfair(self)

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


class EcommerceAsync:
    def __init__(self, username: str, password: str) -> None:
        """
        Initializes an instance of the EcommerceAsync class.

        Args:
            username (str): The username for API authentication.
            password (str): The password for API authentication.

        Returns:
            None
        """

        self.api_credentials = APICredentials(username, password)
        self.amazon_async = AmazonAsync(self)
        self.google_shopping_async = GoogleShoppingAsync(self)
        self.universal_async = UniversalAsync(self)
        self.wayfair_async = WayfairAsync(self)
        self.client = ClientAsync(ASYNC_BASE_URL, self.api_credentials)
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

        result = None
        self.requests += 1

        try:

            self.session = await utils.ensure_session(self.session)

            result = await self.client.execute_with_timeout(
                payload, config, self.session
            )
            return result

        except Exception as e:
            print(f"An error occurred: {e}")

        finally:
            self.requests -= 1
            if self.requests == 0:
                await utils.close(self.session)
        return None
