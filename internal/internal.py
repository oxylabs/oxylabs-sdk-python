import requests
import json
from typing import Optional
import base64

class ApiCredentials:
    def __init__(self, username, password):
        """
        Initializes an instance of ApiCredentials.

        Args:
            username (str): The username for API authentication.
            password (str): The password for API authentication.
        """
        self.username = username
        self.password = password

    def get_encoded_credentials(self):
        """
        Returns the Base64 encoded username and password for API authentication.
        """
        credentials = f"{self.username}:{self.password}"
        return base64.b64encode(credentials.encode()).decode()


class Client:
    def __init__(self, base_url: str, api_credentials: ApiCredentials):
        self.base_url = base_url
        self.api_credentials = api_credentials

    def req(self, json_payload: dict, method: str) -> Optional[requests.Response]:
        # Prepare headers
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Basic {self.api_credentials.get_encoded_credentials()}"
        }

        # Make the request
        try:
            if method == "POST":
                response = requests.post(self.base_url, headers=headers, data=json_payload, timeout=50)
            elif method == "GET":
                response = requests.get(self.base_url, headers=headers, timeout=50)
            else:
                print(f"Unsupported method: {method}")
                return None

            response.raise_for_status()
            return response

        except requests.exceptions.Timeout:
            print("Timeout error")
            return None
        except requests.exceptions.HTTPError as err:
            print(f"HTTP error occurred: {err}")
            return None
        except requests.exceptions.RequestException as err:
            print(f"Error occurred: {err}")
            return None
