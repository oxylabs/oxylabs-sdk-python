from utils.constants import UserAgent, Render, FnName
from urllib.parse import urlparse
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
        parse=False,
    ):
        self.domain = domain
        self.start_page = start_page
        self.pages = pages
        self.limit = limit
        self.user_agent_type = user_agent_type
        self.callback_url = callback_url
        self.parsing_instructions = parsing_instructions
        self.parse = parse


class BaseUrlOpts:
    def __init__(
        self,
        user_agent_type=DEFAULT_USER_AGENT,
        callback_url=None,
        parsing_instructions=None,
        parse=False,
    ):
        self.user_agent_type = user_agent_type
        self.callback_url = callback_url
        self.parsing_instructions = parsing_instructions
        self.parse = parse


class BaseGoogleOpts:
    def __init__(
        self,
        geo_location=None,
        user_agent_type=DEFAULT_USER_AGENT,
        render=None,
        callback_url=None,
        parsing_instructions=None,
        parse=False,
        context=None,
    ):
        self.geo_location = geo_location
        self.user_agent_type = user_agent_type
        self.render = render
        self.callback_url = callback_url
        self.parsing_instructions = parsing_instructions
        self.parse = parse
        self.context = context


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
    if fn["_fn"] not in [e.value for e in FnName]:
        raise ValueError(f"_fn must be a valid function name, got {fn['_fn']}")

    # Delegate to specific argument validators
    validate_fn_args(fn["_fn"], fn.get("_args"))

def validate_fn_args(fn_name, args):
    # Map function name to validator function
    validators = {
        FnName.ElementText.value: validate_empty,
        FnName.Length.value: validate_empty,
        FnName.ConvertToFloat.value: validate_empty,
        FnName.ConvertToInt.value: validate_empty,
        FnName.ConvertToStr.value: validate_empty,
        FnName.Max.value: validate_empty,
        FnName.Min.value: validate_empty,
        FnName.Product.value: validate_empty,
        FnName.Xpath.value: validate_string_array,
        FnName.XpathOne.value: validate_string_array,
        FnName.Css.value: validate_string_array,
        FnName.CssOne.value: validate_string_array,
        FnName.AmountFromString.value: validate_string,
        FnName.AmountRangeFromString.value: validate_string,
        FnName.RegexFindAll.value: validate_string,
        FnName.Join.value: validate_optional_string,
        FnName.RegexSearch.value: validate_list_string_optional_int,
        FnName.RegexSubstring.value: validate_list_string_optional_int,
        FnName.SelectNth.value: validate_non_zero_int,
        FnName.Average.value: validate_optional_int,
    }

    if fn_name not in validators:
        raise ValueError(f"No validator for function name: {fn_name}")

    # Call the appropriate validator
    validator = validators[fn_name]
    validator(args)
    
def validate_empty(args):
    if args:
        raise ValueError("_args must be empty")

def validate_string_array(args):
    if not isinstance(args, list) or not all(isinstance(elem, str) and elem for elem in args):
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
    if not isinstance(args, list) or len(args) < 1 or not isinstance(args[0], str) or not args[0]:
        raise ValueError("_args first argument must be a non-empty string")
    if len(args) > 1 and (not isinstance(args[1], int) or args[1] == 0):
        raise ValueError("_args second argument must be a non-zero integer when present")
