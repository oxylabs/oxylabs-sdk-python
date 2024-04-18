import oxylabs.utils.utils as utils
from oxylabs.utils import source
from oxylabs.utils.utils import BaseEcommerceOpts, validate_url
from typing import Any, Dict, Optional


class AmazonSearchOpts(BaseEcommerceOpts):
    """
    Represents the search options for AmazonSearch.
    """

    def __init__(
        self,
        domain=None,
        start_page=None,
        pages=None,
        context=None,
        parse=None,
        **kwargs
    ):
        super().__init__(**kwargs)
        self.domain = domain
        self.start_page = start_page
        self.pages = pages
        self.context = context
        self.parse = parse

    def check_parameter_validity(self):
        """
        Checks the validity of AmazonSearchOpts parameters.
        """
        utils.check_user_agent_validity(self.user_agent_type)
        utils.check_render_validity(self.render)
        utils.check_pages_validity(self.pages)
        utils.check_start_page_validity(self.start_page)


class AmazonUrlOpts(BaseEcommerceOpts):
    """
    Represents the URL options for AmazonUrl.
    """

    def __init__(self, parse=None, **kwargs):
        super().__init__(**kwargs)
        self.parse = parse

    def check_parameter_validity(self):
        """
        Checks the validity of AmazonUrlOpts parameters.
        """
        utils.check_user_agent_validity(self.user_agent_type)
        utils.check_render_validity(self.render)


class AmazonProductOpts(BaseEcommerceOpts):
    """
    Represents the product options for AmazonProduct.
    """

    def __init__(self, domain=None, context=None, parse=None, **kwargs):
        super().__init__(**kwargs)
        self.domain = domain
        self.context = context
        self.parse = parse

    def check_parameter_validity(self):
        """
        Checks the validity of AmazonProductOpts parameters.
        """
        utils.check_user_agent_validity(self.user_agent_type)
        utils.check_render_validity(self.render)


class AmazonPricingOpts(BaseEcommerceOpts):
    """
    Represents the product pricing options for AmazonPricing.
    """

    def __init__(self, domain=None, start_page=None, pages=None, parse=None, **kwargs):
        super().__init__(**kwargs)
        self.domain = domain
        self.start_page = start_page
        self.pages = pages
        self.parse = parse

    def check_parameter_validity(self):
        """
        Checks the validity of AmazonPricingOpts parameters.
        """
        utils.check_user_agent_validity(self.user_agent_type)
        utils.check_render_validity(self.render)
        utils.check_pages_validity(self.pages)
        utils.check_start_page_validity(self.start_page)


class AmazonReviewsOpts(BaseEcommerceOpts):
    """
    Represents the product review options for AmazonReview.
    """

    def __init__(self, domain=None, start_page=None, pages=None, parse=None, **kwargs):
        super().__init__(**kwargs)
        self.domain = domain
        self.start_page = start_page
        self.pages = pages
        self.parse = parse

    def check_parameter_validity(self):
        """
        Checks the validity of AmazonReviewsOpts parameters.
        """
        utils.check_user_agent_validity(self.user_agent_type)
        utils.check_render_validity(self.render)
        utils.check_pages_validity(self.pages)
        utils.check_start_page_validity(self.start_page)


class AmazonQuestionsOpts(BaseEcommerceOpts):
    """
    Represents the product questions options for AmazonQuestions.
    """

    def __init__(self, domain=None, parse=None, **kwargs):
        super().__init__(**kwargs)
        self.domain = domain
        self.parse = parse

    def check_parameter_validity(self):
        """
        Checks the validity of AmazonQuestionsOpts parameters.
        """
        utils.check_user_agent_validity(self.user_agent_type)
        utils.check_render_validity(self.render)


class AmazonBestsellerOpts(BaseEcommerceOpts):
    """
    Represents the bestseller options for AmazonBestseller.
    """

    def __init__(self, domain=None, start_page=None, pages=None, parse=None, **kwargs):
        super().__init__(**kwargs)
        self.domain = domain
        self.start_page = start_page
        self.pages = pages
        self.parse = parse

    def check_parameter_validity(self):
        """
        Checks the validity of AmazonBestsellerOpts parameters.
        """
        utils.check_user_agent_validity(self.user_agent_type)
        utils.check_render_validity(self.render)
        utils.check_pages_validity(self.pages)
        utils.check_start_page_validity(self.start_page)


class AmazonSellerOpts(BaseEcommerceOpts):
    """
    Represents the seller options for AmazonSeller.
    """

    def __init__(self, domain=None, parse=None, **kwargs):
        super().__init__(**kwargs)
        self.domain = domain
        self.parse = parse

    def check_parameter_validity(self):
        """
        Checks the validity of AmazonSellerOpts parameters.
        """
        utils.check_user_agent_validity(self.user_agent_type)
        utils.check_render_validity(self.render)


