from typing import Optional
from urllib.parse import quote, urlparse

import requests

from src.oxylabs.utils.defaults import (
    NON_UNIVERSAL_DOMAINS,
    PROXY_BASE_URL,
    PROXY_PORT,
)
from src.oxylabs.utils.utils import prepare_config


class Proxy:
    def __init__(self, username: str, password: str) -> None:
        """
        Initializes a Proxy object with the provided username and password.

        Args:
            username (str): The username for the proxy authentication.
            password (str): The password for the proxy authentication.
        """
        self._username = quote(username)
        self._password = quote(password)
        self._proxy_url = self._build_proxy_url()
        self._session = requests.Session()
        self._session.proxies = {
            "http": self._proxy_url,
            "https": self._proxy_url,
        }
        self._session.verify = False
        self._url_to_scrape = None

    def _build_proxy_url(self) -> str:
        """
        Build the proxy URL using configured constants.

        Returns:
            str: The constructed proxy URL.
        """
        return f"http://{self._username}:{self._password}@{PROXY_BASE_URL}:{PROXY_PORT}"

    def get(
        self, url: str, request_timeout: Optional[int] = None
    ) -> Optional[requests.Response]:
        """
        Sends a GET request to the specified URL using the session object.

        Args:
            url (str): The URL to send the GET request to.
            request_timeout (Optional[int]): The request timeout in seconds. Defaults to None (no timeout).

        Returns:
            Optional[requests.Response]: The response object returned by the GET request, or None if an error occurred.
        """
        try:
            config = prepare_config(request_timeout=request_timeout)
            self._url_to_scrape = url
            response = self._session.get(
                url, timeout=config["request_timeout"]
            )
            response.raise_for_status()
            return response
        except requests.exceptions.Timeout:
            print(
                f"Timeout error. The request to {url} has timed out after {request_timeout} seconds."
            )
            return None
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            return None

    def add_user_agent_header(self, user_agent_type: str) -> None:
        """
        Adds a user agent header to the session headers.
        There is no way to indicate a specific User-Agent, but you can let us know which user-agent type you would like us to use.

        Args:
            user_agent_type (str): The user agent to add. Must be one of the following:
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
        self._session.headers["x-oxylabs-user-agent-type"] = user_agent_type

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
        self._session.headers["x-oxylabs-render"] = render

    def add_parse_header(
        self, parse: bool = False, parsing_instructions: Optional[dict] = None
    ) -> None:
        """
        Adds a parse header to the session headers.

        Args:
            parse (bool, optional): Whether to enable parsing. Defaults to False.
            parsing_instructions (dict, optional): Instructions for parsing. Defaults to None.

        Returns:
            None
        """

        if parse or parsing_instructions:
            self._session.headers["x-oxylabs-parse"] = "1"
            if self._is_universal_source():
                self._session.headers["x-oxylabs-parser-type"] = (
                    "universal_ecommerce"
                )
            else:
                self._session.headers.pop("x-oxylabs-parser-type", None)
        else:
            self._session.headers.pop("x-oxylabs-parse", None)

    def _is_universal_source(self) -> bool:
        """
        Checks if the URL to scrape belongs to a universal source.

        Returns:
            bool: True if the URL belongs to a universal source, False otherwise.
        """
        parsed_url = urlparse(self._url_to_scrape)
        if any(
            domain in parsed_url.netloc.decode()
            for domain in NON_UNIVERSAL_DOMAINS
        ):
            return False

        return True

    def add_geo_location_header(self, geo_location: str) -> None:
        """
        Adds a geo location header to the session headers.
        In some cases, you may need to indicate the geographical location that the result should be adapted for.

        Args:
            geo_location (str): The geo location to add. Accepted values depend on the URL you would like us to scrape.

        Returns:
            None
        """
        self._session.headers["x-oxylabs-geo-location"] = geo_location
