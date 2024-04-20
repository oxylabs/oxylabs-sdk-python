import asyncio
import oxylabs.utils.utils as utils
from oxylabs.internal import APICredentials, Client, ClientAsync
from oxylabs.utils.defaults import ASYNC_BASE_URL, SYNC_BASE_URL


class InitSERP:
    def __init__(self, username: str, password: str) -> None:
        """
        Initializes a synchronous SERP client.

        Args:
            username (str): The username for API authentication.
            password (str): The password for API authentication.
        """
        api_credentials = APICredentials(username, password)
        self.client = Client(SYNC_BASE_URL, api_credentials)

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


class InitSERPAsync:

    def __init__(self, username: str, password: str) -> None:
        """
        Initializes an asynchronous SERP client.

        Args:
            username (str): The username for API authentication.
            password (str): The password for API authentication.
        """
        self.api_credentials = APICredentials(username, password)
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

        result: dict = None
        self.requests += 1

        try:
            self.session = await utils.ensure_session(self.session)

            result = await asyncio.wait_for(
                self.client.execute_with_timeout(
                    payload, config, self.session
                ),
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
