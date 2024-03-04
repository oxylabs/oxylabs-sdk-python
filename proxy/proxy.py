import requests
from urllib.parse import quote

class Proxy:
    def __init__(self, username, password):
        self.username = quote(username)
        self.password = quote(password)
        self.proxy_url = f"http://{self.username}:{self.password}@realtime.oxylabs.io:60000"
        self.session = requests.Session()
        self.session.proxies = {"http": self.proxy_url}
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

    def add_geo_location_header(self, geo_location):
        self.session.headers["x-oxylabs-geo-location"] = geo_location
