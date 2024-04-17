from urllib.parse import quote
from oxylabs.utils.defaults import PROXY_BASE_URL, PROXY_PORT

import requests


class Proxy:
    def __init__(self, username: str, password: str) -> None:
        """
        Initializes a Proxy object with the provided username and password.

        Args:
            username (str): The username for the proxy authentication.
            password (str): The password for the proxy authentication.
        """
        self.username = quote(username)
        self.password = quote(password)
        self.proxy_url = self._build_proxy_url()
        self.session = requests.Session()
        self.session.proxies = {"http": self.proxy_url, "https": self.proxy_url}
        self.session.verify = False

    def _build_proxy_url(self) -> str:
        """
        Build the proxy URL using configured constants.

        Returns:
            str: The constructed proxy URL.
        """
        return f"http://{self.username}:{self.password}@{PROXY_BASE_URL}:{PROXY_PORT}"

    def get(self, url: str) -> requests.Response:
        """
        Sends a GET request to the specified URL using the session object.

        Args:
            url (str): The URL to send the GET request to.

        Returns:
            requests.Response: The response object returned by the GET request.

        Raises:
            requests.exceptions.RequestException: If the GET request encounters an error.
        """
        try:
            response = self.session.get(url)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            return None

    def add_user_agent_header(self, user_agent: str) -> None:
        """
        Adds a user agent header to the session headers.
        There is no way to indicate a specific User-Agent, but you can let us know which user-agent type you would like us to use.

        Args:
            user_agent (str): The user agent to add. Must be one of the following:
            - "desktop"         - A User-Agent of a desktop browser.
            - "desktop_chrome"  - A User-Agent of one of the latest versions of a desktop Chrome browser.
            - "desktop_edge"    - A User-Agent of one of the latest versions of a desktop Edge browser.
            - "desktop_firefox" - A User-Agent of one of the latest versions of a desktop Firefox browser.
            - "desktop_opera"   - A User-Agent of one of the latest versions of a desktop Opera browser.
            - "desktop_safari"  - A User-Agent of one of the latest versions of a desktop Safari browser.
            - "mobile"          - A User-Agent of a mobile browser.
            - "mobile_android"  - A User-Agent of one of the latest versions of an Android mobile browser.
            - "mobile_ios"      - A User-Agent of one of the latest versions of an iOS mobile browser.
            - "tablet"          - A User-Agent of a tablet browser.
            - "tablet_android"  - A User-Agent of one of the latest versions of an Android tablet browser.
            - "tablet_ios"      - A User-Agent of one of the latest versions of an iOS tablet browser.

        Returns:
            None
        """
        self.session.headers["x-oxylabs-user-agent-type"] = user_agent

    def add_render_header(self, render: str) -> None:
        """
        Adds a render header to the session headers.

        Args:
            render (str): The render type to add. Must be one of the following:
            - "html" - The output will include an HTML result.
            - "png"  - The output will include a PNG screenshot of the result.

        Returns:
            None
        """
        self.session.headers["x-oxylabs-render"] = render

    def add_parse_header(self, parser_type: str) -> None:
        """
        Adds a parse header to the session headers.
        Setting this will return parsed data for the targets for which we have dedicated parsers.

        Args:
            parser (str): The parser to add. Must be one of the following:
            - For Google:               "google", "google_search", "google_ads", "google_images"
            - For Google Shopping:      "google_shopping", "google_shopping_search", "google_shopping_product", "google_shopping_pricing"
            - For Amazon:               "amazon", "amazon_search", "amazon_product", "amazon_pricing", "amazon_reviews", "amazon_questions", "amazon_bestsellers", "amazon_sellers"
            - For Best Buy:             "universal_ecommerce"
            - For Etsy:                 "universal_ecommerce"
            - For Target:               "universal_ecommerce"
            - For Walmart:              "universal_ecommerce"

        Returns:
            None
        """
        self.session.headers["x-oxylabs-parse"] = "1"
        self.session.headers["x-oxylabs-parser-type"] = parser_type

    def add_geo_location_header(self, geo_location: str) -> None:
        """
        Adds a geo location header to the session headers.
        In some cases, you may need to indicate the geographical location that the result should be adapted for.

        Args:
            geo_location (str): The geo location to add. Accepted values depend on the URL you would like us to scrape.

        Returns:
            None
        """
        self.session.headers["x-oxylabs-geo-location"] = geo_location
