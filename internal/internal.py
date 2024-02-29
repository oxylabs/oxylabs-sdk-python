import requests
import base64
from utils.defaults import DEFAULT_TIMEOUT
import aiohttp
from aiohttp import ClientTimeout
import asyncio


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
                    json=json_payload,
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

class ClientAsync:
    def __init__(self, base_url, api_credentials):
        self.base_url = base_url
        self.api_credentials = api_credentials

    async def get_job_id(self, json_payload, config):
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Basic {self.api_credentials.get_encoded_credentials()}"
        }
        timeout = ClientTimeout(total=config['timeout'])
        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(self.base_url, headers=headers, json=json_payload, timeout=timeout) as response:
                    response.raise_for_status()
                    data = await response.json()
                    return data['id']
        except aiohttp.ClientResponseError as e:
            print(f"HTTP error occurred: {e.status}")
        except aiohttp.ClientConnectionError as e:
            print(f"Connection error occurred: {e}")
        except asyncio.TimeoutError:
            print(f"Timeout error. The request to {self.base_url} has timed out.")
        except Exception as e:
            print(f"An error occurred: {e}")
        return None
            
    async def get_http_resp(self, job_id, config):
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Basic {self.api_credentials.get_encoded_credentials()}"
        }
        timeout = ClientTimeout(total=config['timeout'])
        result_url = f"{self.base_url}/{job_id}/results"
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(result_url, headers=headers, timeout=timeout) as response:
                    response.raise_for_status()
                    return await response.json()
        except aiohttp.ClientResponseError as e:
            print(f"HTTP error occurred: {e.status}")
        except aiohttp.ClientConnectionError as e:
            print(f"Connection error occurred: {e}")
        except asyncio.TimeoutError:
            print(f"Timeout error. The request to {result_url} has timed out.")
        except Exception as e:
            print(f"An error occurred: {e}")
        return None

    async def poll_job_status(self, job_id, config):
        poll_interval = config['poll_interval']
        timeout = ClientTimeout(total=config['timeout'])
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Basic {self.api_credentials.get_encoded_credentials()}"
        }
        job_status_url = f"{self.base_url}/{job_id}"
        async with aiohttp.ClientSession() as session:
            while True:
                try:
                    async with session.get(job_status_url, headers=headers, timeout=timeout) as response:
                        if response.status == 200:
                            job = await response.json()
                            print(poll_interval, job['status'])
                            if job['status'] == 'done':
                                return await self.get_http_resp(job_id, config)
                            elif job['status'] == 'faulted':
                                raise Exception("Job faulted")
                        else:
                            raise aiohttp.ClientResponseError(response.request_info, response.history, status=response.status, message=f"HTTP Error {response.status}: {await response.text()}", headers=response.headers)
                except aiohttp.ClientResponseError as e:
                    print(f"HTTP error occurred: {e.status} - {e.message}")
                    return None
                except aiohttp.ClientConnectionError as e:
                    print(f"Connection error occurred: {e}")
                    return None
                except asyncio.TimeoutError:
                    print(f"Timeout error. The request to {job_status_url} has timed out.")
                    return None
                except Exception as e:
                    print(f"Unexpected error processing your query: {e}")
                    return None
                await asyncio.sleep(poll_interval)
