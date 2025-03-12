from typing import Any, List
from urllib.parse import urlparse

import aiohttp

from .defaults import (
    DEFAULT_JOB_COMPLETION_TIMEOUT,
    DEFAULT_POLL_INTERVAL,
    DEFAULT_REQUEST_TIMEOUT,
    DEFAULT_REQUEST_TIMEOUT_ASYNC,
)
from .types import fn_name


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


VALID_FN_NAMES = get_valid_values(fn_name)


def prepare_config(**kwargs):
    """
    Prepare a configuration dictionary based on the provided keyword arguments.

    Args:
        request_timeout (int, optional): The timeout value in seconds. Defaults
        to None.
        poll_interval (int, optional): The poll interval value in seconds.
        Defaults to None.
        job_completion_timeout (int, optional): The job completion timeout
        value in seconds. Defaults to None.

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
        ValueError: If the URL parameter is empty, missing scheme, missing
        host, or does not belong to the specified host.

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


async def close_session(user_session: aiohttp.ClientSession) -> None:
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
        ValueError: If the first argument is not a non-empty string or if the
        second argument is not a non-zero integer when present.
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
