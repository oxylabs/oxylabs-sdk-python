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
import utils.utils as utils

import dataclasses
import json


BaiduSearchAcceptedDomainParameters = [
    Domain.DOMAIN_COM.value,
    Domain.DOMAIN_CN.value,
]


@dataclasses.dataclass
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


@dataclasses.dataclass
class BaiduUrlOpts(BaseUrlOpts):
    """
    Represents the URL options for Baidu.
    """

    def check_parameter_validity(self):
        """
        Checks the validity of BaiduUrlOpts parameters.
        """
        utils.check_user_agent_validity(self.user_agent_type)



@dataclasses.dataclass
class Baidu:
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

    def scrape_baidu_search(self, query, opts=None, timeout=None):
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
            "user_agent_type": DEFAULT_USER_AGENT,
            "callback_url": None,
            "parse_instructions": None,
            "poll_interval": None,
            "parse": False,
        }
        
        opts = self.set_or_update_opts(opts, defaults)
        
        opts = BaiduSearchOpts(**opts)
        
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
            "user_agent": opts.user_agent_type,
            "callback_url": opts.callback_url,
        }
        
        if opts.parse_instructions:
            payload["parse"] = True
            payload["parse_instructions"] = opts.parse_instructions
        
        
        response = self.get_payload_response(payload)
        
        return response
    
    
    def scrape_baidu_url(self, url, opts=None, timeout=None):
        config = Config()

        if timeout is not None:
            config.set_timeout(timeout)
            
        else:
            config.reset_timeout()

            
        validate_url(url, "baidu")
            
        defaults = {
            "user_agent_type": DEFAULT_USER_AGENT,
            "callback_url": None,
            "parse_instructions": None,
            "poll_interval": None,
        }
        
        opts = self.set_or_update_opts(opts, defaults)
        
        opts = BaiduUrlOpts(**opts)
        
        opts.user_agent_type = set_default_user_agent(opts.user_agent_type)
        
        opts.check_parameter_validity()
        
        payload = {
            "source": Source.BaiduUrl.value,
            "url": url,
            "user_agent": opts.user_agent_type,
            "callback_url": opts.callback_url,
        }
        
        if opts.parse_instructions:
            payload["parse"] = True
            payload["parse_instructions"] = opts.parse_instructions
        
        response = self.get_payload_response(payload)
        
        return response
        

        
        
            
