from urllib.parse import urlparse
import aiohttp
from utils import user_agent, render, fn_name, source, domain, locale

from utils.defaults import (
    DEFAULT_LIMIT_SERP,
    DEFAULT_DOMAIN,
    DEFAULT_START_PAGE,
    DEFAULT_USER_AGENT,
    DEFAULT_PAGES,
    DEFAULT_POLL_INTERVAL,
    DEFAULT_TIMEOUT,
)


class BaseSearchOpts:
    def __init__(
        self,
        domain=DEFAULT_DOMAIN,
        start_page=DEFAULT_START_PAGE,
        pages=DEFAULT_PAGES,
        limit=DEFAULT_LIMIT_SERP,
        user_agent_type=DEFAULT_USER_AGENT,
        callback_url=None,
        parsing_instructions=None,
    ):
        self.domain = domain
        self.start_page = start_page
        self.pages = pages
        self.limit = limit
        self.user_agent_type = user_agent_type
        self.callback_url = callback_url
        self.parsing_instructions = parsing_instructions


class BaseUrlOpts:
    def __init__(
        self,
        user_agent_type=DEFAULT_USER_AGENT,
        callback_url=None,
        parsing_instructions=None,
    ):
        self.user_agent_type = user_agent_type
        self.callback_url = callback_url
        self.parsing_instructions = parsing_instructions


class BaseGoogleOpts:
    def __init__(
        self,
        geo_location=None,
        user_agent_type=DEFAULT_USER_AGENT,
        render=None,
        callback_url=None,
        parsing_instructions=None,
        context=None,
    ):
        self.geo_location = geo_location
        self.user_agent_type = user_agent_type
        self.render = render
        self.callback_url = callback_url
        self.parsing_instructions = parsing_instructions

        self.context = context


class BaseEcommerceOpts:
    def __init__(
        self,
        user_agent_type=DEFAULT_USER_AGENT,
        render=None,
        callback_url=None,
        geo_location=None,
        parsing_instructions=None,
    ):
        self.user_agent_type = user_agent_type
        self.callback_url = callback_url
        self.parsing_instructions = parsing_instructions
        self.render = render
        self.geo_location = geo_location


def get_valid_values(module):
    return [getattr(module, name) for name in dir(module) if not name.startswith("__")]


VALID_UAS = get_valid_values(user_agent)
VALID_RENDERS = get_valid_values(render)
VALID_FN_NAMES = get_valid_values(fn_name)
VALID_SOURCES = get_valid_values(source)
VALID_DOMAINS = get_valid_values(domain)
VALID_LOCALES = get_valid_values(locale)


def prepare_config(**kwargs):
    config = {}
    if "timeout" in kwargs:
        config["timeout"] = (
            kwargs["timeout"] if kwargs["timeout"] is not None else DEFAULT_TIMEOUT
        )
    if "poll_interval" in kwargs:
        config["poll_interval"] = (
            kwargs["poll_interval"]
            if kwargs["poll_interval"] is not None
            else DEFAULT_POLL_INTERVAL
        )
    return config


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
    if user_agent_type and not user_agent_type in VALID_UAS:
        raise ValueError(f"Invalid user agent parameter: {user_agent_type}")


def check_render_validity(render):
    if render and not render in VALID_RENDERS:
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


def check_limit_validity_ecom(limit):
    if limit != 24 and limit != 48 and limit != 96:
        raise ValueError("Limit parameter must be 24, 48, or 96")


def check_pages_validity(pages):
    if pages <= 0:
        raise ValueError("Pages parameter must be greater than 0")


def check_start_page_validity(start_page):
    if start_page <= 0:
        raise ValueError("Start page parameter must be greater than 0")


def check_sorting_parameter_validity(context, acceptable_sorting_parameters):
    if context and any(
        item.get("key") == "sort_by"
        and item.get("value") not in acceptable_sorting_parameters
        for item in context
    ):
        raise ValueError("Invalid sorting parameter")


def check_price_range_validity(context):
    if context and any(
        item.get("key") in ("min_price", "max_price")
        and item.get("value") is not None
        and item.get("value") < 0
        for item in context
    ):
        raise ValueError("Price range parameters must be greater than 0")


def check_http_method_validity(context):
    if context and any(
        item.get("key") == "http_method" and item.get("value") not in ["post", "get"]
        for item in context
    ):
        raise ValueError("Invalid http method in context")


def check_content_for_post_validity(context):
    if (
        context
        and any(item.get("key") == "content" for item in context)
        and not any(
            item.get("key") == "http_method" and item.get("value") == "post"
            for item in context
        )
    ):
        raise ValueError("Content is only allowed for POST requests")


async def ensure_session(session):
    if session is None or session.closed:
        session = aiohttp.ClientSession()
    return session


async def close(user_session):
    if user_session:
        await user_session.close()


def check_parsing_instructions_validity(instructions):
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


def validate_fns(fns):
    if fns is None:
        raise Exception("_fns cannot be nil")
    if not isinstance(fns, list):
        raise Exception("_fns must be a list")

    for fn in fns:
        validate_fn(fn)


def validate_fn(fn):
    if not isinstance(fn, dict):
        raise ValueError("Each item in _fns must be a dictionary")
    if "_fn" not in fn:
        raise ValueError("_fn must be set in each function")
    if fn["_fn"] not in VALID_FN_NAMES:
        raise ValueError(f"_fn must be a valid function name, got {fn['_fn']}")

    # Delegate to specific argument validators
    validate_fn_args(fn["_fn"], fn.get("_args"))


def validate_fn_args(function, args):
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


def validate_empty(args):
    if args:
        raise ValueError("_args must be empty")


def validate_string_array(args):
    if not isinstance(args, list) or not all(
        isinstance(elem, str) and elem for elem in args
    ):
        raise ValueError("_args must be a list of non-empty strings")


def validate_string(args):
    if not isinstance(args, str) or not args:
        raise ValueError("_args must be a non-empty string")


def validate_optional_string(args):
    if args is not None and (not isinstance(args, str) or not args):
        raise ValueError("_args must be a non-empty string or None")


def validate_non_zero_int(args):
    if not isinstance(args, int) or args == 0:
        raise ValueError("_args must be a non-zero integer")


def validate_optional_int(args):
    if args is not None and (not isinstance(args, int) or args == 0):
        raise ValueError("_args must be a non-zero integer or None")


def validate_list_string_optional_int(args):
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


def check_context_tbm_validity(context, acceptable_tbms):
    if context and any(
        item.get("key") == "tbm" and item.get("value") not in acceptable_tbms
        for item in context
    ):
        raise ValueError("Invalid tbm parameter value in context")
