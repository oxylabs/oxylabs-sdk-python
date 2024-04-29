from typing import Any, List
from urllib.parse import urlparse

import aiohttp

from .defaults import (
    DEFAULT_JOB_COMPLETION_TIMEOUT,
    DEFAULT_POLL_INTERVAL,
    DEFAULT_REQUEST_TIMEOUT,
    DEFAULT_REQUEST_TIMEOUT_ASYNC,
)
from .types import domain, fn_name, locale, render, source, user_agent_type


class BaseSearchOpts:
    def __init__(
        self,
        domain: str = None,
        start_page: int = None,
        pages: int = None,
        limit: int = None,
        user_agent_type: str = None,
        callback_url: str = None,
        parsing_instructions: str = None,
    ):
        """
        Represents the base search options for a search operation.

        Args:
            domain (str): The domain to search on. Defaults to DEFAULT_DOMAIN.
            start_page (int): The starting page number. Defaults to DEFAULT_START_PAGE.
            pages (int): The number of pages to search. Defaults to DEFAULT_PAGES.
            limit (int): The maximum number of search results per page. Defaults to DEFAULT_LIMIT_SERP.
            user_agent_type (str): The user agent type to use. Defaults to DEFAULT_USER_AGENT.
            callback_url (str): The URL to send the search results callback to. Defaults to None.
            parsing_instructions (dict): Instructions for parsing the search results. Defaults to None.
        """
        self.domain = domain
        self.start_page = start_page
        self.pages = pages
        self.limit = limit
        self.user_agent_type = user_agent_type
        self.callback_url = callback_url
        self.parsing_instructions = parsing_instructions


class BaseUrlOpts:
    """Options for configuring the base URL."""

    def __init__(
        self,
        user_agent_type: str = None,
        callback_url: str = None,
        parsing_instructions: str = None,
    ):
        """
        Initialize the BaseUrlOpts class.

        Args:
            user_agent_type (str): The type of user agent to use. Defaults to DEFAULT_USER_AGENT.
            callback_url (str, optional): The callback URL to use. Defaults to None.
            parsing_instructions (dict, optional): Instructions for parsing the response. Defaults to None.
        """
        self.user_agent_type = user_agent_type
        self.callback_url = callback_url
        self.parsing_instructions = parsing_instructions


class BaseGoogleOpts:
    def __init__(
        self,
        geo_location: str = None,
        user_agent_type: str = None,
        render: bool = None,
        callback_url: str = None,
        parsing_instructions: dict = None,
        context: list = None,
    ):
        """
        Base class for Google-specific options.

        Args:
            geo_location (str, optional): The geographic location to use for the request. Defaults to None.
            user_agent_type (str, optional): The type of user agent to use. Defaults to DEFAULT_USER_AGENT.
            render (bool, optional): Whether to render JavaScript on the page. Defaults to None.
            callback_url (str, optional): The URL to send a callback request to. Defaults to None.
            parsing_instructions (dict, optional): Instructions for parsing the response. Defaults to None.
            context (list, optional): Additional context information. Defaults to None.
        """
        self.geo_location = geo_location
        self.user_agent_type = user_agent_type
        self.render = render
        self.callback_url = callback_url
        self.parsing_instructions = parsing_instructions
        self.context = context


class BaseEcommerceOpts:
    """
    Represents the options for an ecommerce request.

    Args:
        user_agent_type (str): The type of user agent to use. Defaults to DEFAULT_USER_AGENT.
        render (str): The rendering mode for the request.
        callback_url (str): The URL to which the response will be sent asynchronously.
        geo_location (str): The desired geographic location for the request.
        parsing_instructions (str): Instructions for parsing the response.
    """

    def __init__(
        self,
        user_agent_type: str = None,
        render: str = None,
        callback_url: str = None,
        geo_location: str = None,
        parsing_instructions: str = None,
    ):
        self.user_agent_type = user_agent_type
        self.callback_url = callback_url
        self.parsing_instructions = parsing_instructions
        self.render = render
        self.geo_location = geo_location


def get_valid_values(module: object) -> list:
    """
    Returns a list of valid values from the given module.

    Args:
        module (object): The module to retrieve valid values from.

    Returns:
        list: A list of valid values from the module.
    """
    return [
        getattr(module, name)
        for name in dir(module)
        if not name.startswith("__")
    ]


VALID_UAS = get_valid_values(user_agent_type)
VALID_RENDERS = get_valid_values(render)
VALID_FN_NAMES = get_valid_values(fn_name)
VALID_SOURCES = get_valid_values(source)
VALID_DOMAINS = get_valid_values(domain)
VALID_LOCALES = get_valid_values(locale)


