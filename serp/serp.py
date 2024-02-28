from internal.internal import Client, ApiCredentials
from utils.defaults import SYNC_BASE_URL
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

    def send_post_request_with_payload(self, payload, timeout):
        # remove empty or null values
        payload = {k: v for k, v in payload.items() if v is not None}

        # Convert payload to JSON
        json_payload = json.dumps(payload)
        
        return self.client.req(json_payload, "POST",timeout)


class SerpClientAsync:
    def __init__(self, username, password):
        """
        Initializes an asynchronous SERP client.

        Args:
            username (str): The username for API authentication.
            password (str): The password for API authentication.
        """
        api_credentials = ApiCredentials(username, password)
        self.client = Client("AsyncBaseUrl", api_credentials)


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
