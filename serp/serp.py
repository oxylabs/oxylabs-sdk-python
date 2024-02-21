from internal.internal import Client, ApiCredentials
from typing import Optional
from utils.defaults import SYNC_BASE_URL
import requests

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

    def req(self, json_payload: dict, method: str) -> Optional[requests.Response]:
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
        self.client = Client('AsyncBaseUrl', api_credentials)