def prepare_config(**kwargs):
    """
    Prepare a configuration dictionary based on the provided keyword arguments.

    Args:
        request_timeout (int, optional): The timeout value in seconds. Defaults to None.
        poll_interval (int, optional): The poll interval value in seconds. Defaults to None.
        job_completion_timeout (int, optional): The job completion timeout value in seconds. Defaults to None.

    Returns:
        dict: The prepared configuration dictionary.

    """
    config = {}
    config["request_timeout"] = (
        kwargs["request_timeout"]
        if kwargs.get("request_timeout") is not None
        else (
            DEFAULT_REQUEST_TIMEOUT_ASYNC
            if kwargs.get("async_integration") is not None
            else DEFAULT_REQUEST_TIMEOUT
        )
    )
    config["poll_interval"] = (
        kwargs["poll_interval"]
        if kwargs.get("poll_interval") is not None
        else DEFAULT_POLL_INTERVAL
    )
    config["job_completion_timeout"] = (
        kwargs["job_completion_timeout"]
        if kwargs.get("job_completion_timeout") is not None
        else DEFAULT_JOB_COMPLETION_TIMEOUT
    )

    return config


def validate_url(input_url: str, host: str) -> None:
    """
    Validates if the given URL is valid and belongs to the specified host.

    Args:
        input_url (str): The URL to be validated.
        host (str): The expected domain or host.

    Raises:
        ValueError: If the URL parameter is empty, missing scheme, missing host, or does not belong to the specified host.

    Returns:
        None
    """
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


def check_user_agent_type_validity(user_agent_type: str) -> None:
    """
    Check the validity of a user agent type.

    Args:
        user_agent_type (str): The user agent type to check.

    Raises:
        ValueError: If the user agent type is invalid.
    """
    if user_agent_type and user_agent_type not in VALID_UAS:
        raise ValueError(f"Invalid user agent parameter: {user_agent_type}")


def check_render_validity(render: str) -> None:
    """
    Check the validity of the render parameter.

    Args:
        render (str): The render parameter to be checked.

    Raises:
        ValueError: If the render parameter is invalid.
    """
    if render and render not in VALID_RENDERS:
        raise ValueError(f"Invalid render parameter: {render}")


def check_domain_validity(domain: str, acceptable_domains: list) -> None:
    """
    Check the validity of a domain.

    Args:
        domain (str): The domain to check.
        acceptable_domains (list): A list of acceptable domains.

    Raises:
        ValueError: If the domain is invalid.

    Returns:
        None
    """
    if domain and domain not in acceptable_domains:
        raise ValueError(f"Invalid domain parameter: {domain}")


def check_locale_validity(locale: str, acceptable_locales: list) -> None:
    """
    Check the validity of a given locale.

    Args:
        locale (str): The locale to be checked.
        acceptable_locales (list): A list of acceptable locales.

    Raises:
        ValueError: If the locale is invalid.

    Returns:
        None
    """
    if locale and locale not in acceptable_locales:
        raise ValueError(f"Invalid locale parameter: {locale}")


def check_limit_validity(limit: int) -> None:
    """
    Check the validity of the limit parameter.

    Args:
        limit: An integer representing the limit parameter.

    Raises:
        ValueError: If the limit parameter is less than or equal to 0.
    """
    if limit and limit <= 0:
        raise ValueError("Limit parameter must be greater than 0")


def check_limit_validity_ecom(limit: int) -> None:
    """
    Check the validity of the limit parameter for e-commerce.

    Args:
        limit: An integer representing the limit parameter.

    Raises:
        ValueError: If the limit parameter is not 24, 48, or 96.
    """
    if limit and limit != 24 and limit != 48 and limit != 96:
        raise ValueError("Limit parameter must be 24, 48, or 96")


def check_pages_validity(pages: int) -> None:
    """
    Check the validity of the pages parameter.

    Args:
        pages (int): The number of pages.

    Raises:
        ValueError: If pages is less than or equal to 0.
    """
    if pages and pages <= 0:
        raise ValueError("Pages parameter must be greater than 0")


def check_start_page_validity(start_page: int) -> None:
    """
    Check the validity of the start page parameter.

    Args:
        start_page (int): The start page parameter to be checked.

    Raises:
        ValueError: If the start page parameter is less than or equal to 0.
    """
    if start_page and start_page <= 0:
        raise ValueError("Start page parameter must be greater than 0")


