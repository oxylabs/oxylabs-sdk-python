from internal.internal import Client, ApiCredentials, ClientAsync
from utils.defaults import SYNC_BASE_URL, ASYNC_BASE_URL


class SerpClient:
    def __init__(self, username, password):
        """
        Initializes a synchronous SERP client.

        Args:
            username (str): The username for API authentication.
            password (str): The password for API authentication.
        """
        api_credentials = ApiCredentials(username, password)
        self.client = Client(SYNC_BASE_URL, api_credentials)

    def req(self, json_payload, method):
        """
        Proxy method to call the req method of the internal client.

        Args:
            json_payload (dict): The JSON payload to send.
            method (str): The HTTP method to use ("POST" or "GET").

        Returns:
            Optional[requests.Response]: The response object if successful, else None.
        """
        return self.client.req(json_payload, method)


class SerpClientAsync:
    def __init__(self, username, password):
        """
        Initializes an asynchronous SERP client.

        Args:
            username (str): The username for API authentication.
            password (str): The password for API authentication.
        """
        api_credentials = ApiCredentials(username, password)
        self.client = ClientAsync(ASYNC_BASE_URL, api_credentials)

    async def get_job_id(self, json_payload):
        """
        Wrapper method to get a job ID for a given payload.

        Args:
            json_payload (dict): The JSON payload for the job.

        Returns:
            str: The job ID.
        """
        return await self.client.get_job_id(json_payload)

    async def poll_job_status(self, job_id, poll_interval=5):
        """
        Wrapper method to poll the status of a job until it's completed.

        Args:
            job_id (str): The job ID to poll.
            poll_interval (int, optional): The interval between status checks. Defaults to 5 seconds.

        Returns:
            None: This method returns None but will raise an exception if the job is faulted.
        """
        await self.client.poll_job_status(job_id, poll_interval)

    async def get_http_resp(self, job_id):
        """
        Wrapper method to get the HTTP response for a completed job.

        Args:
            job_id (str): The job ID whose results are to be fetched.

        Returns:
            dict: The JSON response containing the job's results.
        """
        return await self.client.get_http_resp(job_id)
