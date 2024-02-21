from utils.defaults import DEFAULT_LIMIT_SERP, set_default_domain, set_default_limit, set_default_pages, set_default_start_page, set_default_user_agent
from utils.utils import BaseSearchOpts, BaseUrlOpts
from utils.constants import Render, Domain, UserAgent, Source
from serp.serp import SerpClient
from serp.response import Resp
import dataclasses
import json
from typing import Optional


BingSearchAcceptedDomainParameters = [
    Domain.DOMAIN_COM,
    Domain.DOMAIN_RU,
    Domain.DOMAIN_UA,
    Domain.DOMAIN_BY,
    Domain.DOMAIN_KZ,
    Domain.DOMAIN_TR,
]

@dataclasses.dataclass
class BingSearchOpts(BaseSearchOpts):
    """
    Represents the search options for Bing.
    """
    locale: str  
    geo_location: str  
    render: Render  
    parse: bool  

    def check_parameter_validity(self):
        """
        Checks the validity of BingSearchOpts parameters.
        """
        if self.domain and self.domain not in BingSearchAcceptedDomainParameters:
            raise ValueError(f"Invalid domain parameter: {self.domain}")

        if not UserAgent.is_user_agent_valid(self.user_agent):
            raise ValueError(f"Invalid user agent parameter: {self.user_agent}")

        if self.render and not Render.is_render_valid(self.render):
            raise ValueError(f"Invalid render parameter: {self.render}")

        if self.limit <= 0 or self.pages <= 0 or self.start_page <= 0:
            raise ValueError("Limit, pages and start_page parameters must be greater than 0")

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
        if not UserAgent.is_user_agent_valid(self.user_agent):
            raise ValueError(f"Invalid user agent parameter: {self.user_agent}")

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

    def scrape_bing_search(self, query: str, opts: Optional[BingSearchOpts] = None):
        if opts is None:
            opts = BingSearchOpts(
                domain=None,
                start_page=None,
                pages=None,
                limit=None,
                user_agent=UserAgent.UA_DESKTOP,
                callback_url=None,
                parse_instructions=None,
                poll_interval=None,
                locale=None, 
                geo_location=None, 
                render=None, 
                parse=False 
            )

        # Set defaults
        opts.domain = set_default_domain(opts.domain)
        opts.start_page = set_default_start_page(opts.start_page)
        opts.limit = set_default_limit(opts.limit, DEFAULT_LIMIT_SERP)
        opts.pages = set_default_pages(opts.pages)
        opts.user_agent = set_default_user_agent(opts.user_agent)

        # Check validity of parameters
        opts.check_parameter_validity()

        # Prepare payload
        payload = {
            "source": Source.BingSearch.value,
            "domain": opts.domain.value,
            "query": query,
            "start_page": opts.start_page,
            "pages": opts.pages,
            "limit": opts.limit,
            "locale": opts.locale,
            "geo_location": opts.geo_location,
            "user_agent_type": opts.user_agent,
            "callback_url": opts.callback_url,
            "render": opts.render,
            "parse": opts.parse,
        }

        # Add custom parsing instructions to the payload if provided
        if opts.parse_instructions is not None:
            payload["parsing_instructions"] = opts.parse_instructions

        # Convert payload to JSON
        json_payload = json.dumps(payload)
        # Make the request
        http_resp = self.client.req(json_payload, "POST")

        # Process the response
        resp = Resp.from_http_resp(http_resp, opts.parse, False)

        return resp


    def scrape_bing_url(self):
        """
        Scrapes URLs from Bing.

        This method implements the functionality to scrape URLs from Bing.
        """
        pass  # Functionality goes here