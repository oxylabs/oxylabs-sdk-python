from utils.defaults import (
    DEFAULT_LIMIT_SERP,
    set_default_domain,
    set_default_limit,
    set_default_pages,
    set_default_start_page,
    set_default_user_agent,
)
from utils.utils import BaseSearchOpts, BaseUrlOpts, validate_url
from utils.constants import Render, Domain, Source, Locale
import utils.utils as utils
import dataclasses
import json
from typing import Optional, Dict, Any


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

    def get_payload_response(self, payload):
        # remove empty or null values
        payload = {k: v for k, v in payload.items() if v is not None}

        # Convert payload to JSON
        json_payload = json.dumps(payload)

        # Make the request
        http_resp = self.client.req(json_payload, "POST")

        return http_resp

    def scrape_yandex_search(
        self, query: str, opts: Optional[Dict[str, Any]] = None, timeout: int = None
    ) -> Dict[str, Any]:
        """
        Scrapes the search results from Yandex.

        Args:
            query (str): The search query.
            opts (dict, optional): Configuration options for the search. Defaults to:

                {
                    "domain": com,
                    "start_page": 1,
                    "pages": 1,
                    "limit": 10,
                    "user_agent_type": desktop,
                    "callback_url": None,
                    "locale": None,
                    "geo_location": None,
                    "parse": None,
                }
                This parameter allows customization of the search request.

            timeout (int, optional): The interval in seconds for the request to time out if no response is returned. Defaults to None.

        Returns:

            dict: The response from the server after the job is completed.
        """

        opts = YandexSearchOpts(**opts if opts is not None else {})

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

        resp = self.client.send_post_request_with_payload(payload, timeout)

        return resp

    def scrape_yandex_url(self, url: str, opts: Optional[Dict[str, Any]] = None, timeout: int = None) -> Dict[str, Any]:
        """
        Scrapes Yandex search results for a given URL.
        
        Args:
            url (str): The URL to be scraped.
            opts (YandexUrlOpts, optional): Configuration options for the search. Defaults to:
                {
                    "user_agent_type": DEFAULT_USER_AGENT,
                    "callback_url": None,
                    "parse_instructions": None,
                }
                This parameter allows customization of the search request.
            timeout (int | None, optional): The interval in seconds for the request to time out if no response is returned. Defaults to None.
            
        Returns:
            dict: The response from the server after the job is completed.
        """
        

        # Check validity of url
        validate_url(url, "yandex")

        opts = YandexUrlOpts(**opts if opts is not None else {})

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

        resp = self.client.send_post_request_with_payload(payload, timeout)

        return resp
