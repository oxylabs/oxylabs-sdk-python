from utils.defaults import (
    DEFAULT_DOMAIN,
    DEFAULT_PAGES,
    DEFAULT_START_PAGE,
    set_default_domain,
    set_default_pages,
    set_default_start_page,
    set_default_user_agent,
)
from utils.utils import validate_url, BaseEcommerceOpts
from utils import source
import utils.utils as utils


class AmazonSearchOpts(BaseEcommerceOpts):
    """
    Represents the search options for AmazonSearch.
    """

    def __init__(
        self,
        domain=DEFAULT_DOMAIN,
        start_page=DEFAULT_START_PAGE,
        pages=DEFAULT_PAGES,
        locale=None,
        context=None,
        parse=None,
        **kwargs
    ):
        super().__init__(**kwargs)
        self.domain = domain
        self.start_page = start_page
        self.pages = pages
        self.locale = locale
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

    def __init__(self, locale=None, parse=None, **kwargs):
        super().__init__(**kwargs)
        self.locale = locale
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

    def __init__(
        self, domain=DEFAULT_DOMAIN, locale=None, context=None, parse=None, **kwargs
    ):
        super().__init__(**kwargs)
        self.domain = domain
        self.locale = locale
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

    def __init__(
        self,
        domain=DEFAULT_DOMAIN,
        start_page=DEFAULT_START_PAGE,
        pages=DEFAULT_PAGES,
        locale=None,
        parse=None,
        **kwargs
    ):
        super().__init__(**kwargs)
        self.domain = domain
        self.start_page = start_page
        self.pages = pages
        self.locale = locale
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

    def __init__(
        self,
        domain=DEFAULT_DOMAIN,
        start_page=DEFAULT_START_PAGE,
        pages=DEFAULT_PAGES,
        locale=None,
        parse=None,
        **kwargs
    ):
        super().__init__(**kwargs)
        self.domain = domain
        self.start_page = start_page
        self.pages = pages
        self.locale = locale
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

    def __init__(self, domain=DEFAULT_DOMAIN, locale=None, parse=None, **kwargs):
        super().__init__(**kwargs)
        self.domain = domain
        self.locale = locale
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

    def __init__(
        self,
        domain=DEFAULT_DOMAIN,
        start_page=DEFAULT_START_PAGE,
        pages=DEFAULT_PAGES,
        locale=None,
        parse=None,
        **kwargs
    ):
        super().__init__(**kwargs)
        self.domain = domain
        self.start_page = start_page
        self.pages = pages
        self.locale = locale
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

    def __init__(self, domain=DEFAULT_DOMAIN, locale=None, parse=None, **kwargs):
        super().__init__(**kwargs)
        self.domain = domain
        self.locale = locale
        self.parse = parse

    def check_parameter_validity(self):
        """
        Checks the validity of AmazonSellerOpts parameters.
        """
        utils.check_user_agent_validity(self.user_agent_type)
        utils.check_render_validity(self.render)


