from utils.constants import UserAgent, Domain
from datetime import timedelta

# Constants
DEFAULT_USER_AGENT = UserAgent.UA_DESKTOP.value
DEFAULT_DOMAIN = Domain.DOMAIN_COM.value
DEFAULT_START_PAGE = 1
DEFAULT_PAGES = 1
DEFAULT_LIMIT_SERP = 10
DEFAULT_LIMIT_ECOMMERCE = 48
SYNC_BASE_URL = "https://realtime.oxylabs.io/v1/queries"
ASYNC_BASE_URL = "https://data.oxylabs.io/v1/queries"

DEFAULT_TIMEOUT = 50
DEFAULT_POLL_INTERVAL = 2


# Functions to set default values
def set_default_domain(domain: str) -> str:
    """
    Sets the default domain for the application.

    Parameters:
    - domain (str): The domain to be set as the default.

    Returns:
    - str: The updated default domain.
    """
    return domain if domain else DEFAULT_DOMAIN


def set_default_start_page(start_page: int) -> int:
    """
    Sets the default start page for the application.

    Parameters:
    - start_page (int): The start page to be set.

    Returns:
    - int: The start page that was set as the default, or the default start page if start_page is None.
    """
    return start_page if start_page is not None else DEFAULT_START_PAGE


def set_default_pages(pages: int) -> int:
    """
    Sets the default number of pages.

    Args:
    - pages (int): The number of pages to set as default.

    Returns:
    - int: The default number of pages.

    """
    return pages if pages is not None else DEFAULT_PAGES


def set_default_limit(limit: int, default_limit: int) -> int:
    """
    Sets the default limit if the limit is not provided.

    Args:
    - limit (int): The limit value.
    - default_limit (int): The default limit value.

    Returns:
    - int: The limit value if provided, otherwise the default limit value.
    """
    return limit if limit is not None else default_limit


def set_default_user_agent(user_agent):
    """
    Sets the default user agent if provided, otherwise returns the default user agent.

    Args:
        user_agent (str): The user agent string to set as the default.

    Returns:
        str: The default user agent.
    """
    return user_agent if user_agent is not None else DEFAULT_USER_AGENT


def set_default_sort_by(ctx: dict) -> str:
    """
    Sets the default sort_by value based on the provided context.

    Args:
        ctx (dict): The context containing the sort_by value.

    Returns:
        str: The default sort_by value. If not found in the context, "r" is returned.
    """
    return ctx.get("sort_by", "r")


def set_default_http_method(ctx: dict) -> str:
    """
    Sets the default HTTP method for the given context.

    Args:
        ctx (dict): The context containing the HTTP method.

    Returns:
        str: The default HTTP method. If not specified in the context, "get" is returned.
    """
    return ctx.get("http_method", "get")


def set_default_content_encoding(content_encoding: str) -> str:
    """
    Set the default content encoding.

    Args:
        content_encoding (str): The content encoding to set.

    Returns:
        str: The content encoding if provided, otherwise "base64".
    """
    return content_encoding if content_encoding else "base64"


def set_default_hotel_occupancy(occupancy):
    """
    Sets the default hotel occupancy if the provided occupancy is None.

    Args:
        occupancy (int): The occupancy value to be checked.

    Returns:
        int: The default occupancy value if the provided occupancy is None, otherwise returns the provided occupancy.
    """
    default_occupancy = 2
    if occupancy is None:
        return default_occupancy
    return occupancy
