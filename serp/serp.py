from internal.internal import Client, ApiCredentials, ClientAsync
from utils.defaults import SYNC_BASE_URL, ASYNC_BASE_URL
import json
import requests
from urllib.parse import urljoin
from requests.adapters import HTTPAdapter
from urllib3.util.ssl_ import create_urllib3_context
from urllib.parse import quote


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

    def send_post_request_with_payload(self, payload, config):
        # remove empty or null values
        payload = {k: v for k, v in payload.items() if v is not None}

        return self.client.req(payload, "POST", config)


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

    async def get_job_id(self, json_payload, config):
        """
        Wrapper method to get a job ID for a given payload.

        Args:
            json_payload (dict): The JSON payload for the job.

        Returns:
            str: The job ID.
        """
        return await self.client.get_job_id(json_payload, config)

    async def poll_job_status(self, job_id, config):
        """
        Wrapper method to poll the status of a job until it's completed.

        Args:
            job_id (str): The job ID to poll.
            poll_interval (int, optional): The interval between status checks. Defaults to 5 seconds.

        Returns:
            None: This method returns None but will raise an exception if the job is faulted.
        """
        return await self.client.poll_job_status(job_id, config)


class TLSAdapter(HTTPAdapter):
    def init_poolmanager(self, *args, **kwargs):
        context = create_urllib3_context()
        kwargs["ssl_context"] = context
        return super().init_poolmanager(*args, **kwargs)


class SerpProxyClient:
    def __init__(self, username, password):
        username = quote(username)
        password = quote(password)
        proxy_url = f"http://{username}:{password}@realtime.oxylabs.io:60000"
        self.session = requests.Session()
        self.session.proxies = {"http": proxy_url, "https": proxy_url}
        self.session.mount("https://", TLSAdapter())
        self.session.verify = False

    def get(self, url):
        try:
            response = self.session.get(url)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            return None

    def add_user_agent_header(self, user_agent):
        self.session.headers["x-oxylabs-user-agent-type"] = user_agent

    def add_render_header(self, render):
        self.session.headers["x-oxylabs-render"] = render

    def add_parse_header(self, parser):
        self.session.headers["x-oxylabs-parse"] = "1"
        self.session.headers["x-oxylabs-parser"] = parser
