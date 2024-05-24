import logging

import oxylabs.utils.utils as utils

from .amazon.amazon import Amazon, AmazonAsync
from .google_shopping.google_shopping import (
    GoogleShopping,
    GoogleShoppingAsync,
)
from .response import EcommerceResponse
from .universal.universal import Universal, UniversalAsync
from .wayfair.wayfair import Wayfair, WayfairAsync

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Ecommerce:

    def __init__(self, client) -> None:
        self._client = client
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

        return EcommerceResponse(self._client._req(payload, "POST", config))


class EcommerceAsync:

    def __init__(self, client) -> None:
        self._client = client
        self.amazon = AmazonAsync(self)
        self.google_shopping = GoogleShoppingAsync(self)
        self.universal = UniversalAsync(self)
        self.wayfair = WayfairAsync(self)
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

            result = await self._client._execute_with_timeout(
                payload, config, self._session
            )
            return EcommerceResponse(result)

        except Exception as e:
            logger.error(f"An error occurred: {e}")

        finally:
            self._requests -= 1
            if self._requests == 0:
                await utils.close(self._session)
        return EcommerceResponse(None)