class AmazonBase:
    def _prepare_amazon_search_payload(
        self, query: str, user_opts: Optional[Dict[str, Any]] = None
    ) -> dict:
        """
        Prepares the search payload for Amazon search.

        Args:
            query (str): The search query.
            user_opts (dict): Optional user-defined options.

        Returns:
            dict: The prepared search payload.

        Raises:
            None

        """

        opts = AmazonSearchOpts(**user_opts if user_opts is not None else {})

        opts.check_parameter_validity()

        payload = {
            "source": source.AMAZON_SEARCH,
            "domain": opts.domain,
            "query": query,
            "start_page": opts.start_page,
            "pages": opts.pages,
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

    def _prepare_amazon_url_payload(
        self, url: str, user_opts: Optional[Dict[str, Any]] = None
    ) -> dict:
        """
        Prepares the payload for making a request to Amazon URL.

        Args:
            url (str): The URL to be requested.
            user_opts (dict): Optional user-defined options.

        Returns:
            dict: The prepared payload for the request.

        Raises:
            ValueError: If the URL is invalid.

        """
        validate_url(url, "amazon")
        opts = AmazonUrlOpts(**user_opts if user_opts is not None else {})

        opts.check_parameter_validity()

        payload = {
            "source": source.AMAZON_URL,
            "url": url,
            "user_agent_type": opts.user_agent_type,
            "render": opts.render,
            "callback_url": opts.callback_url,
            "parse": opts.parse,
        }

        if opts.parsing_instructions is not None:
            payload["parsing_instructions"] = opts.parsing_instructions
            payload["parse"] = True

        return payload

    def _prepare_amazon_product_payload(
        self, query: str, user_opts: Optional[Dict[str, Any]] = None
    ) -> dict:
        """
        Prepare the payload for the Amazon product request.

        Args:
            query (str): The search query for the product.
            user_opts (dict): User options for the request.

        Returns:
            dict: The prepared payload for the request.
        """
        opts = AmazonProductOpts(**user_opts if user_opts is not None else {})

        opts.check_parameter_validity()

        payload = {
            "source": source.AMAZON_PRODUCT,
            "domain": opts.domain,
            "query": query,
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

    def _prepare_amazon_pricing_payload(
        self, query: str, user_opts: Optional[Dict[str, Any]] = None
    ) -> dict:
        """
        Prepares the payload for pricing request to Amazon.

        Args:
            query (str): The search query.
            user_opts (dict): User options for pricing request.

        Returns:
            dict: The prepared payload for pricing request.
        """

        opts = AmazonPricingOpts(**user_opts if user_opts is not None else {})

        opts.check_parameter_validity()

        payload = {
            "source": source.AMAZON_PRICING,
            "domain": opts.domain,
            "query": query,
            "start_page": opts.start_page,
            "pages": opts.pages,
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

    def _prepare_amazon_reviews_payload(
        self, query: str, user_opts: Optional[Dict[str, Any]] = None
    ) -> dict:
        """
        Prepare the payload for retrieving Amazon reviews.

        Args:
            query (str): The search query for the reviews.
            user_opts (dict): User-defined options for retrieving the reviews.

        Returns:
            dict: The prepared payload for retrieving Amazon reviews.
        """
        opts = AmazonReviewsOpts(**user_opts if user_opts is not None else {})

        opts.check_parameter_validity()

        payload = {
            "source": source.AMAZON_REVIEWS,
            "domain": opts.domain,
            "query": query,
            "start_page": opts.start_page,
            "pages": opts.pages,
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

    def _prepare_amazon_questions_payload(
        self, query: str, user_opts: Optional[Dict[str, Any]] = None
    ) -> dict:
        """
        Prepare the payload for sending a request to retrieve Amazon questions.

        Args:
            query (str): The query string for the Amazon questions.
            user_opts (dict): Optional user-defined options for the request.

        Returns:
            dict: The prepared payload for the request.

        Raises:
            ValueError: If the provided options are invalid.
        """
        opts = AmazonQuestionsOpts(**user_opts if user_opts is not None else {})

        opts.check_parameter_validity()

        payload = {
            "source": source.AMAZON_QUESTIONS,
            "domain": opts.domain,
            "query": query,
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

    def _prepare_amazon_bestseller_payload(
        self, query: str, user_opts: Optional[Dict[str, Any]] = None
    ) -> dict:
        """
        Prepares the payload for retrieving Amazon bestsellers.

        Args:
            query (str): The search query.
            user_opts (dict): The user options for customizing the request.

        Returns:
            dict: The prepared payload for the request.
        """
        opts = AmazonBestsellerOpts(**user_opts if user_opts is not None else {})

        opts.check_parameter_validity()

        payload = {
            "source": source.AMAZON_BEST_SELLERS,
            "domain": opts.domain,
            "query": query,
            "start_page": opts.start_page,
            "pages": opts.pages,
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

    def _prepare_amazon_seller_payload(
        self, query: str, user_opts: Optional[Dict[str, Any]] = None
    ) -> dict:
        """
        Prepare the payload for the Amazon seller request.

        Args:
            query (str): The query string.
            user_opts (dict): The user options for the request.

        Returns:
            dict: The prepared payload for the request.
        """
        opts = AmazonSellerOpts(**user_opts if user_opts is not None else {})

        opts.check_parameter_validity()

        payload = {
            "source": source.AMAZON_SELLERS,
            "domain": opts.domain,
            "query": query,
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