def check_sorting_parameter_validity(
    context: List[dict], acceptable_sorting_parameters: List[str]
) -> None:
    """
    Check the validity of the sorting parameter in the given context.

    Args:
        context (List[dict]): The context containing the sorting parameter.
        acceptable_sorting_parameters (List[str]): The list of acceptable sorting parameters.

    Raises:
        ValueError: If the sorting parameter in the context is invalid.
    """
    if context and any(
        item.get("key") == "sort_by"
        and item.get("value") not in acceptable_sorting_parameters
        for item in context
    ):
        raise ValueError(
            f"Invalid sorting parameter, must be one of {acceptable_sorting_parameters}"
        )


def check_price_range_validity(context: List[dict]) -> None:
    """
    Check the validity of price range parameters.

    Args:
        context: A list of dictionaries representing the context.

    Raises:
        ValueError: If any of the price range parameters is less than 0.
    """
    if context and any(
        item.get("key") in ("min_price", "max_price")
        and item.get("value") is not None
        and item.get("value") < 0
        for item in context
    ):
        raise ValueError("Price range parameters must be greater than 0")


def check_http_method_validity(context: List[dict]) -> None:
    """
    Check the validity of the HTTP method in the given context.

    Args:
        context: A list of dictionaries representing the context.

    Raises:
        ValueError: If an invalid HTTP method is found in the context.
    """
    if context and any(
        item.get("key") == "http_method"
        and item.get("value") not in ["post", "get"]
        for item in context
    ):
        raise ValueError(
            "Invalid HTTP method in context, must be one of ['post', 'get']"
        )


def check_content_for_post_validity(context: list) -> None:
    """
    Check if the content is valid for a POST request.

    Args:
        context (list): The context containing the request information.

    Raises:
        ValueError: If the content is provided but the request method is not POST.
    """
    if (
        context
        and any(item.get("key") == "content" for item in context)
        and not any(
            item.get("key") == "http_method" and item.get("value") == "post"
            for item in context
        )
    ):
        raise ValueError("Content is only allowed for POST requests")


async def ensure_session(session) -> aiohttp.ClientSession:
    """
    Ensure the provided session is valid and return a valid session.

    Args:
        session: The session to ensure.

    Returns:
        A valid aiohttp.ClientSession object.

    """
    if session is None or session.closed:
        session = aiohttp.ClientSession()
    return session


async def close(user_session: aiohttp.ClientSession) -> None:
    """
    Closes the user session.

    Args:
        user_session: The user session to be closed.

    Returns:
        None
    """

    if user_session:
        await user_session.close()


def check_parsing_instructions_validity(instructions: dict) -> None:
    """
    Check the validity of parsing instructions.

    Args:
        instructions (dict): The parsing instructions to be validated.

    Raises:
        Exception: If the parsing instructions have an invalid structure.

    Returns:
        None
    """
    if instructions is None:
        return

    if "_fns" in instructions:
        validate_fns(instructions["_fns"])
    else:
        for key, value in instructions.items():
            if isinstance(value, dict):
                check_parsing_instructions_validity(value)
            else:
                raise Exception(f"Invalid structure for key: {key}")


def validate_fns(fns: List[Any]) -> None:
    """
    Validates a list of functions.

    Args:
        fns (list): A list of functions to validate.

    Raises:
        Exception: If `fns` is None or not a list.
    """
    if fns is None:
        raise Exception("_fns cannot be nil")
    if not isinstance(fns, list):
        raise Exception("_fns must be a list")

    for fn in fns:
        validate_fn(fn)


def validate_fn(fn: dict) -> None:
    """
    Validates the given function dictionary.

    Args:
        fn: A dictionary representing the function.

    Raises:
        ValueError: If the function dictionary is not valid.
    """
    if not isinstance(fn, dict):
        raise ValueError("Each item in _fns must be a dictionary")
    if "_fn" not in fn:
        raise ValueError("_fn must be set in each function")
    if fn["_fn"] not in VALID_FN_NAMES:
        raise ValueError(f"_fn must be a valid function name, got {fn['_fn']}")

    # Delegate to specific argument validators
    validate_fn_args(fn["_fn"], fn.get("_args"))


