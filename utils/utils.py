import dataclasses
from utils.constants import UserAgent, Domain


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
    """
    domain: Domain = None
    start_page: int = 1
    pages: int = 1
    limit: int = 10
    user_agent: UserAgent = UserAgent.UA_DESKTOP
    callback_url: str = None
    parse_instructions: dict = None
    poll_interval: int = 0

@dataclasses.dataclass
class BaseUrlOpts:
    """
    Represents the options for the base URL.

    Args:
        user_agent (UserAgent): The user agent to use for the search.
        callback_url (str): The URL to send the search results to.
        parse_instructions (dict): The instructions for parsing the search results.
        poll_interval (int): The interval (in seconds) between polling for search results.
    """
    user_agent: UserAgent
    callback_url: str
    parse_instructions: dict
    poll_interval: int
