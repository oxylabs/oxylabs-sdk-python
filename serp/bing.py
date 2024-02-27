from utils.defaults import (
    DEFAULT_DOMAIN,
    DEFAULT_LIMIT_SERP,
    DEFAULT_PAGES,
    DEFAULT_START_PAGE,
    DEFAULT_USER_AGENT,
    set_default_domain,
    set_default_limit,
    set_default_pages,
    set_default_start_page,
    set_default_user_agent,
)
from utils.utils import BaseSearchOpts, BaseUrlOpts, validate_url, Config
from utils.constants import Render, Domain, UserAgent, Source
import dataclasses
import json


BingSearchAcceptedDomainParameters = [
    Domain.DOMAIN_COM.value,
    Domain.DOMAIN_RU.value,
    Domain.DOMAIN_UA.value,
    Domain.DOMAIN_BY.value,
    Domain.DOMAIN_KZ.value,
    Domain.DOMAIN_TR.value,
]


@dataclasses.dataclass
class BingSearchOpts(BaseSearchOpts):
    """
    Represents the search options for Bing.
    """

    locale: str = None
    geo_location: str = None
    render: Render = None
    parse: bool = False

    def check_parameter_validity(self):
        """
        Checks the validity of BingSearchOpts parameters.
        """
        if self.domain and self.domain not in BingSearchAcceptedDomainParameters:
            raise ValueError(f"Invalid domain parameter: {self.domain}")

        if not UserAgent.is_user_agent_valid(self.user_agent_type):
            raise ValueError(f"Invalid user agent parameter: {self.user_agent_type}")

        if self.render and not Render.is_render_valid(self.render):
            raise ValueError(f"Invalid render parameter: {self.render}")

        if self.limit <= 0 or self.pages <= 0 or self.start_page <= 0:
            raise ValueError(
                "Limit, pages and start_page parameters must be greater than 0"
            )


@dataclasses.dataclass
class BingUrlOpts(BaseUrlOpts):
    """
    Represents the URL options for Bing.
    """

    geo_location: str
    render: Render
    parse: bool

    def check_parameter_validity(self):
        """
        Checks the validity of BingUrlOpts parameters.
        """
        if not UserAgent.is_user_agent_valid(self.user_agent_type):
            raise ValueError(f"Invalid user agent parameter: {self.user_agent_type}")

        if self.render and not Render.is_render_valid(self.render):
            raise ValueError(f"Invalid render parameter: {self.render}")


class Bing:
    def __init__(self, client):
        """
        Initializes a new instance of the Bing class.

        Args:
            client: The client object used for making API requests.
        """
        self.client = client

    def set_and_validate_opts(self, opts, defaults):
        if opts is None:
            opts = defaults
        elif isinstance(opts, dict):
            defaults.update(opts)
            opts = defaults
        else:
            raise ValueError(
                f"opts must be either None or a dictionary, not {type(opts).__name__}"
            )

        return opts

    def get_payload_response(self, payload):
        # remove empty or null values
        payload = {k: v for k, v in payload.items() if v is not None}

        # Convert payload to JSON
        json_payload = json.dumps(payload)

        # Make the request
        http_resp = self.client.req(json_payload, "POST")

        return http_resp

    def scrape_bing_search(self, query, opts=None, timeout=None):

        if timeout is not None:
            config = Config()
            config.set_timeout(timeout)

        defaults = {
            "domain": DEFAULT_DOMAIN,
            "start_page": DEFAULT_START_PAGE,
            "pages": DEFAULT_PAGES,
            "limit": DEFAULT_LIMIT_SERP,
            "user_agent_type": DEFAULT_USER_AGENT,
            "callback_url": None,
            "locale": None,
            "geo_location": None,
            "render": None,
            "parse": None,
        }

        opts = self.set_and_validate_opts(opts, defaults)

        opts = BingSearchOpts(**opts)

        # Set defaults
        opts.domain = set_default_domain(opts.domain)
        opts.start_page = set_default_start_page(opts.start_page)
        opts.limit = set_default_limit(opts.limit, DEFAULT_LIMIT_SERP)
        opts.pages = set_default_pages(opts.pages)
        opts.user_agent_type = set_default_user_agent(opts.user_agent_type)

        # Check validity of parameters
        opts.check_parameter_validity()

        # Prepare payload
        payload = {
            "source": Source.BingSearch.value,
            "domain": opts.domain,
            "query": query,
            "start_page": opts.start_page,
            "pages": opts.pages,
            "limit": opts.limit,
            "locale": opts.locale,
            "geo_location": opts.geo_location,
            "user_agent_type": opts.user_agent_type,
            "callback_url": opts.callback_url,
            "render": opts.render,
            "parse": opts.parse,
        }

        # Add parsing instructions to the payload if provided
        if opts.parse_instructions is not None:
            payload["parsing_instructions"] = opts.parse_instructions

        resp = self.get_payload_response(payload)

        return resp

    def scrape_bing_url(self, url, opts=None, timeout=None):

        if timeout is not None:
            config = Config()
            config.set_timeout(timeout)

        # Check validity of url
        validate_url(url, "bing")

        defaults = {
            "user_agent_type": DEFAULT_USER_AGENT,
            "callback_url": None,
            "parse_instructions": None,
            "geo_location": None,
            "render": None,
            "parse": False,
        }

        opts = self.set_and_validate_opts(opts, defaults)

        opts = BingUrlOpts(**opts)

        # Set defaults
        opts.user_agent_type = set_default_user_agent(opts.user_agent_type)

        # Check validity of parameters
        opts.check_parameter_validity()

        # Prepare payload
        payload = {
            "source": Source.BingUrl.value,
            "url": url,
            "user_agent_type": opts.user_agent_type,
            "geo_location": opts.geo_location,
            "render": opts.render,
            "callback_url": opts.callback_url,
            "parse": opts.parse,
        }

        # Add parsing instructions to the payload if provided
        if opts.parse_instructions is not None:
            payload["parsing_instructions"] = opts.parse_instructions

        resp = self.get_payload_response(payload)

        return resp
