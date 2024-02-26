import requests
import base64
import aiohttp
import asyncio
from utils.utils import Config


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

    def req(self, json_payload, method):
        # Prepare headers
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Basic {self.api_credentials.get_encoded_credentials()}",
        }

        config = Config()
        timeout = config.timeout
        print(f"Timeout in internal: {timeout}")

        # Make the request
        try:
            if method == "POST":
                response = requests.post(
                    self.base_url, headers=headers, data=json_payload, timeout=timeout
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
            return None
        except requests.exceptions.RequestException as err:
            print(f"Error occurred: {err}")
            return None

class ClientAsync:
    def __init__(self, base_url, api_credentials):
        self.base_url = base_url
        self.api_credentials = api_credentials

    async def get_job_id(self, json_payload):
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Basic {self.api_credentials.get_encoded_credentials()}"
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(self.base_url, headers=headers, json=json_payload) as response:
                response.raise_for_status()
                data = await response.json()
                return data['id']
            
    async def get_http_resp(self, job_id):
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Basic {self.api_credentials.get_encoded_credentials()}"
        }
        result_url = f"{self.base_url}/{job_id}/results"
        async with aiohttp.ClientSession() as session:
            async with session.get(result_url, headers=headers) as response:
                response.raise_for_status()
                return await response.json()

    async def poll_job_status(self, job_id, poll_interval=5):
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Basic {self.api_credentials.get_encoded_credentials()}"
        }
        job_status_url = f"{self.base_url}/{job_id}"
        async with aiohttp.ClientSession() as session:
            while True:
                async with session.get(job_status_url, headers=headers) as response:
                    response.raise_for_status()
                    job = await response.json()
                    print("status", job['status'])
                    if job['status'] == 'done':
                        resp = await self.get_http_resp(job_id)
                        return resp
                    elif job['status'] == 'faulted':
                        raise Exception("Job faulted")
                await asyncio.sleep(poll_interval)

