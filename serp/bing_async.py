from utils.defaults import (
    DEFAULT_DOMAIN,
    DEFAULT_LIMIT_SERP,
    DEFAULT_PAGES,
    DEFAULT_START_PAGE,
    DEFAULT_USER_AGENT,
    DEFAULT_POLL_INTERVAL,
    DEFAULT_TIMEOUT,
    set_default_domain,
    set_default_limit,
    set_default_pages,
    set_default_start_page,
    set_default_user_agent,
)
from utils.utils import BaseSearchOpts
from utils.constants import Domain, Source
import utils.utils as utils
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

class BingAsync:
    def __init__(self, client):
        """
        Initializes a new instance of the Bing class.

        Args:
            client: The client object used for making API requests.
        """
        self.client = client
    
    async def scrape_bing_search(
        self, query: str, opts: Optional[Dict[str, Any]] = None, 
        poll_interval: Optional[int] = None, timeout: Optional[int] = None
    ) -> Dict[str, Any]:

        """
        Asynchronously scrapes Bing search results for a given query.

        Args:
            query (str): The search query.
            opts (dict, optional): Configuration options for the search. Defaults to:
                {
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
                This parameter allows customization of the search request.
            poll_interval (int | None, optional): The interval in seconds between status checks for the asynchronous job. Defaults to None.
            timeout (int | None, optional): The interval in seconds for the request to time out if no response is returned. Defaults to None.

        Returns:
            The response from the server after the job is completed.
        """
        config = {
            'timeout': timeout if timeout is not None else DEFAULT_TIMEOUT,
            'poll_interval': poll_interval if poll_interval is not None else DEFAULT_POLL_INTERVAL
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

        resp = await self.client.get_resp(payload, config)
        
        return resp
    
