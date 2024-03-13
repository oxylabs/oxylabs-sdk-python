from utils.defaults import (
    DEFAULT_DOMAIN,
    DEFAULT_LIMIT_SERP,
    DEFAULT_PAGES,
    DEFAULT_START_PAGE,
    set_default_domain,
    set_default_limit,
    set_default_pages,
    set_default_start_page,
    set_default_user_agent,
    set_default_hotel_occupancy,
    set_default_tbm_context,
)
from utils.utils import BaseGoogleOpts, validate_url
from utils import source, render
import utils.utils as utils
from typing import Optional, Any


class GoogleSearchOpts(BaseGoogleOpts):
    def __init__(
        self,
        domain: str = DEFAULT_DOMAIN,
        start_page: int = DEFAULT_START_PAGE,
        pages: int = DEFAULT_PAGES,
        limit: int = DEFAULT_LIMIT_SERP,
        locale: Optional[str] = None,
        parse: bool = False,
        **kwargs: Any,
    ) -> None:
        """
        Initializes a new instance of the GoogleBase class.

        Args:
            domain (str): The domain to search on. Defaults to DEFAULT_DOMAIN.
            start_page (int): The starting page number. Defaults to DEFAULT_START_PAGE.
            pages (int): The number of pages to retrieve. Defaults to DEFAULT_PAGES.
            limit (int): The maximum number of search results per page. Defaults to DEFAULT_LIMIT_SERP.
            locale (str): The locale to use for the search. Defaults to None.
            parse (bool): Whether to parse the search results. Defaults to False.
            **kwargs: Additional keyword arguments to pass to the base class.

        """
        super().__init__(
            **kwargs,
        )
        self.domain = domain
        self.start_page = start_page
        self.pages = pages
        self.limit = limit
        self.locale = locale
        self.parse = parse

    AcceptedTbmParameters = [
        "app",
        "bks",
        "isch",
        "nws",
        "pts",
        "vid",
    ]

    def check_parameter_validity(self):
        """
        Checks the validity of the parameters used for the Google SERP API request.

        This method validates the user agent type, render option, limit, pages, start page,
        parsing instructions, and context TBM parameters. It calls various utility functions
        to perform the validation.

        Raises:
            ValueError: If any of the parameters are invalid.
        """
        utils.check_user_agent_validity(self.user_agent_type)
        utils.check_render_validity(self.render)
        utils.check_limit_validity(self.limit)
        utils.check_pages_validity(self.pages)
        utils.check_start_page_validity(self.start_page)
        utils.check_parsing_instructions_validity(self.parsing_instructions)
        utils.check_context_tbm_validity(self.context, self.AcceptedTbmParameters)


class GoogleUrlOpts(BaseGoogleOpts):

    def __init__(self, parse: bool = False, **kwargs: Any) -> None:
        """
        Initializes a new instance of the GoogleBase class.

        Args:
            parse (bool, optional): Indicates whether to parse the response. Defaults to False.
            **kwargs: Additional keyword arguments to be passed to the base class constructor.
        """
        super().__init__(
            **kwargs,
        )
        self.parse = parse

    def check_parameter_validity(self):
        """
        Checks the validity of the parameters used in the GoogleBase class.

        This method calls various utility functions to validate the user agent type,
        render option, and parsing instructions. If any of these parameters are invalid,
        an exception will be raised.

        Parameters:
            self (GoogleBase): The current instance of the GoogleBase class.

        Raises:
            InvalidUserAgentError: If the user agent type is invalid.
            InvalidRenderError: If the render option is invalid.
            InvalidParsingInstructionsError: If the parsing instructions are invalid.
        """
        utils.check_user_agent_validity(self.user_agent_type)
        utils.check_render_validity(self.render)
        utils.check_parsing_instructions_validity(self.parsing_instructions)


