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
from utils.constants import Render, Domain, UserAgent, Source, Locale
import utils.utils as utils
import dataclasses
import json


YandexSearchAcceptedDomainParameters = [
    Domain.DOMAIN_COM.value,
    Domain.DOMAIN_RU.value,
    Domain.DOMAIN_UA.value,
    Domain.DOMAIN_BY.value,
    Domain.DOMAIN_KZ.value,
    Domain.DOMAIN_TR.value,
]

YandexSearchAcceptedLocaleParameters = [
    Locale.LOCALE_EN.value,
    Locale.LOCALE_RU.value,
    Locale.LOCALE_BY.value,
    Locale.LOCALE_DE.value,
    Locale.LOCALE_FR.value,
    Locale.LOCALE_ID.value,
    Locale.LOCALE_KK.value,
    Locale.LOCALE_TT.value,
    Locale.LOCALE_TR.value,
    Locale.LOCALE_UK.value,
]


@dataclasses.dataclass
class YandexSearchOpts(BaseSearchOpts):
    """
    Represents the search options for Yandex.
    """

    locale: str = None
    geo_location: str = None

    def check_parameter_validity(self):
        """
        Checks the validity of YandexSearchOpts parameters.
        """
        utils.check_user_agent_validity(self.user_agent_type)
        utils.check_domain_validity(self.domain, YandexSearchAcceptedDomainParameters)
        utils.check_locale_validity(self.locale, YandexSearchAcceptedLocaleParameters)
        utils.check_limit_validity(self.limit)
        utils.check_pages_validity(self.pages)
        utils.check_start_page_validity(self.start_page)


@dataclasses.dataclass
class YandexUrlOpts(BaseUrlOpts):
    """
    Represents the URL options for Yandex.
    """

    render: Render = None

    def check_parameter_validity(self):
        """
        Checks the validity of YandexUrlOpts parameters.
        """
        utils.check_render_validity(self.render)


class Yandex:
    def __init__(self, client):

        self.client = client

    def set_or_update_opts(self, opts, defaults):
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

    def scrape_yandex_search(self, query, opts=None, timeout=None):
        """
        Scrapes the search results from Yandex.

        Args:
            query (str): The search query.
            opts (YandexSearchOpts): The search options.

        Returns:
            dict: The search results.
        """
        config = Config()

        if timeout is not None:
            config.set_timeout(timeout)

        else:
            config.reset_timeout()

        defaults = {
            "domain": DEFAULT_DOMAIN,
            "start_page": DEFAULT_START_PAGE,
            "pages": DEFAULT_PAGES,
            "limit": DEFAULT_LIMIT_SERP,
            "locale": None,
            "geo_location": None,
            "user_agent_type": DEFAULT_USER_AGENT,
            "callback_url": None,
            "parse_instructions": None,
            "parse": False,
            "poll_interval": 0,
        }

        opts = self.set_or_update_opts(opts, defaults)

        opts = YandexSearchOpts(**opts)

        # Set defaults
        opts.domain = set_default_domain(opts.domain)
        opts.start_page = set_default_start_page(opts.start_page)
        opts.pages = set_default_pages(opts.pages)
        opts.limit = set_default_limit(opts.limit, DEFAULT_LIMIT_SERP)
        opts.user_agent_type = set_default_user_agent(opts.user_agent_type)

        opts.check_parameter_validity()

        payload = {
            "source": Source.YandexSearch.value,
            "domain": opts.domain,
            "query": query,
            "start_page": opts.start_page,
            "pages": opts.pages,
            "limit": opts.limit,
            "locale": opts.locale,
            "geo_location": opts.geo_location,
            "user_agent_type": opts.user_agent_type,
            "callback_url": opts.callback_url,
            "parse": opts.parse,
        }
        if opts.parse_instructions is not None:
            payload["parsing_instructions"] = opts.parse_instructions
            payload["parse"] = True

        response = self.get_payload_response(payload)

        return response

    def scrape_yandex_url(self, url, opts=None, timeout=None):
        config = Config()

        if timeout is not None:
            config.set_timeout(timeout)

        else:
            config.reset_timeout()

        # Check validity of url
        validate_url(url, "yandex")

        defaults = {
            "user_agent_type": DEFAULT_USER_AGENT,
            "render": None,
            "callback_url": None,
            "parse_instructions": None,
            "poll_interval": None,
            "parse": False,
        }

        opts = self.set_or_update_opts(opts, defaults)

        opts = YandexUrlOpts(**opts)

        # Set defaults
        opts.user_agent_type = set_default_user_agent(opts.user_agent_type)

        # Check validity of parameters
        opts.check_parameter_validity()

        # Prepare payload
        payload = {
            "source": Source.YandexUrl.value,
            "url": url,
            "user_agent_type": opts.user_agent_type,
            "render": opts.render,
            "callback_url": opts.callback_url,
            "parse": opts.parse,
        }

        # Add parsing instructions to the payload if provided
        if opts.parse_instructions is not None:
            payload["parsing_instructions"] = opts.parse_instructions
            payload["parse"] = True

        resp = self.get_payload_response(payload)

        return resp
