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
from utils.utils import BaseSearchOpts, BaseUrlOpts, validate_url
from utils.constants import Domain, Source
import utils.utils as utils
from typing import Optional, Any

BingSearchAcceptedDomainParameters = [
    Domain.DOMAIN_COM.value,
    Domain.DOMAIN_RU.value,
    Domain.DOMAIN_UA.value,
    Domain.DOMAIN_BY.value,
    Domain.DOMAIN_KZ.value,
    Domain.DOMAIN_TR.value,
]


class BingSearchOpts(BaseSearchOpts):
    """
    Represents the search options for Bing.
    """

    def __init__(
        self,
        locale: Optional[str] = None,
        geo_location: Optional[str] = None,
        render: Optional[bool] = None,
        parse: Optional[bool] = None,
        **kwargs: Any,
    ) -> None:
        """
        Initialize a new instance of the BingBase class.

        Args:
            locale (str): The locale to be used for the search results. Defaults to None.
            geo_location (str): The geo location to be used for the search results. Defaults to None.
            render (bool): Whether to render JavaScript on the page. Defaults to None.
            parse (bool): Whether to parse the search results. Defaults to None.
            **kwargs: Additional keyword arguments.

        Returns:
            None
        """
        super().__init__(
            **kwargs,
        )
        self.locale = locale
        self.geo_location = geo_location
        self.render = render
        self.parse = parse

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
        utils.check_parsing_instructions_validity(self.parsing_instructions)


class BingUrlOpts(BaseUrlOpts):
    """
    Represents the URL options for Bing.
    """

    def __init__(
        self,
        geo_location: Optional[str] = None,
        render: Optional[bool] = None,
        parse: Optional[bool] = None,
        **kwargs: Any,
    ) -> None:
        """
        Initializes a new instance of the BingBase class.

        Args:
            geo_location (str): The geographic location for the search.
            render (bool): Indicates whether to render JavaScript on the page.
            parse (bool): Indicates whether to parse the search results.
            **kwargs: Additional keyword arguments.

        """
        super().__init__(**kwargs)
        self.geo_location = geo_location
        self.render = render
        self.parse = parse

    def check_parameter_validity(self):
        """
        Checks the validity of BingUrlOpts parameters.
        """
        utils.check_user_agent_validity(self.user_agent_type)
        utils.check_render_validity(self.render)
        utils.check_parsing_instructions_validity(self.parsing_instructions)


class BingBase:
    def _prepare_search_payload(self, query: str, opts: Optional[dict]) -> dict:
        """
        Prepares the search payload for the Bing search.

        Args:
            query (str): The search query.
            opts (dict): The search options.

        Returns:
            dict: The prepared search payload.

        """
        opts = BingSearchOpts(**opts if opts is not None else {})

        # Set defaults and check validity
        opts.domain = set_default_domain(opts.domain)
        opts.start_page = set_default_start_page(opts.start_page)
        opts.limit = set_default_limit(opts.limit, DEFAULT_LIMIT_SERP)
        opts.pages = set_default_pages(opts.pages)
        opts.user_agent_type = set_default_user_agent(opts.user_agent_type)
        opts.check_parameter_validity()

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

        if opts.parsing_instructions is not None:
            payload["parsing_instructions"] = opts.parsing_instructions
            payload["parse"] = True

        return payload

    def _prepare_url_payload(self, url: str, opts: Optional[dict]) -> dict:
        """
        Prepares the payload for a Bing URL request.

        Args:
            url (str): The URL to be queried.
            opts (dict): Optional parameters for the request.

        Returns:
            dict: The prepared payload for the request.
        """
        validate_url(url, "bing")
        opts = BingUrlOpts(**opts if opts is not None else {})

        # Set defaults and check validity
        opts.user_agent_type = set_default_user_agent(opts.user_agent_type)
        opts.check_parameter_validity()

        payload = {
            "source": Source.BingUrl.value,
            "url": url,
            "user_agent_type": opts.user_agent_type,
            "geo_location": opts.geo_location,
            "render": opts.render,
            "callback_url": opts.callback_url,
            "parse": opts.parse,
        }

        if opts.parsing_instructions is not None:
            payload["parsing_instructions"] = opts.parsing_instructions
            payload["parse"] = True

        return payload
