from utils.defaults import (
    DEFAULT_LIMIT_SERP,
    DEFAULT_DOMAIN,
    DEFAULT_START_PAGE,
    DEFAULT_USER_AGENT,
    DEFAULT_PAGES,
    DEFAULT_TIMEOUT,
    set_default_domain,
    set_default_limit,
    set_default_pages,
    set_default_start_page,
    set_default_user_agent,
)
from utils.utils import BaseSearchOpts, BaseUrlOpts, validate_url
import utils.utils as utils
from utils.constants import Domain, Source
from typing import Optional, Dict, Any


BingSearchAcceptedDomainParameters = [
    Domain.DOMAIN_COM.value,
    Domain.DOMAIN_RU.value,
    Domain.DOMAIN_UA.value,
    Domain.DOMAIN_BY.value,
    Domain.DOMAIN_KZ.value,
    Domain.DOMAIN_TR.value,
]


class BingSearchOpts(BaseSearchOpts):

    def __init__(
        self,
        domain=DEFAULT_DOMAIN,
        start_page=DEFAULT_START_PAGE,
        pages=DEFAULT_PAGES,
        limit=DEFAULT_LIMIT_SERP,
        user_agent_type=DEFAULT_USER_AGENT,
        callback_url=None,
        parse_instructions=None,
        parse=False,
        locale=None,
        geo_location=None,
        render=None,
    ):
        super().__init__(
            domain,
            start_page,
            pages,
            limit,
            user_agent_type,
            callback_url,
            parse_instructions,
            parse,
        )
        self.locale = locale
        self.geo_location = geo_location
        self.render = render

    def check_parameter_validity(self):
        """
        Checks the validity of BingSearchOpts parameters.
        """
        utils.check_domain_validity(self.domain, BingSearchAcceptedDomainParameters)
        utils.check_user_agent_validity(self.user_agent_type)
        utils.check_render_validity(self.render)
        utils.check_limit_validity(self.limit)
        utils.check_pages_validity(self.pages)
        utils.check_start_page_validity(self.start_page)


class BingUrlOpts(BaseUrlOpts):
    def __init__(
        self,
        user_agent_type=DEFAULT_USER_AGENT,
        callback_url=None,
        parse_instructions=None,
        parse=False,
        geo_location=None,
        render=None,
    ):
        super().__init__(user_agent_type, callback_url, parse_instructions, parse)
        self.geo_location = geo_location
        self.render = render

    def check_parameter_validity(self):
        """
        Checks the validity of BingUrlOpts parameters.
        """
        utils.check_user_agent_validity(self.user_agent_type)

        utils.check_render_validity(self.render)


class Bing:
    def __init__(self, client):
        """
        Initializes a new instance of the Bing class.

        Args:
            client: The client object used for making API requests.
        """
        self.client = client

    def scrape_bing_search(
        self, query: str, opts: Optional[Dict[str, Any]] = None, timeout: int = None
    ) -> Dict[str, Any]:
        """
        Scrapes Bing search results for a given query.

        Args:
            query (str): The search query.
            opts (dict, optional): Configuration options for the search. Defaults to None. Options can include:
                {
                    "domain": "com",
                    "start_page": 1,
                    "pages": 1,
                    "limit": 10,
                    "user_agent_type": "desktop",
                    "callback_url": None,
                    "locale": None,
                    "geo_location": None, (City,Region,Country, for example Harrisburg,Arkansas,United States)
                    "render": None,
                    "parse": None,
                    "parse_instructions": None,
                }
                This parameter allows customization of the search request.
            timeout (int | None, optional): The interval in seconds for the request to time out if no response is returned. Defaults to None.

        Returns:
            dict: The response from the server after the job is completed.
        """
        config = {
            "timeout": timeout if timeout is not None else DEFAULT_TIMEOUT,
        }

        opts = BingSearchOpts(**opts if opts is not None else {})

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
            payload["parse"] = True

        resp = self.client.send_post_request_with_payload(payload, config)

        return resp

    def scrape_bing_url(
        self, url: str, opts: Optional[Dict[str, Any]] = None, timeout: int = None
    ) -> Dict[str, Any]:
        """
        Scrapes Bing search results for a given URL.

        Args:
            url (str): The URL to be scraped.
            opts (BingUrlOpts, optional): Configuration options for the search. Defaults to:
                {
                    "user_agent_type": desktop,
                    "geo_location": None,
                    "callback_url": None,
                    "render": None,
                    "parse_instructions": None,
                }
                This parameter allows customization of the search request.
            timeout (int | None, optional): The interval in seconds for the request to time out if no response is returned. Defaults to None.

        Returns:
            dict: The response from the server after the job is completed.
        """
        config = {
            "timeout": timeout if timeout is not None else DEFAULT_TIMEOUT,
        }
        # Check validity of url
        validate_url(url, "bing")

        opts = BingUrlOpts(**opts if opts is not None else {})

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
            payload["parse"] = True

        resp = self.client.send_post_request_with_payload(payload, config)

        return resp
