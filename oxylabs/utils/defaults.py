from . import user_agent, domain

# Constants
DEFAULT_USER_AGENT = user_agent.DESKTOP
DEFAULT_DOMAIN = domain.COM
DEFAULT_START_PAGE = 1
DEFAULT_PAGES = 1
DEFAULT_LIMIT_SERP = 10
DEFAULT_LIMIT_ECOMMERCE = 48
SYNC_BASE_URL = "https://realtime.oxylabs.io/v1/queries"
ASYNC_BASE_URL = "https://data.oxylabs.io/v1/queries"

DEFAULT_TIMEOUT = 50
DEFAULT_POLL_INTERVAL = 5


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


def set_default_sort_by(context):
    """
    Sets the default sort_by value if the provided value is None.

    Args:
        context (list): The context list of dictionaries to be checked and updated.

    Returns:
        list: The updated context list.
    """
    if context is None:
        context = []

    default_sort_by = "r"
    for item in context:
        if item.get("key") == "sort_by":
            item["value"] = item.get("value", default_sort_by)
            break
    else:
        context.append({"key": "sort_by", "value": default_sort_by})
    return context


def set_default_http_method(context):
    """
    Sets the default HTTP method if the provided method is None.

    Args:
        context (list): The context list of dictionaries to be checked and updated.

    Returns:
        list: The updated context list.
    """
    if context is None:
        context = []

    default_http_method = "get"
    for item in context:
        if item.get("key") == "http_method":
            item["value"] = item.get("value", default_http_method)
            break
    else:
        context.append({"key": "http_method", "value": default_http_method})
    return context


def set_default_content_encoding(content_encoding: str) -> str:
    """
    Set the default content encoding.

    Args:
        content_encoding (str): The content encoding to set.

    Returns:
        str: The content encoding if provided, otherwise "base64".
    """
    return content_encoding if content_encoding else "base64"


def set_default_hotel_occupancy(context):
    """
    Sets the default hotel occupancy if the provided occupancy is None.

    Args:
        context (list): The context list of dictionaries to be checked and updated.

    Returns:
        list: The updated context list.
    """
    if context is None:
        context = []

    default_occupancy = 2
    for item in context:
        if item.get("key") == "hotel_occupancy":
            item["value"] = item.get("value", default_occupancy)
            break
    else:
        context.append({"key": "hotel_occupancy", "value": default_occupancy})
    return context


def set_default_tbm_context(context):
    """
    Sets the default tbm value if the provided value is None.

    Args:
        context (list): The context list of dictionaries to be checked and updated.

    Returns:
        list: The updated context list.
    """
    if context is None:
        context = []

    default_tbm = "isch"
    for item in context:
        if item.get("key") == "tbm":
            item["value"] = item.get("value", default_tbm)
            break
    else:
        context.append({"key": "tbm", "value": default_tbm})
    return context
