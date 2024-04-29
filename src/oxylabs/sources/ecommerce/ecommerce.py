import src.oxylabs.utils.utils as utils
from src.oxylabs.internal import APICredentials, Client, ClientAsync
from src.oxylabs.utils.defaults import ASYNC_BASE_URL, SYNC_BASE_URL

from .amazon.amazon import Amazon, AmazonAsync
from .google_shopping.google_shopping import (
    GoogleShopping,
    GoogleShoppingAsync,
)
from .universal.universal import Universal, UniversalAsync
from .wayfair.wayfair import Wayfair, WayfairAsync


class Ecommerce:
    def __init__(self, username: str, password: str) -> None:
        """
        Initializes an instance of the Ecommerce class.

        Args:
            username (str): The username for API authentication.
            password (str): The password for API authentication.
        """
        api_credentials = APICredentials(username, password)
        self._client = Client(SYNC_BASE_URL, api_credentials)
        self.amazon = Amazon(self)
        self.google_shopping = GoogleShopping(self)
        self.universal = Universal(self)
        self.wayfair = Wayfair(self)

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
        self._client = ClientAsync(ASYNC_BASE_URL, self.api_credentials)
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

        result = None
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
