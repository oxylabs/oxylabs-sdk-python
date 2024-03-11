from utils.defaults import (
    DEFAULT_LIMIT_SERP,
    set_default_domain,
    set_default_limit,
    set_default_pages,
    set_default_start_page,
    set_default_user_agent,
)
from utils.utils import BaseSearchOpts, BaseUrlOpts, validate_url
from utils.constants import Domain, Source
import utils.utils as utils

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
        utils.check_parsing_instructions_validity(self.parsing_instructions)


class BaiduUrlOpts(BaseUrlOpts):
    """
    Represents the URL options for Baidu.
    """

    def check_parameter_validity(self):
        """
        Checks the validity of BaiduUrlOpts parameters.
        """
        utils.check_user_agent_validity(self.user_agent_type)
        utils.check_parsing_instructions_validity(self.parsing_instructions)

class BaiduBase:
    def _prepare_search_payload(self, query, opts):
        opts = BaiduSearchOpts(**opts if opts is not None else {})

        # Set defaults and check validity
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

        if opts.parsing_instructions:
            payload["parse"] = True
            payload["parsing_instructions"] = opts.parsing_instructions

        return payload

    def _prepare_url_payload(self, url, opts):
        validate_url(url, "baidu")
        opts = BaiduUrlOpts(**opts if opts is not None else {})

        # Set defaults and check validity
        opts.user_agent_type = set_default_user_agent(opts.user_agent_type)
        opts.check_parameter_validity()

        payload = {
            "source": Source.BaiduUrl.value,
            "url": url,
            "user_agent_type": opts.user_agent_type,
            "callback_url": opts.callback_url,
            "parse": opts.parse,
        }

        if opts.parsing_instructions is not None:
            payload["parsing_instructions"] = opts.parsing_instructions
            payload["parse"] = True

        return payload
