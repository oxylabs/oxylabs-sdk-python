import http.client

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

class Client:
    def __init__(self, base_url, api_credentials):
        """
        Initializes an instance of Client.

        Args:
            base_url (str): The base URL for the API.
            api_credentials (ApiCredentials): An instance of ApiCredentials for API authentication.
        """
        self.base_url = base_url
        self.api_credentials = api_credentials
        self.http_client = http.client.HTTPConnection(base_url)
