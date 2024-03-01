from utils.defaults import (
    DEFAULT_LIMIT_SERP,
    DEFAULT_TIMEOUT,
    set_default_domain,
    set_default_limit,
    set_default_pages,
    set_default_start_page,
    set_default_user_agent,
)
from utils.utils import BaseSearchOpts, BaseUrlOpts, validate_url
from utils.constants import Domain, Source
import utils.utils as utils
from typing import Optional, Dict, Any


BaiduSearchAcceptedDomainParameters = [
    Domain.DOMAIN_COM.value,
    Domain.DOMAIN_CN.value,
]


class BaiduSearchOpts(BaseSearchOpts):
    """
    Represents the search options for Baidu.
    """

    def check_parameter_validity(self):
        """
        Checks the validity of BaiduSearchOpts parameters.
        """
        utils.check_domain_validity(self.domain, BaiduSearchAcceptedDomainParameters)
        utils.check_user_agent_validity(self.user_agent_type)
        utils.check_limit_validity(self.limit)
        utils.check_pages_validity(self.pages)
        utils.check_start_page_validity(self.start_page)


class BaiduUrlOpts(BaseUrlOpts):
    """
    Represents the URL options for Baidu.
    """

    def check_parameter_validity(self):
        """
        Checks the validity of BaiduUrlOpts parameters.
        """
        utils.check_user_agent_validity(self.user_agent_type)


class Baidu:
    def __init__(self, client):
        self.client = client

    def scrape_baidu_search(
        self, query: str, opts: Optional[Dict[str, Any]] = None, timeout: int = None
    ) -> Dict[str, Any]:
        """
        Scrapes Baidu search results for a given query.

        Args:
            query (str): The search query.
            opts (BaiduSearchOpts, optional): Configuration options for the search. Defaults to:
                {
                    "domain": com,
                    "start_page": 1,
                    "pages": 1,
                    "limit": 10,
                    "user_agent_type": desktop,
                    "callback_url": None,
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

        opts = BaiduSearchOpts(**opts if opts is not None else {})

        # Set defaults
        opts.domain = set_default_domain(opts.domain)
        opts.start_page = set_default_start_page(opts.start_page)
        opts.pages = set_default_pages(opts.pages)
        opts.limit = set_default_limit(opts.limit, DEFAULT_LIMIT_SERP)
        opts.user_agent_type = set_default_user_agent(opts.user_agent_type)

        opts.check_parameter_validity()

        payload = {
            "source": Source.BaiduSearch.value,
            "domain": opts.domain,
            "query": query,
            "start_page": opts.start_page,
            "pages": opts.pages,
            "limit": opts.limit,
            "user_agent_type": opts.user_agent_type,
            "callback_url": opts.callback_url,
        }

        if opts.parse_instructions:
            payload["parse"] = True
            payload["parse_instructions"] = opts.parse_instructions

        resp = self.client.get_resp(payload, config)

        return resp

    def scrape_baidu_url(
        self, url: str, opts: Optional[Dict[str, Any]] = None, timeout: int = None
    ) -> Dict[str, Any]:
        """
        Scrapes Baidu search results for a given URL.

        Args:
            url (str): The URL to be scraped.
            opts (BaiduUrlOpts, optional): Configuration options for the search. Defaults to:
                {
                    "user_agent_type": desktop,
                    "callback_url": None,
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

        validate_url(url, "baidu")

        opts = BaiduUrlOpts(**opts if opts is not None else {})

        opts.user_agent_type = set_default_user_agent(opts.user_agent_type)

        opts.check_parameter_validity()

        payload = {
            "source": Source.BaiduUrl.value,
            "url": url,
            "user_agent_type": opts.user_agent_type,
            "callback_url": opts.callback_url,
        }

        if opts.parse_instructions:
            payload["parse"] = True
            payload["parse_instructions"] = opts.parse_instructions

        resp = self.client.get_resp(payload, config)

        return resp
