import dataclasses
from utils.constants import UserAgent, Domain, Render
from urllib.parse import urlparse
from utils.defaults import DEFAULT_TIMEOUT


@dataclasses.dataclass
class BaseSearchOpts:
    """
    Represents the base search options for performing a search.

    Args:
        domain (Domain): The domain to search on.
        start_page (int): The starting page number.
        pages (int): The number of pages to search.
        limit (int): The maximum number of results to retrieve.
        user_agent (UserAgent): The user agent to use for the search.
        callback_url (str): The URL to send the search results to.
        parse_instructions (dict): The instructions for parsing the search results.
        poll_interval (int): The interval (in seconds) between polling for search results.
        parse (bool): Whether to parse the search results.
    """

    domain: Domain = None
    start_page: int = 1
    pages: int = 1
    limit: int = 10
    user_agent_type: UserAgent = UserAgent.UA_DESKTOP.value
    callback_url: str = None
    parse_instructions: dict = None
    poll_interval: int = 0
    parse: bool = False


@dataclasses.dataclass
class BaseUrlOpts:
    """
    Represents the options for the base URL.

    Args:
        user_agent (UserAgent): The user agent to use for the search.
        callback_url (str): The URL to send the search results to.
        parse_instructions (dict): The instructions for parsing the search results.
        poll_interval (int): The interval (in seconds) between polling for search results.
        parse (bool): Whether to parse the search results.
    """

    user_agent_type: UserAgent = UserAgent.UA_DESKTOP.value
    callback_url: str = None
    parse_instructions: dict = None
    poll_interval: int = 0
    parse: bool = False


@dataclasses.dataclass
class BaseGoogleOpts:
    geo_location: str = None
    user_agent_type: UserAgent = UserAgent.UA_DESKTOP.value
    render: Render = None
    callback_url: str = None
    parse_instructions: dict = None
    parse: bool = False
    context: list = None



class Config:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Config, cls).__new__(cls, *args, **kwargs)
            cls._instance.timeout = DEFAULT_TIMEOUT
        return cls._instance

    def set_timeout(self, timeout):
        self.timeout = timeout
        return self.timeout

    def reset_timeout(self):
        self.timeout = DEFAULT_TIMEOUT


def validate_url(input_url, host):
    # Check if the URL is empty
    if not input_url:
        raise ValueError("URL parameter is empty")

    # Parse the URL
    parsed_url = urlparse(input_url)

    # Check if the scheme (protocol) is present and not empty
    if not parsed_url.scheme:
        raise ValueError("URL is missing scheme")

    # Check if the host is present and not empty
    if not parsed_url.netloc:
        raise ValueError("URL is missing a host")

    # Check if the host matches the expected domain or host
    if host not in parsed_url.netloc:
        raise ValueError(f"URL does not belong to {host}")

    return None


def check_user_agent_validity(user_agent_type):
    if not UserAgent.is_user_agent_valid(user_agent_type):
        raise ValueError(f"Invalid user agent parameter: {user_agent_type}")


def check_render_validity(render):
    if render and not Render.is_render_valid(render):
        raise ValueError(f"Invalid render parameter: {render}")


def check_domain_validity(domain, acceptable_domains):
    if domain and domain not in acceptable_domains:
        raise ValueError(f"Invalid domain parameter: {domain}")


def check_locale_validity(locale, acceptable_locales):
    if locale and locale not in acceptable_locales:
        raise ValueError(f"Invalid locale parameter: {locale}")


def check_limit_validity(limit):
    if limit <= 0:
        raise ValueError("Limit parameter must be greater than 0")


def check_pages_validity(pages):
    if pages <= 0:
        raise ValueError("Pages parameter must be greater than 0")


def check_start_page_validity(start_page):
    if start_page <= 0:
        raise ValueError("Start page parameter must be greater than 0")