class GoogleAdsOpts(BaseGoogleOpts):
    """
    Represents options for making Google Ads API requests.

    Args:
        parse (bool): Whether to parse the response. Defaults to False.
        domain (str): The domain to search on. Defaults to DEFAULT_DOMAIN.
        start_page (int): The starting page number. Defaults to DEFAULT_START_PAGE.
        pages (int): The number of pages to retrieve. Defaults to DEFAULT_PAGES.
        limit (int): The maximum number of results to retrieve. Defaults to DEFAULT_LIMIT_SERP.
        locale (str): The locale to use for the search. Defaults to None.
        **kwargs: Additional keyword arguments.

    Attributes:
        AcceptedTbmParameters (list): A list of accepted TBM (To Be Matched) parameters.

    Methods:
        check_parameter_validity: Checks the validity of the parameters.

    """

    def __init__(
        self,
        parse: bool = False,
        domain: str = DEFAULT_DOMAIN,
        start_page: int = DEFAULT_START_PAGE,
        pages: int = DEFAULT_PAGES,
        limit: int = DEFAULT_LIMIT_SERP,
        locale: Optional[str] = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(
            **kwargs,
        )
        self.domain = domain
        self.start_page = start_page
        self.pages = pages
        self.limit = limit
        self.locale = locale
        self.parse = parse

    AcceptedTbmParameters = [
        "app",
        "bks",
        "isch",
        "nws",
        "pts",
        "vid",
    ]

    def check_parameter_validity(self):
        """
        Checks the validity of the parameters.

        Raises:
            ValueError: If any of the parameters are invalid.

        """
        utils.check_user_agent_validity(self.user_agent_type)
        utils.check_render_validity(self.render)
        utils.check_start_page_validity(self.start_page)
        utils.check_parsing_instructions_validity(self.parsing_instructions)
        utils.check_context_tbm_validity(self.context, self.AcceptedTbmParameters)


class GoogleSuggestionsOpts(BaseGoogleOpts):
    """
    Options for making Google Suggestions API requests.

    Args:
        locale (str): The locale to use for the suggestions. Defaults to None.

    Attributes:
        locale (str): The locale to use for the suggestions.

    Methods:
        check_parameter_validity: Checks the validity of the parameters.

    """

    def __init__(
        self,
        locale: Optional[str] = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(
            **kwargs,
        )
        self.locale = locale

    def check_parameter_validity(self):
        """
        Checks the validity of the parameters.

        This method checks the validity of the user agent type, render, and parsing instructions.

        Returns:
            None

        """
        utils.check_user_agent_validity(self.user_agent_type)
        utils.check_render_validity(self.render)
        utils.check_parsing_instructions_validity(self.parsing_instructions)


class GoogleHotelsOpts(BaseGoogleOpts):
    """
    Options for making requests to Google Hotels search engine.

    Args:
        domain (str): The domain to use for the search. Defaults to DEFAULT_DOMAIN.
        start_page (int): The starting page number for the search. Defaults to DEFAULT_START_PAGE.
        pages (int): The number of pages to retrieve. Defaults to DEFAULT_PAGES.
        limit (int): The maximum number of search results to retrieve. Defaults to DEFAULT_LIMIT_SERP.
        locale (str): The locale to use for the search. Defaults to None.
        **kwargs: Additional keyword arguments to pass to the parent class.

    Attributes:
        domain (str): The domain to use for the search.
        start_page (int): The starting page number for the search.
        pages (int): The number of pages to retrieve.
        limit (int): The maximum number of search results to retrieve.
        locale (str): The locale to use for the search.

    Methods:
        check_parameter_validity: Checks the validity of the search parameters.

    """

    def __init__(
        self,
        domain: str = DEFAULT_DOMAIN,
        start_page: int = DEFAULT_START_PAGE,
        pages: int = DEFAULT_PAGES,
        limit: int = DEFAULT_LIMIT_SERP,
        locale: Optional[str] = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(
            **kwargs,
        )
        self.domain = domain
        self.start_page = start_page
        self.pages = pages
        self.limit = limit
        self.locale = locale

    def check_parameter_validity(self):
        """
        Checks the validity of the search parameters.

        Raises:
            ValueError: If any of the search parameters are invalid.

        """
        utils.check_user_agent_validity(self.user_agent_type)
        utils.check_render_validity(self.render)
        utils.check_limit_validity(self.limit)
        utils.check_pages_validity(self.pages)
        utils.check_start_page_validity(self.start_page)
        utils.check_parsing_instructions_validity(self.parsing_instructions)


class GoogleTravelHotelsOpts(BaseGoogleOpts):
    """
    Options for retrieving hotel search results from Google Travel.

    Args:
        domain (str, optional): The domain to use for the search. Defaults to DEFAULT_DOMAIN.
        start_page (int, optional): The starting page number for the search. Defaults to DEFAULT_START_PAGE.
        locale (str, optional): The locale to use for the search. Defaults to None.
        **kwargs: Additional keyword arguments to be passed to the parent class.

    Attributes:
        domain (str): The domain to use for the search.
        start_page (int): The starting page number for the search.
        locale (str): The locale to use for the search.

    Methods:
        check_parameter_validity(): Checks the validity of the parameters.

    """

    def __init__(
        self,
        domain: str = DEFAULT_DOMAIN,
        start_page: int = DEFAULT_START_PAGE,
        locale: Optional[str] = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(
            **kwargs,
        )
        self.domain = domain
        self.start_page = start_page
        self.locale = locale

    def check_parameter_validity(self):
        """
        Checks the validity of the parameters.

        Raises:
            ValueError: If any of the parameters are invalid.

        """
        utils.check_user_agent_validity(self.user_agent_type)
        utils.check_render_validity(self.render)
        utils.check_start_page_validity(self.start_page)
        utils.check_parsing_instructions_validity(self.parsing_instructions)


class GoogleImagesOpts(BaseGoogleOpts):
    """
    Options for making requests to the Google Images search engine.

    Args:
        domain (str): The domain to use for the search. Defaults to DEFAULT_DOMAIN.
        start_page (int): The starting page number for the search. Defaults to DEFAULT_START_PAGE.
        pages (int): The number of pages to retrieve. Defaults to DEFAULT_PAGES.
        limit (int): The maximum number of search results to retrieve. Defaults to DEFAULT_LIMIT_SERP.
        locale (str): The locale to use for the search. Defaults to None.
        parse (bool): Whether to parse the search results. Defaults to False.
        **kwargs: Additional keyword arguments to pass to the parent class.

    Attributes:
        domain (str): The domain to use for the search.
        start_page (int): The starting page number for the search.
        pages (int): The number of pages to retrieve.
        limit (int): The maximum number of search results to retrieve.
        locale (str): The locale to use for the search.
        parse (bool): Whether to parse the search results.

    Methods:
        check_parameter_validity: Checks the validity of the parameters.

    """

    def __init__(
        self,
        domain: str = DEFAULT_DOMAIN,
        start_page: int = DEFAULT_START_PAGE,
        pages: int = DEFAULT_PAGES,
        limit: int = DEFAULT_LIMIT_SERP,
        locale: Optional[str] = None,
        parse: bool = False,
        **kwargs: Any,
    ) -> None:
        super().__init__(
            **kwargs,
        )
        self.domain = domain
        self.start_page = start_page
        self.pages = pages
        self.limit = limit
        self.locale = locale
        self.parse = parse

    def check_parameter_validity(self):
        """
        Checks the validity of the parameters.

        Raises:
            ValueError: If any of the parameters are invalid.

        """
        utils.check_render_validity(self.render)
        utils.check_start_page_validity(self.start_page)
        utils.check_parsing_instructions_validity(self.parsing_instructions)


class GoogleTrendsExploreOpts(BaseGoogleOpts):
    """
    Represents options for exploring Google Trends.

    This class provides methods to check the validity of parameters such as user agent type and parsing instructions.

    Attributes:
        user_agent_type (str): The type of user agent to be used.
        parsing_instructions (str): The parsing instructions to be applied.

    Methods:
        check_parameter_validity: Checks the validity of the parameters.

    """

    def check_parameter_validity(self):
        """
        Checks the validity of the parameters.

        This method checks the validity of the user agent type and parsing instructions.
        It calls utility functions to perform the validity checks.

        Returns:
            None

        """
        utils.check_user_agent_validity(self.user_agent_type)
        utils.check_parsing_instructions_validity(self.parsing_instructions)


class GoogleBase:
    def _prepare_search_payload(self, query: str, user_opts: Optional[dict]) -> dict:
        """
        Prepares the search payload for a Google search.

        Args:
            query (str): The search query.
            opts (dict): The options for the search.

        Returns:
            dict: The prepared search payload.

        Raises:
            ValueError: If the `limit`, `start_page`, and `pages` parameters are used together with the `limit_per_page` context parameter.

        """

        if (
            (
                user_opts.get("limit") is not None
                or user_opts.get("start_page") is not None
                or user_opts.get("pages") is not None
            )
            and user_opts.get("context")
            and any(
                item.get("key") == "limit_per_page" for item in user_opts["context"]
            )
        ):
            raise ValueError(
                "limit, start_page, and pages parameters cannot be used together with limit_per_page context parameter"
            )
            
        opts = GoogleSearchOpts(**user_opts if user_opts is not None else {})

        # Set defaults and check validity
        opts.domain = set_default_domain(opts.domain)
        opts.start_page = set_default_start_page(opts.start_page)
        opts.limit = set_default_limit(opts.limit, DEFAULT_LIMIT_SERP)
        opts.pages = set_default_pages(opts.pages)
        opts.user_agent_type = set_default_user_agent(opts.user_agent_type)
        opts.check_parameter_validity()

        # Prepare payload
        payload = {
            "source": source.GOOGLE_SEARCH,
            "domain": opts.domain,
            "query": query,
            "locale": opts.locale,
            "geo_location": opts.geo_location,
            "user_agent_type": opts.user_agent_type,
            "render": opts.render,
            "callback_url": opts.callback_url,
            "parse": opts.parse,
            "context": opts.context,
        }

        # If user sends limit_per_page context parameter, use it instead of limit, start_page, and pages parameters.
        if opts.context and any(
            opt.get("key") == "limit_per_page" for opt in opts.context
        ):
            payload["limit"] = None
            payload["start_page"] = None
            payload["pages"] = None
        else:
            payload["limit"] = opts.limit
            payload["start_page"] = opts.start_page
            payload["pages"] = opts.pages

        if opts.parsing_instructions:
            payload["parse"] = True
            payload["parsing_instructions"] = opts.parsing_instructions

        return payload

    def _prepare_url_payload(self, url: str, user_opts: Optional[dict]) -> dict:
        """
        Prepares the payload for a Google URL request.

        Args:
            url (str): The URL to be requested.
            opts (dict): Optional parameters for the request.

        Returns:
            dict: The prepared payload for the request.
        """
        validate_url(url, "google")
        opts = GoogleUrlOpts(**user_opts if user_opts is not None else {})

        # Set defaults and check validity
        opts.user_agent_type = set_default_user_agent(opts.user_agent_type)
        opts.check_parameter_validity()

        # Prepare payload
        payload = {
            "source": source.GOOGLE_URL,
            "url": url,
            "user_agent_type": opts.user_agent_type,
            "render": opts.render,
            "callback_url": opts.callback_url,
            "geo_location": opts.geo_location,
            "parse": opts.parse,
        }

        if opts.parsing_instructions is not None:
            payload["parsing_instructions"] = opts.parsing_instructions
            payload["parse"] = True

        return payload

    def _prepare_ads_payload(self, query: str, user_opts: Optional[dict]) -> dict:
        """
        Prepares the payload for the Google Ads request.

        Args:
            query (str): The search query.
            opts (dict): The options for the Google Ads request.

        Returns:
            dict: The prepared payload for the request.
        """
        opts = GoogleAdsOpts(**user_opts if user_opts is not None else {})

        # Set defaults and check validity
        opts.domain = set_default_domain(opts.domain)
        opts.start_page = set_default_start_page(opts.start_page)
        opts.pages = set_default_pages(opts.pages)
        opts.user_agent_type = set_default_user_agent(opts.user_agent_type)
        opts.check_parameter_validity()

        # Prepare payload
        payload = {
            "source": source.GOOGLE_ADS,
            "domain": opts.domain,
            "query": query,
            "locale": opts.locale,
            "geo_location": opts.geo_location,
            "user_agent_type": opts.user_agent_type,
            "render": opts.render,
            "callback_url": opts.callback_url,
            "parse": opts.parse,
            "context": opts.context,
        }

        if opts.parsing_instructions is not None:
            payload["parsing_instructions"] = opts.parsing_instructions
            payload["parse"] = True

        return payload

    def _prepare_suggestions_payload(
        self, query: str, user_opts: Optional[dict]
    ) -> dict:
        """
        Prepares the payload for making a suggestions request to Google.

        Args:
            query (str): The query for which suggestions are requested.
            opts (dict): The options for the suggestions request.

        Returns:
            dict: The prepared payload for the suggestions request.
        """
        opts = GoogleSuggestionsOpts(**user_opts if user_opts is not None else {})

        # Set defaults and check validity
        opts.user_agent_type = set_default_user_agent(opts.user_agent_type)
        opts.check_parameter_validity()

        # Prepare payload
        payload = {
            "source": source.GOOGLE_SUGGESTIONS,
            "query": query,
            "locale": opts.locale,
            "geo_location": opts.geo_location,
            "user_agent_type": opts.user_agent_type,
            "render": opts.render,
            "callback_url": opts.callback_url,
        }

        if opts.parsing_instructions is not None:
            payload["parsing_instructions"] = opts.parsing_instructions
            payload["parse"] = True

        return payload

    def _prepare_hotels_payload(self, query: str, user_opts: Optional[dict]) -> dict:
        """
        Prepares the payload for the hotels request.

        Args:
            query (str): The search query for hotels.
            opts (dict): The options for the hotels request.

        Returns:
            dict: The prepared payload for the hotels request.
        """
        opts = GoogleHotelsOpts(**user_opts if user_opts is not None else {})

        # Set defaults and check validity
        opts.domain = set_default_domain(opts.domain)
        opts.start_page = set_default_start_page(opts.start_page)
        opts.limit = set_default_limit(opts.limit, DEFAULT_LIMIT_SERP)
        opts.pages = set_default_pages(opts.pages)
        opts.user_agent_type = set_default_user_agent(opts.user_agent_type)
        opts.context = set_default_hotel_occupancy(opts.context)
        opts.check_parameter_validity()

        # Prepare payload
        payload = {
            "source": source.GOOGLE_HOTELS,
            "domain": opts.domain,
            "query": query,
            "start_page": opts.start_page,
            "pages": opts.pages,
            "limit": opts.limit,
            "locale": opts.locale,
            "geo_location": opts.geo_location,
            "user_agent_type": opts.user_agent_type,
            "render": opts.render,
            "callback_url": opts.callback_url,
            "context": opts.context,
        }

        if opts.parsing_instructions is not None:
            payload["parsing_instructions"] = opts.parsing_instructions
            payload["parse"] = True

        return payload

    def _prepare_travel_hotels_payload(
        self, query: str, user_opts: Optional[dict]
    ) -> dict:
        """
        Prepares the payload for the travel hotels request.

        Args:
            query (str): The search query.
            opts (dict): The options for the request.

        Returns:
            dict: The prepared payload for the request.
        """
        opts = GoogleTravelHotelsOpts(**user_opts if user_opts is not None else {})

        # Set defaults and check validity
        opts.domain = set_default_domain(opts.domain)
        opts.start_page = set_default_start_page(opts.start_page)
        opts.context = set_default_hotel_occupancy(opts.context)

        opts.check_parameter_validity()

        # Prepare payload
        payload = {
            "source": source.GOOGLE_TRAVEL_HOTELS,
            "domain": opts.domain,
            "query": query,
            "start_page": opts.start_page,
            "locale": opts.locale,
            "geo_location": opts.geo_location,
            "user_agent_type": opts.user_agent_type,
            "render": opts.render if opts.render else render.HTML,
            "callback_url": opts.callback_url,
            "context": opts.context,
        }

        if opts.parsing_instructions is not None:
            payload["parsing_instructions"] = opts.parsing_instructions
            payload["parse"] = True

        return payload

    def _prepare_images_payload(self, query: str, user_opts: Optional[dict]) -> dict:
        """
        Prepare the payload for the images search request.

        Args:
            query (str): The search query.
            opts (dict): The options for the images search.

        Returns:
            dict: The prepared payload for the images search request.
        """
        opts = GoogleImagesOpts(**user_opts if user_opts is not None else {})

        # Set defaults and check validity
        opts.user_agent_type = set_default_user_agent(opts.user_agent_type)
        opts.domain = set_default_domain(opts.domain)
        opts.start_page = set_default_start_page(opts.start_page)
        opts.pages = set_default_pages(opts.pages)
        opts.context = set_default_tbm_context(opts.context)
        opts.check_parameter_validity()

        # Prepare payload
        payload = {
            "source": source.GOOGLE_SEARCH,
            "domain": opts.domain,
            "query": query,
            "start_page": opts.start_page,
            "pages": opts.pages,
            "locale": opts.locale,
            "geo_location": opts.geo_location,
            "user_agent_type": opts.user_agent_type,
            "render": opts.render,
            "callback_url": opts.callback_url,
            "parse": opts.parse,
            "context": opts.context,
        }

        if opts.parsing_instructions is not None:
            payload["parsing_instructions"] = opts.parsing_instructions
            payload["parse"] = True

        return payload

    def _prepare_trends_explore_payload(
        self, query: str, user_opts: Optional[dict]
    ) -> dict:
        """
        Prepares the payload for Google Trends Explore API request.

        Args:
            query (str): The query string for the Google Trends Explore API request.
            opts (dict): Optional parameters for the Google Trends Explore API request.

        Returns:
            dict: The prepared payload for the Google Trends Explore API request.
        """
        opts = GoogleTrendsExploreOpts(**user_opts if user_opts is not None else {})

        # Set defaults and check validity
        opts.user_agent_type = set_default_user_agent(opts.user_agent_type)
        opts.check_parameter_validity()

        # Prepare payload
        payload = {
            "source": source.GOOGLE_TRENDS_EXPLORE,
            "query": query,
            "geo_location": opts.geo_location,
            "context": opts.context,
            "user_agent_type": opts.user_agent_type,
            "callback_url": opts.callback_url,
        }

        if opts.parsing_instructions is not None:
            payload["parsing_instructions"] = opts.parsing_instructions
            payload["parse"] = True

        return payload
