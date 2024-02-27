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
from typing import Optional, Dict, Any

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

class BingAsync:
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
    
    async def get_payload_response(self, payload):
        """
        Processes the payload asynchronously, starts a job, polls for its completion, and retrieves the results.

        Args:
            payload (dict): The payload for the request.

        Returns:
            The response from the server after the job is completed.
        """
        # Remove empty or null values from the payload
        payload = {k: v for k, v in payload.items() if v is not None}

        # Start the job and get its ID
        job_id = await self.client.get_job_id(payload)

        # Poll for the job status until completion and return the results
        return await self.client.poll_job_status(job_id)
    
    async def scrape_bing_search(
        self, query: str, opts: Optional[Dict[str, Any]] = None, 
        poll_interval: Optional[int] = None
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

        Returns:
            The response from the server after the job is completed.
        """
        config = Config()

        if poll_interval is not None:
            config.set_polling(poll_interval)

        if poll_interval is not None:
            config.set_polling(poll_interval)
            
        else:
            config.reset_polling()

        # Prepare your JSON payload based on the query and opts
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

        response = await self.get_payload_response(payload)
        return response
    
