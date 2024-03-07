from utils.defaults import (
    DEFAULT_DOMAIN,
    DEFAULT_PAGES,
    DEFAULT_START_PAGE,
    set_default_domain,
    set_default_pages,
    set_default_start_page,
    set_default_user_agent,
    set_default_sort_by,
)
from utils.utils import validate_url, BaseEcommerceOpts
from utils.constants import Domain, Source
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
        **kwargs
    ):
        super().__init__(**kwargs)
        self.domain = domain
        self.start_page = start_page
        self.pages = pages
        self.locale = locale
        self.context = context

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

    def __init__(self, locale=None, **kwargs):
        super().__init__(**kwargs)
        self.locale = locale

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

    def __init__(self, domain=DEFAULT_DOMAIN, locale=None, context=None, **kwargs):
        super().__init__(**kwargs)
        self.domain = domain
        self.locale = locale
        self.context = context

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
        **kwargs
    ):
        super().__init__(**kwargs)
        self.domain = domain
        self.start_page = start_page
        self.pages = pages
        self.locale = locale

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
        **kwargs
    ):
        super().__init__(**kwargs)
        self.domain = domain
        self.start_page = start_page
        self.pages = pages
        self.locale = locale

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

    def __init__(self, domain=DEFAULT_DOMAIN, locale=None, **kwargs):
        super().__init__(**kwargs)
        self.domain = domain
        self.locale = locale

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
        **kwargs
    ):
        super().__init__(**kwargs)
        self.domain = domain
        self.start_page = start_page
        self.pages = pages
        self.locale = locale

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

    def __init__(self, domain=DEFAULT_DOMAIN, locale=None, **kwargs):
        super().__init__(**kwargs)
        self.domain = domain
        self.locale = locale

    def check_parameter_validity(self):
        """
        Checks the validity of AmazonSellerOpts parameters.
        """
        utils.check_user_agent_validity(self.user_agent_type)
        utils.check_render_validity(self.render)