def validate_fn_args(function: str, args: Any) -> None:
    """
    Validate the arguments for a given function.

    Args:
        function (str): The name of the function to validate.
        args (Any): The arguments to validate.

    Raises:
        ValueError: If there is no validator for the given function name.
    """
    # Map function name to validator function
    validators = {
        fn_name.ELEMENT_TEXT: validate_empty,
        fn_name.LENGTH: validate_empty,
        fn_name.CONVERT_TO_FLOAT: validate_empty,
        fn_name.CONVERT_TO_INT: validate_empty,
        fn_name.CONVERT_TO_STR: validate_empty,
        fn_name.MAX: validate_empty,
        fn_name.MIN: validate_empty,
        fn_name.PRODUCT: validate_empty,
        fn_name.XPATH: validate_string_array,
        fn_name.XPATH_ONE: validate_string_array,
        fn_name.CSS: validate_string_array,
        fn_name.CSS_ONE: validate_string_array,
        fn_name.AMOUNT_FROM_STRING: validate_string,
        fn_name.AMOUNT_RANGE_FROM_STRING: validate_string,
        fn_name.REGEX_FIND_ALL: validate_string,
        fn_name.JOIN: validate_optional_string,
        fn_name.REGEX_SEARCH: validate_list_string_optional_int,
        fn_name.REGEX_SUBSTRING: validate_list_string_optional_int,
        fn_name.SELECT_NTH: validate_non_zero_int,
        fn_name.AVERAGE: validate_optional_int,
    }

    if function not in validators:
        raise ValueError(f"No validator for function name: {function}")

    # Call the appropriate validator
    validator = validators[function]
    validator(args)


def validate_empty(args: Any) -> None:
    """
    Validates if the given argument is empty.

    Args:
        args: The argument to be validated.

    Raises:
        ValueError: If the argument is not empty.
    """
    if args:
        raise ValueError("_args must be empty")


def validate_string_array(args: List[str]) -> None:
    """
    Validates a list of non-empty strings.

    Args:
        args: A list of strings to be validated.

    Raises:
        ValueError: If `args` is not a list of non-empty strings.
    """
    if not isinstance(args, list) or not all(
        isinstance(elem, str) and elem for elem in args
    ):
        raise ValueError("_args must be a list of non-empty strings")


def validate_string(args: str) -> None:
    """
    Validates if the given argument is a non-empty string.

    Args:
        args: The argument to be validated.

    Raises:
        ValueError: If the argument is not a non-empty string.
    """
    if not isinstance(args, str) or not args:
        raise ValueError("_args must be a non-empty string")


def validate_optional_string(args: str) -> None:
    """
    Validates if the given argument is a non-empty string or None.

    Args:
        args (str): The argument to be validated.

    Raises:
        ValueError: If the argument is not a non-empty string or None.
    """
    if args is not None and (not isinstance(args, str) or not args):
        raise ValueError("_args must be a non-empty string or None")


def validate_non_zero_int(args: int) -> None:
    """
    Validates if the given argument is a non-zero integer.

    Args:
        args (int): The argument to be validated.

    Raises:
        ValueError: If the argument is not a non-zero integer.

    Returns:
        None
    """
    if not isinstance(args, int) or args == 0:
        raise ValueError("_args must be a non-zero integer")


def validate_optional_int(args: int) -> None:
    """
    Validates if the given argument is a non-zero integer or None.

    Args:
        args (int): The argument to be validated.

    Raises:
        ValueError: If the argument is not a non-zero integer or None.
    """
    if args is not None and (not isinstance(args, int) or args == 0):
        raise ValueError("_args must be a non-zero integer or None")


def validate_list_string_optional_int(args: list) -> None:
    """
    Validates the input arguments.

    Args:
        args: A list containing the arguments to be validated.

    Raises:
        ValueError: If the first argument is not a non-empty string or if the second argument is not a non-zero integer when present.
    """
    if (
        not isinstance(args, list)
        or len(args) < 1
        or not isinstance(args[0], str)
        or not args[0]
    ):
        raise ValueError("_args first argument must be a non-empty string")
    if len(args) > 1 and (not isinstance(args[1], int) or args[1] == 0):
        raise ValueError(
            "_args second argument must be a non-zero integer when present"
        )


def check_context_tbm_validity(
    context: List[dict], acceptable_tbms: List[str]
) -> None:
    """
    Check the validity of the 'tbm' parameter value in the given context.

    Args:
        context: A list of dictionaries representing the context.
        acceptable_tbms: A list of acceptable 'tbm' parameter values.

    Raises:
        ValueError: If the 'tbm' parameter value in the context is invalid.
    """
    if context and any(
        item.get("key") == "tbm" and item.get("value") not in acceptable_tbms
        for item in context
    ):
        raise ValueError("Invalid tbm parameter value in context")
