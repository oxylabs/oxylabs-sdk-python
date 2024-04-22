from oxylabs.utils.constants import domain
from oxylabs.utils.defaults import (
    DEFAULT_LIMIT_SERP,
    set_default_domain,
    set_default_limit,
    set_default_pages,
    set_default_start_page,
    set_default_user_agent_type,
)
from oxylabs.utils.utils import BaseSearchOpts, BaseUrlOpts, validate_url
from oxylabs.utils.constants import source
import oxylabs.utils.utils as utils
from typing import Optional, Dict, Any

BaiduSearchAcceptedDomainParameters = [domain.COM, domain.CN]


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
    def _prepare_search_payload(
        self, query: str, user_opts: Optional[dict] = None
    ) -> dict:
        """
        Prepares the search payload for Baidu search.

        Args:
            query (str): The search query.
            opts (dict): The search options.

        Returns:
            dict: The prepared search payload.
        """
        opts = BaiduSearchOpts(**user_opts if user_opts is not None else {})

        opts.check_parameter_validity()

        payload = {
            "source": source.BAIDU_SEARCH,
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

    def _prepare_url_payload(self, url: str, user_opts: Optional[dict] = None) -> dict:
        """
        Prepares the payload for a Baidu URL request.

        Args:
            url (str): The URL to be requested.
            opts (dict): Optional parameters for the request.

        Returns:
            dict: The prepared payload for the request.
        """
        validate_url(url, "baidu")
        opts = BaiduUrlOpts(**user_opts if user_opts is not None else {})

        opts.check_parameter_validity()

        payload = {
            "source": source.BAIDU_URL,
            "url": url,
            "user_agent_type": opts.user_agent_type,
            "callback_url": opts.callback_url,
        }

        if opts.parsing_instructions is not None:
            payload["parsing_instructions"] = opts.parsing_instructions
            payload["parse"] = True

        return payload