class AmazonBase:
    def _prepare_search_payload(self, query, opts):
        opts = AmazonSearchOpts(**opts if opts is not None else {})

        # Set defaults and check validity
        opts.domain = set_default_domain(opts.domain)
        opts.start_page = set_default_start_page(opts.start_page)
        opts.pages = set_default_pages(opts.pages)
        opts.user_agent_type = set_default_user_agent(opts.user_agent_type)

        opts.check_parameter_validity()

        payload = {
            "source": Source.AmazonSearch.value,
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
        }

        if opts.parse_instructions is not None:
            payload["parsing_instructions"] = opts.parse_instructions
            payload["parse"] = True

        return payload

    def _prepare_url_payload(self, url, opts):
        validate_url(url, "amazon")
        opts = AmazonUrlOpts(**opts if opts is not None else {})

        # Set defaults and check validity
        opts.user_agent_type = set_default_user_agent(opts.user_agent_type)
        opts.check_parameter_validity()

        payload = {
            "source": Source.AmazonUrl.value,
            "url": url,
            "user_agent_type": opts.user_agent_type,
            "locale": opts.locale,
            "render": opts.render,
            "callback_url": opts.callback_url,
            "geo_location": opts.geo_location,
        }

        if opts.parse_instructions is not None:
            payload["parsing_instructions"] = opts.parse_instructions
            payload["parse"] = True

        return payload

    def _prepare_product_payload(self, query, opts):
        opts = AmazonProductOpts(**opts if opts is not None else {})

        opts.domain = set_default_domain(opts.domain)
        opts.user_agent_type = set_default_user_agent(opts.user_agent_type)

        opts.check_parameter_validity()

        payload = {
            "source": Source.AmazonProduct.value,
            "domain": opts.domain,
            "query": query,
            "geo_location": opts.geo_location,
            "user_agent_type": opts.user_agent_type,
            "locale": opts.locale,
            "render": opts.render,
            "callback_url": opts.callback_url,
            "context": opts.context,
        }

        if opts.parse_instructions is not None:
            payload["parsing_instructions"] = opts.parse_instructions
            payload["parse"] = True

        return payload

    def _prepare_pricing_payload(self, query, opts):
        opts = AmazonPricingOpts(**opts if opts is not None else {})

        opts.domain = set_default_domain(opts.domain)
        opts.start_page = set_default_start_page(opts.start_page)
        opts.pages = set_default_pages(opts.pages)
        opts.user_agent_type = set_default_user_agent(opts.user_agent_type)

        opts.check_parameter_validity()

        payload = {
            "source": Source.AmazonPricing.value,
            "domain": opts.domain,
            "query": query,
            "start_page": opts.start_page,
            "pages": opts.pages,
            "geo_location": opts.geo_location,
            "user_agent_type": opts.user_agent_type,
            "locale": opts.locale,
            "render": opts.render,
            "callback_url": opts.callback_url,
        }

        if opts.parse_instructions is not None:
            payload["parsing_instructions"] = opts.parse_instructions
            payload["parse"] = True

        return payload

    def _prepare_reviews_payload(self, query, opts):
        opts = AmazonReviewsOpts(**opts if opts is not None else {})

        opts.domain = set_default_domain(opts.domain)
        opts.start_page = set_default_start_page(opts.start_page)
        opts.pages = set_default_pages(opts.pages)
        opts.user_agent_type = set_default_user_agent(opts.user_agent_type)

        opts.check_parameter_validity()

        payload = {
            "source": Source.AmazonReviews.value,
            "domain": opts.domain,
            "query": query,
            "geo_location": opts.geo_location,
            "user_agent_type": opts.user_agent_type,
            "locale": opts.locale,
            "start_page": opts.start_page,
            "pages": opts.pages,
            "render": opts.render,
            "callback_url": opts.callback_url,
        }

        if opts.parse_instructions is not None:
            payload["parsing_instructions"] = opts.parse_instructions
            payload["parse"] = True

        return payload

    def _prepare_questions_payload(self, query, opts):
        opts = AmazonQuestionsOpts(**opts if opts is not None else {})

        opts.domain = set_default_domain(opts.domain)
        opts.user_agent_type = set_default_user_agent(opts.user_agent_type)

        opts.check_parameter_validity()

        payload = {
            "source": Source.AmazonQuestions.value,
            "domain": opts.domain,
            "query": query,
            "geo_location": opts.geo_location,
            "user_agent_type": opts.user_agent_type,
            "locale": opts.locale,
            "render": opts.render,
            "callback_url": opts.callback_url,
        }

        if opts.parse_instructions is not None:
            payload["parsing_instructions"] = opts.parse_instructions
            payload["parse"] = True

        return payload

    def _prepare_bestseller_payload(self, query, opts):
        opts = AmazonBestsellerOpts(**opts if opts is not None else {})

        opts.domain = set_default_domain(opts.domain)
        opts.start_page = set_default_start_page(opts.start_page)
        opts.pages = set_default_pages(opts.pages)
        opts.user_agent_type = set_default_user_agent(opts.user_agent_type)

        opts.check_parameter_validity()

        payload = {
            "source": Source.AmazonBestsellers.value,
            "domain": opts.domain,
            "query": query,
            "start_page": opts.start_page,
            "pages": opts.pages,
            "geo_location": opts.geo_location,
            "user_agent_type": opts.user_agent_type,
            "locale": opts.locale,
            "render": opts.render,
            "callback_url": opts.callback_url,
        }

        if opts.parse_instructions is not None:
            payload["parsing_instructions"] = opts.parse_instructions
            payload["parse"] = True

        return payload

    def _prepare_seller_payload(self, query, opts):
        opts = AmazonSellerOpts(**opts if opts is not None else {})

        opts.domain = set_default_domain(opts.domain)
        opts.user_agent_type = set_default_user_agent(opts.user_agent_type)

        opts.check_parameter_validity()

        payload = {
            "source": Source.AmazonSellers.value,
            "domain": opts.domain,
            "query": query,
            "geo_location": opts.geo_location,
            "user_agent_type": opts.user_agent_type,
            "locale": opts.locale,
            "render": opts.render,
            "callback_url": opts.callback_url,
        }

        if opts.parse_instructions is not None:
            payload["parsing_instructions"] = opts.parse_instructions
            payload["parse"] = True

        return payload
