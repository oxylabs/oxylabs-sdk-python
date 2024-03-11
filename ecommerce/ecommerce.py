from internal.internal import Client, ApiCredentials, ClientAsync
from utils.defaults import SYNC_BASE_URL, ASYNC_BASE_URL
import asyncio
import utils.utils as utils


class Ecommerce:
    def __init__(self, username, password):
        """
        Initializes a synchronous Ecommerce client.

        Args:
            username (str): The username for API authentication.
            password (str): The password for API authentication.
        """
        api_credentials = ApiCredentials(username, password)
        self.client = Client(SYNC_BASE_URL, api_credentials)

    def get_resp(self, payload, config):
        """
        Processes the payload synchronously and fetches api response.

        Args:
            payload (dict): The payload for the request.

        Returns:
            dict: The response from the server after the job is completed.
        """
        # Remove empty or null values from the payload
        payload = {k: v for k, v in payload.items() if v is not None}

        return self.client.req(payload, "POST", config)


class EcommerceAsync:
    _requests = 0

    def __init__(self, username, password):
        """
        Initializes an asynchronous Ecommerce client.

        Args:
            username (str): The username for API authentication.
            password (str): The password for API authentication.
        """
        self.api_credentials = ApiCredentials(username, password)
        self.client = ClientAsync(ASYNC_BASE_URL, self.api_credentials)
        self.session = None

    async def get_resp(self, payload, config):
        """
        Processes the payload asynchronously and fetches api response.

        Args:
            payload (dict): The payload for the request.

        Returns:
            dict: The response from the server after the job is completed.
        """
        # Remove empty or null values from the payload
        payload = {k: v for k, v in payload.items() if v is not None}

        result = None
        type(self)._requests += 1

        try:
            self.session = await utils.ensure_session(self.session)

            result = await asyncio.wait_for(
                self.client.execute_with_timeout(payload, config, self.session),
                timeout=config["timeout"],
            )
            type(self)._requests -= 1

            if type(self)._requests == 0:
                await utils.close(self.session)

            return result
        except asyncio.TimeoutError:
            print("The request timed out")
        except Exception as e:
            print(f"An error occurred: {e}")
        return None
