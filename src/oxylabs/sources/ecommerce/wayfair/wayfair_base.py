from typing import Optional

import src.oxylabs.utils.utils as utils
from src.oxylabs.utils.constants import source
from src.oxylabs.utils.utils import validate_url


class WayfairSearchOpts:
    """
    Represents the search options for Wayfair.
    """

    def __init__(
        self,
        start_page=None,
        pages=None,
        limit=None,
        user_agent_type=None,
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
        utils.check_user_agent_type_validity(self.user_agent_type)
        utils.check_limit_validity_ecom(self.limit)
        utils.check_pages_validity(self.pages)
        utils.check_start_page_validity(self.start_page)


class WayfairUrlOpts:
    """
    Represents the URL options for Wayfair.
    """

    def __init__(self, user_agent_type=None, callback_url=None):
        self.user_agent_type = user_agent_type
        self.callback_url = callback_url

    def check_parameter_validity(self):
        """
        Checks the validity of WayfairUrlOpts parameters.
        """
        utils.check_user_agent_type_validity(self.user_agent_type)


class WayfairBase:
    def _prepare_search_payload(
        self, query: str, user_opts: Optional[dict] = None
    ) -> dict:
        """
        Prepare the search payload for Wayfair.

        Args:
            query (str): The search query.
            user_opts (dict): Optional user-defined options.

        Returns:
            dict: The prepared search payload.
        """
        opts = WayfairSearchOpts(**user_opts if user_opts is not None else {})

        opts.check_parameter_validity()

        payload = {
            "source": source.WAYFAIR_SEARCH,
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

    def _prepare_url_payload(self, url: str, user_opts: Optional[dict] = None) -> dict:
        """
        Prepare the payload for a Wayfair URL request.

        Args:
            url (str): The Wayfair URL to be requested.
            user_opts (dict): Optional user-defined options.

        Returns:
            dict: The prepared payload containing the source, URL, user agent type, and callback URL.

        Raises:
            ValidationError: If the URL is invalid.

        """
        validate_url(url, "wayfair")
        opts = WayfairUrlOpts(**user_opts if user_opts is not None else {})

        opts.check_parameter_validity()

        payload = {
            "source": source.WAYFAIR,
            "url": url,
            "user_agent_type": opts.user_agent_type,
            "callback_url": opts.callback_url,
        }

        return payload