class AmazonBase:
    def _prepare_search_payload(self, query: str, user_opts: dict) -> dict:
        """
        Prepares the search payload for Amazon search.

        Args:
            query (str): The search query.
            user_opts (dict): User options for the search.

        Returns:
            dict: The prepared search payload.

        Raises:
            None

        """

        opts = AmazonSearchOpts(**user_opts if user_opts is not None else {})

        # Set defaults and check validity
        opts.domain = set_default_domain(opts.domain)
        opts.start_page = set_default_start_page(opts.start_page)
        opts.pages = set_default_pages(opts.pages)
        opts.user_agent_type = set_default_user_agent(opts.user_agent_type)

        opts.check_parameter_validity()

        payload = {
            "source": source.AMAZON_SEARCH,
            "domain": opts.domain,
            "query": query,
            "start_page": opts.start_page,
            "pages": opts.pages,
            "geo_location": opts.geo_location,
            "user_agent_type": opts.user_agent_type,
            "locale": opts.locale,
            "render": opts.render,
            "callback_url": opts.callback_url,
            "context": opts.context,
            "parse": opts.parse,
        }

        if opts.parsing_instructions is not None:
            payload["parsing_instructions"] = opts.parsing_instructions
            payload["parse"] = True

        return payload

    def _prepare_url_payload(self, url: str, user_opts: dict) -> dict:
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

        # Set defaults and check validity
        opts.user_agent_type = set_default_user_agent(opts.user_agent_type)
        opts.check_parameter_validity()

        payload = {
            "source": source.AMAZON_URL,
            "url": url,
            "user_agent_type": opts.user_agent_type,
            "locale": opts.locale,
            "render": opts.render,
            "callback_url": opts.callback_url,
            "geo_location": opts.geo_location,
            "parse": opts.parse,
        }

        if opts.parsing_instructions is not None:
            payload["parsing_instructions"] = opts.parsing_instructions
            payload["parse"] = True

        return payload

    def _prepare_product_payload(self, query: str, user_opts: dict) -> dict:
        """
        Prepare the payload for the Amazon product request.

        Args:
            query (str): The search query for the product.
            user_opts (dict): User options for the request.

        Returns:
            dict: The prepared payload for the request.
        """
        opts = AmazonProductOpts(**user_opts if user_opts is not None else {})

        opts.domain = set_default_domain(opts.domain)
        opts.user_agent_type = set_default_user_agent(opts.user_agent_type)

        opts.check_parameter_validity()

        payload = {
            "source": source.AMAZON_PRODUCT,
            "domain": opts.domain,
            "query": query,
            "geo_location": opts.geo_location,
            "user_agent_type": opts.user_agent_type,
            "locale": opts.locale,
            "render": opts.render,
            "callback_url": opts.callback_url,
            "context": opts.context,
            "parse": opts.parse,
        }

        if opts.parsing_instructions is not None:
            payload["parsing_instructions"] = opts.parsing_instructions
            payload["parse"] = True

        return payload

    def _prepare_pricing_payload(self, query: str, user_opts: dict) -> dict:
        """
        Prepares the payload for pricing request to Amazon.

        Args:
            query (str): The search query.
            user_opts (dict): User options for pricing request.

        Returns:
            dict: The prepared payload for pricing request.
        """

        opts = AmazonPricingOpts(**user_opts if user_opts is not None else {})

        opts.domain = set_default_domain(opts.domain)
        opts.start_page = set_default_start_page(opts.start_page)
        opts.pages = set_default_pages(opts.pages)
        opts.user_agent_type = set_default_user_agent(opts.user_agent_type)

        opts.check_parameter_validity()

        payload = {
            "source": source.AMAZON_PRICING,
            "domain": opts.domain,
            "query": query,
            "start_page": opts.start_page,
            "pages": opts.pages,
            "geo_location": opts.geo_location,
            "user_agent_type": opts.user_agent_type,
            "locale": opts.locale,
            "render": opts.render,
            "callback_url": opts.callback_url,
            "parse": opts.parse,
        }

        if opts.parsing_instructions is not None:
            payload["parsing_instructions"] = opts.parsing_instructions
            payload["parse"] = True

        return payload

    def _prepare_reviews_payload(self, query: str, user_opts: dict) -> dict:
        """
        Prepare the payload for retrieving Amazon reviews.

        Args:
            query (str): The search query for the reviews.
            user_opts (dict): User-defined options for retrieving the reviews.

        Returns:
            dict: The prepared payload for retrieving Amazon reviews.
        """
        opts = AmazonReviewsOpts(**user_opts if user_opts is not None else {})

        opts.domain = set_default_domain(opts.domain)
        opts.start_page = set_default_start_page(opts.start_page)
        opts.pages = set_default_pages(opts.pages)
        opts.user_agent_type = set_default_user_agent(opts.user_agent_type)

        opts.check_parameter_validity()

        payload = {
            "source": source.AMAZON_REVIEWS,
            "domain": opts.domain,
            "query": query,
            "geo_location": opts.geo_location,
            "user_agent_type": opts.user_agent_type,
            "locale": opts.locale,
            "start_page": opts.start_page,
            "pages": opts.pages,
            "render": opts.render,
            "callback_url": opts.callback_url,
            "parse": opts.parse,
        }

        if opts.parsing_instructions is not None:
            payload["parsing_instructions"] = opts.parsing_instructions
            payload["parse"] = True

        return payload

    def _prepare_questions_payload(self, query: str, user_opts: dict) -> dict:
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

        opts.domain = set_default_domain(opts.domain)
        opts.user_agent_type = set_default_user_agent(opts.user_agent_type)

        opts.check_parameter_validity()

        payload = {
            "source": source.AMAZON_QUESTIONS,
            "domain": opts.domain,
            "query": query,
            "geo_location": opts.geo_location,
            "user_agent_type": opts.user_agent_type,
            "locale": opts.locale,
            "render": opts.render,
            "callback_url": opts.callback_url,
            "parse": opts.parse,
        }

        if opts.parsing_instructions is not None:
            payload["parsing_instructions"] = opts.parsing_instructions
            payload["parse"] = True

        return payload

    def _prepare_bestseller_payload(self, query: str, user_opts: dict) -> dict:
        """
        Prepares the payload for retrieving Amazon bestsellers.

        Args:
            query (str): The search query.
            user_opts (dict): The user options for customizing the request.

        Returns:
            dict: The prepared payload for the request.
        """
        opts = AmazonBestsellerOpts(**user_opts if user_opts is not None else {})

        opts.domain = set_default_domain(opts.domain)
        opts.start_page = set_default_start_page(opts.start_page)
        opts.pages = set_default_pages(opts.pages)
        opts.user_agent_type = set_default_user_agent(opts.user_agent_type)

        opts.check_parameter_validity()

        payload = {
            "source": source.AMAZON_BEST_SELLERS,
            "domain": opts.domain,
            "query": query,
            "start_page": opts.start_page,
            "pages": opts.pages,
            "geo_location": opts.geo_location,
            "user_agent_type": opts.user_agent_type,
            "locale": opts.locale,
            "render": opts.render,
            "callback_url": opts.callback_url,
            "parse": opts.parse,
        }

        if opts.parsing_instructions is not None:
            payload["parsing_instructions"] = opts.parsing_instructions
            payload["parse"] = True

        return payload

    def _prepare_seller_payload(self, query: str, user_opts: dict) -> dict:
        """
        Prepare the payload for the Amazon seller request.

        Args:
            query (str): The query string.
            user_opts (dict): The user options for the request.

        Returns:
            dict: The prepared payload for the request.
        """
        opts = AmazonSellerOpts(**user_opts if user_opts is not None else {})

        opts.domain = set_default_domain(opts.domain)
        opts.user_agent_type = set_default_user_agent(opts.user_agent_type)

        opts.check_parameter_validity()

        payload = {
            "source": source.AMAZON_SELLERS,
            "domain": opts.domain,
            "query": query,
            "geo_location": opts.geo_location,
            "user_agent_type": opts.user_agent_type,
            "locale": opts.locale,
            "render": opts.render,
            "callback_url": opts.callback_url,
            "parse": opts.parse,
        }

        if opts.parsing_instructions is not None:
            payload["parsing_instructions"] = opts.parsing_instructions
            payload["parse"] = True

        return payload
