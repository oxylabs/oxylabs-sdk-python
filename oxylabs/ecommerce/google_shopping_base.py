from typing import Optional, Dict, Any
from oxylabs.utils.defaults import (
    DEFAULT_DOMAIN,
    DEFAULT_PAGES,
    DEFAULT_START_PAGE,
    set_default_domain,
    set_default_pages,
    set_default_start_page,
    set_default_user_agent,
    set_default_sort_by,
)
from oxylabs.utils.utils import validate_url, BaseEcommerceOpts
from oxylabs.utils import source
import oxylabs.utils.utils as utils


class GoogleShoppingSearchOpts(BaseEcommerceOpts):
    """
    Represents the search options for GoogleShoppingSearch.
    """

    def __init__(
        self,
        domain=None,
        start_page=None,
        pages=None,
        locale=None,
        results_language=None,
        context=None,
        parse=None,
        **kwargs
    ):
        super().__init__(**kwargs)
        self.domain = domain
        self.start_page = start_page
        self.pages = pages
        self.locale = locale
        self.results_language = results_language
        self.context = context
        self.parse = parse

    ACCEPTED_SORT_BY_PARAMS = [
        "r",
        "p",
        "rv",
        "pd",
    ]

    def check_parameter_validity(self):
        """
        Checks the validity of GoogleShoppingSearchOpts parameters.
        """
        utils.check_user_agent_validity(self.user_agent_type)
        utils.check_render_validity(self.render)
        utils.check_pages_validity(self.pages)
        utils.check_start_page_validity(self.start_page)
        utils.check_sorting_parameter_validity(
            self.context, self.ACCEPTED_SORT_BY_PARAMS
        )
        utils.check_price_range_validity(self.context)


class GoogleShoppingUrlOpts(BaseEcommerceOpts):
    """
    Represents the URL options for GoogleShoppingUrl.
    """

    def __init__(self, parse=None, **kwargs):
        super().__init__(**kwargs)
        self.parse = parse

    def check_parameter_validity(self):
        """
        Checks the validity of GoogleShoppingUrlOpts parameters.
        """
        utils.check_user_agent_validity(self.user_agent_type)
        utils.check_render_validity(self.render)


class GoogleShoppingProductOpts(BaseEcommerceOpts):
    """
    Represents the product options for GoogleShoppingProduct.
    """

    def __init__(
        self, domain=None, locale=None, results_language=None, parse=None, **kwargs
    ):
        super().__init__(**kwargs)
        self.domain = domain
        self.locale = locale
        self.results_language = results_language
        self.parse = parse

    def check_parameter_validity(self):
        """
        Checks the validity of GoogleShoppingProductOpts parameters.
        """
        utils.check_user_agent_validity(self.user_agent_type)
        utils.check_render_validity(self.render)


class GoogleProductPricingOpts(BaseEcommerceOpts):
    """
    Represents the product pricing options for GoogleProductPricing.
    """

    def __init__(
        self,
        domain=None,
        start_page=None,
        pages=None,
        locale=None,
        results_language=None,
        parse=None,
        **kwargs
    ):
        super().__init__(**kwargs)
        self.domain = domain
        self.start_page = start_page
        self.pages = pages
        self.locale = locale
        self.results_language = results_language
        self.parse = parse

    def check_parameter_validity(self):
        """
        Checks the validity of GoogleProductPricingOpts parameters.
        """
        utils.check_user_agent_validity(self.user_agent_type)
        utils.check_render_validity(self.render)
        utils.check_pages_validity(self.pages)
        utils.check_start_page_validity(self.start_page)


class GoogleShoppingBase:
    def _prepare_google_shopping_search_payload(
        self, query: str, user_opts: Optional[dict] = None
    ) -> dict:
        """
        Prepare the search payload for Google Shopping.

        Args:
            query (str): The search query.
            user_opts (dict): Optional user-defined options.

        Returns:
            dict: The prepared search payload.

        """
        opts = GoogleShoppingSearchOpts(**user_opts if user_opts is not None else {})

        opts.check_parameter_validity()

        payload = {
            "source": source.GOOGLE_SHOPPING_SEARCH,
            "domain": opts.domain,
            "query": query,
            "start_page": opts.start_page,
            "pages": opts.pages,
            "locale": opts.locale,
            "results_language": opts.results_language,
            "geo_location": opts.geo_location,
            "user_agent_type": opts.user_agent_type,
            "render": opts.render,
            "callback_url": opts.callback_url,
            "context": opts.context,
            "parse": opts.parse,
        }

        if opts.parsing_instructions is not None:
            payload["parsing_instructions"] = opts.parsing_instructions
            payload["parse"] = True

        return payload

    def _prepare_google_shopping_url_payload(
        self, url: str, user_opts: Optional[dict] = None
    ) -> dict:
        """
        Prepares the payload for a Google Shopping URL request.

        Args:
            url (str): The URL to be used for the request.
            user_opts (dict): Optional user-defined options.

        Returns:
            dict: The prepared payload for the request.
        """
        validate_url(url, "google")
        opts = GoogleShoppingUrlOpts(**user_opts if user_opts is not None else {})

        opts.check_parameter_validity()

        payload = {
            "source": source.GOOGLE_SHOPPING_URL,
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

    def _prepare_google_shopping_product_payload(
        self, query: str, user_opts: Optional[dict] = None
    ) -> dict:
        """
        Prepare the payload for the Google Shopping product request.

        Args:
            query (str): The search query.
            user_opts (dict): User options for the request.

        Returns:
            dict: The prepared payload for the request.
        """
        opts = GoogleShoppingProductOpts(**user_opts if user_opts is not None else {})

        opts.check_parameter_validity()

        payload = {
            "source": source.GOOGLE_SHOPPING_PRODUCT,
            "query": query,
            "domain": opts.domain,
            "locale": opts.locale,
            "results_language": opts.results_language,
            "geo_location": opts.geo_location,
            "user_agent_type": opts.user_agent_type,
            "render": opts.render,
            "callback_url": opts.callback_url,
            "parse": opts.parse,
        }

        if opts.parsing_instructions is not None:
            payload["parsing_instructions"] = opts.parsing_instructions
            payload["parse"] = True

        return payload

    def _prepare_google_shopping_product_pricing_payload(
        self, query: str, user_opts: Optional[dict] = None
    ) -> dict:
        """
        Prepares the payload for retrieving product pricing from Google Shopping.

        Args:
            query (str): The search query for the products.
            user_opts (dict): User-defined options for the request.

        Returns:
            dict: The prepared payload for the request.
        """
        opts = GoogleProductPricingOpts(**user_opts if user_opts is not None else {})

        opts.check_parameter_validity()

        payload = {
            "source": source.GOOGLE_SHOPPING_PRICING,
            "domain": opts.domain,
            "query": query,
            "start_page": opts.start_page,
            "pages": opts.pages,
            "locale": opts.locale,
            "results_language": opts.results_language,
            "geo_location": opts.geo_location,
            "user_agent_type": opts.user_agent_type,
            "render": opts.render,
            "callback_url": opts.callback_url,
            "parse": opts.parse,
        }

        if opts.parsing_instructions is not None:
            payload["parsing_instructions"] = opts.parsing_instructions
            payload["parse"] = True

        return payload
