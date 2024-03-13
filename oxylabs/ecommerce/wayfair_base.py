from utils.defaults import (
    DEFAULT_DOMAIN,
    DEFAULT_LIMIT_ECOMMERCE,
    DEFAULT_PAGES,
    DEFAULT_START_PAGE,
    DEFAULT_USER_AGENT,
    set_default_domain,
    set_default_limit,
    set_default_pages,
    set_default_start_page,
    set_default_user_agent,
)
from utils.utils import validate_url
from utils.types import Domain, Source
import utils.utils as utils


class WayfairSearchOpts:
    """
    Represents the search options for Wayfair.
    """

    def __init__(
        self,
        start_page=DEFAULT_START_PAGE,
        pages=DEFAULT_PAGES,
        limit=DEFAULT_LIMIT_ECOMMERCE,
        user_agent_type=DEFAULT_USER_AGENT,
        callback_url=None,
        parsing_instructions=None,
    ):
        self.start_page = start_page
        self.pages = pages
        self.limit = limit
        self.user_agent_type = user_agent_type
        self.callback_url = callback_url
        self.parsing_instructions = parsing_instructions

    def check_parameter_validity(self):
        """
        Checks the validity of WayfairSearchOpts parameters.
        """
        utils.check_user_agent_validity(self.user_agent_type)
        utils.check_limit_validity_ecom(self.limit)
        utils.check_pages_validity(self.pages)
        utils.check_start_page_validity(self.start_page)


class WayfairUrlOpts:
    """
    Represents the URL options for Wayfair.
    """

    def __init__(
        self,
        user_agent_type=DEFAULT_USER_AGENT,
        callback_url=None
    ):
        self.user_agent_type = user_agent_type
        self.callback_url = callback_url

    def check_parameter_validity(self):
        """
        Checks the validity of WayfairUrlOpts parameters.
        """
        utils.check_user_agent_validity(self.user_agent_type)


class WayfairBase:
    def _prepare_search_payload(self, query, opts):
        opts = WayfairSearchOpts(**opts if opts is not None else {})

        # Set defaults and check validity
        opts.start_page = set_default_start_page(opts.start_page)
        opts.limit = set_default_limit(opts.limit, DEFAULT_LIMIT_ECOMMERCE)
        opts.pages = set_default_pages(opts.pages)
        opts.user_agent_type = set_default_user_agent(opts.user_agent_type)
        
        opts.check_parameter_validity()

        payload = {
            "source": Source.WayfairSearch.value,
            "query": query,
            "start_page": opts.start_page,
            "pages": opts.pages,
            "limit": opts.limit,
            "user_agent_type": opts.user_agent_type,
            "callback_url": opts.callback_url,
        }

        if opts.parsing_instructions is not None:
            payload["parsing_instructions"] = opts.parsing_instructions
            payload["parse"] = True

        return payload

    def _prepare_url_payload(self, url, opts):
        validate_url(url, "wayfair")
        opts = WayfairUrlOpts(**opts if opts is not None else {})

        # Set defaults and check validity
        opts.user_agent_type = set_default_user_agent(opts.user_agent_type)
        opts.check_parameter_validity()

        payload = {
            "source": Source.Wayfair.value,
            "url": url,
            "user_agent_type": opts.user_agent_type,
            "callback_url": opts.callback_url,
        }
        
        return payload
