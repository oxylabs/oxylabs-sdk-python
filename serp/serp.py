from internal.internal import Client, ApiCredentials, ClientAsync
from utils.defaults import SYNC_BASE_URL, ASYNC_BASE_URL


class Serp:
    def __init__(self, username, password):
        """
        Initializes a synchronous SERP client.

        Args:
            username (str): The username for API authentication.
            password (str): The password for API authentication.
        """
        api_credentials = ApiCredentials(username, password)
        self.client = Client(SYNC_BASE_URL, api_credentials)

    def get_resp(self, payload, config):
        # remove empty or null values
        payload = {k: v for k, v in payload.items() if v is not None}

        return self.client.req(payload, "POST", config)


class SerpAsync:
    def __init__(self, username, password):
        """
        Initializes an asynchronous SERP client.

        Args:
            username (str): The username for API authentication.
            password (str): The password for API authentication.
        """
        api_credentials = ApiCredentials(username, password)
        self.client = ClientAsync(ASYNC_BASE_URL, api_credentials)

    async def get_resp(self, payload, config):
        """
        Processes the payload asynchronously, starts a job, polls for its completion, and retrieves the results.

        Args:
            payload (dict): The payload for the request.

        Returns:
            The response from the server after the job is completed.
        """
        # Remove empty or null values from the payload
        payload = {k: v for k, v in payload.items() if v is not None}

        # Start the job and get its ID
        job_id = await self.client.get_job_id(payload, config)

        # Poll for the job status until completion and return the results
        return await self.client.poll_job_status(job_id, config)
