import requests
import base64
from utils.defaults import DEFAULT_TIMEOUT


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
    def __init__(self, base_url, api_credentials):
        self.base_url = base_url
        self.api_credentials = api_credentials

    def req(self, json_payload, method, timeout):
        # Prepare headers
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Basic {self.api_credentials.get_encoded_credentials()}",
        }

        # Make the request
        try:
            if method == "POST":
                response = requests.post(
                    self.base_url,
                    headers=headers,
                    data=json_payload,
                    timeout=timeout if timeout else DEFAULT_TIMEOUT,
                )
            elif method == "GET":
                response = requests.get(self.base_url, headers=headers, timeout=timeout)
            else:
                print(f"Unsupported method: {method}")
                return None

            response.raise_for_status()

            if response.status_code == 200:
                return response.json()
            else:
                print(f"Error occurred: {response.status_code}")
                return None

        except requests.exceptions.Timeout:
            print(
                f"Timeout error. The request to {self.base_url} with method {method} has timed out."
            )
            return None
        except requests.exceptions.HTTPError as err:
            print(f"HTTP error occurred: {err}")
            print(response.text)
            return None
        except requests.exceptions.RequestException as err:
            print(f"Error occurred: {err}")
            return None
