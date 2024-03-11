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
    set_default_hotel_occupancy,
)
from utils.utils import BaseGoogleOpts, validate_url
from utils.constants import Source, Render
import utils.utils as utils


class GoogleSearchOpts(BaseGoogleOpts):
    def __init__(
        self,
        geo_location=None,
        user_agent_type=DEFAULT_USER_AGENT,
        render=None,
        callback_url=None,
        parsing_instructions=None,
        parse=False,
        context=None,
        domain=DEFAULT_DOMAIN,
        start_page=DEFAULT_START_PAGE,
        pages=DEFAULT_PAGES,
        limit=DEFAULT_LIMIT_SERP,
        locale=None,
    ):
        super().__init__(
            geo_location,
            user_agent_type,
            render,
            callback_url,
            parsing_instructions,
            parse,
            context,
        )
        self.domain = domain
        self.start_page = start_page
        self.pages = pages
        self.limit = limit
        self.locale = locale

    AcceptedTbmParameters = [
        "app",
        "bks",
        "isch",
        "nws",
        "pts",
        "vid",
    ]

    def check_parameter_validity(self):
        utils.check_user_agent_validity(self.user_agent_type)
        utils.check_render_validity(self.render)
        utils.check_limit_validity(self.limit)
        utils.check_pages_validity(self.pages)
        utils.check_start_page_validity(self.start_page)
        utils.check_parsing_instructions_validity(self.parsing_instructions)

        # check if tbm parameter is valid
        if self.context:
            for opt in self.context:
                if (
                    opt.get("key") == "tbm"
                    and opt.get("value") not in self.AcceptedTbmParameters
                ):
                    raise ValueError(
                        f"Invalid tbm parameter value: {opt.get('value')}. Accepted values are: {', '.join(self.AcceptedTbmParameters)}"
                    )


class GoogleUrlOpts(BaseGoogleOpts):

    def check_parameter_validity(self):
        utils.check_user_agent_validity(self.user_agent_type)
        utils.check_render_validity(self.render)
        utils.check_parsing_instructions_validity(self.parsing_instructions)


class GoogleAdsOpts(BaseGoogleOpts):
    def __init__(
        self,
        geo_location=None,
        user_agent_type=DEFAULT_USER_AGENT,
        render=None,
        callback_url=None,
        parsing_instructions=None,
        parse=False,
        context=None,
        domain=DEFAULT_DOMAIN,
        start_page=DEFAULT_START_PAGE,
        pages=DEFAULT_PAGES,
        limit=DEFAULT_LIMIT_SERP,
        locale=None,
    ):
        super().__init__(
            geo_location,
            user_agent_type,
            render,
            callback_url,
            parsing_instructions,
            parse,
            context,
        )
        self.domain = domain
        self.start_page = start_page
        self.pages = pages
        self.limit = limit
        self.locale = locale

    AcceptedTbmParameters = [
        "app",
        "bks",
        "isch",
        "nws",
        "pts",
        "vid",
    ]

    def check_parameter_validity(self):
        utils.check_user_agent_validity(self.user_agent_type)
        utils.check_render_validity(self.render)
        utils.check_start_page_validity(self.start_page)
        utils.check_parsing_instructions_validity(self.parsing_instructions)

        if self.context:
            for opt in self.context:
                if (
                    opt.get("key") == "tbm"
                    and opt.get("value") not in self.AcceptedTbmParameters
                ):
                    raise ValueError(
                        f"Invalid tbm parameter value: {opt.get('value')}. Accepted values are: {', '.join(self.AcceptedTbmParameters)}"
                    )


class GoogleSuggestionsOpts(BaseGoogleOpts):
    def __init__(
        self,
        geo_location=None,
        user_agent_type=DEFAULT_USER_AGENT,
        render=None,
        callback_url=None,
        parsing_instructions=None,
        parse=False,
        context=None,
        locale=None,
    ):
        super().__init__(
            geo_location,
            user_agent_type,
            render,
            callback_url,
            parsing_instructions,
            parse,
            context,
        )
        self.locale = locale

    def check_parameter_validity(self):
        utils.check_user_agent_validity(self.user_agent_type)
        utils.check_render_validity(self.render)
        utils.check_parsing_instructions_validity(self.parsing_instructions)


class GoogleHotelsOpts(BaseGoogleOpts):
    def __init__(
        self,
        geo_location=None,
        user_agent_type=DEFAULT_USER_AGENT,
        render=None,
        callback_url=None,
        parsing_instructions=None,
        parse=False,
        context=None,
        domain=DEFAULT_DOMAIN,
        start_page=DEFAULT_START_PAGE,
        pages=DEFAULT_PAGES,
        limit=DEFAULT_LIMIT_SERP,
        locale=None,
    ):
        super().__init__(
            geo_location,
            user_agent_type,
            render,
            callback_url,
            parsing_instructions,
            parse,
            context,
        )
        self.domain = domain
        self.start_page = start_page
        self.pages = pages
        self.limit = limit
        self.locale = locale

    def check_parameter_validity(self):
        utils.check_user_agent_validity(self.user_agent_type)
        utils.check_render_validity(self.render)
        utils.check_limit_validity(self.limit)
        utils.check_pages_validity(self.pages)
        utils.check_start_page_validity(self.start_page)
        utils.check_parsing_instructions_validity(self.parsing_instructions)


class GoogleTravelHotelsOpts(BaseGoogleOpts):
    def __init__(
        self,
        geo_location=None,
        user_agent_type=DEFAULT_USER_AGENT,
        render=None,
        callback_url=None,
        parsing_instructions=None,
        parse=False,
        context=None,
        domain=DEFAULT_DOMAIN,
        start_page=DEFAULT_START_PAGE,
        locale=None,
    ):
        super().__init__(
            geo_location,
            user_agent_type,
            render,
            callback_url,
            parsing_instructions,
            parse,
            context,
        )
        self.domain = domain
        self.start_page = start_page
        self.locale = locale

    def check_parameter_validity(self):
        utils.check_user_agent_validity(self.user_agent_type)
        utils.check_render_validity(self.render)
        utils.check_start_page_validity(self.start_page)
        utils.check_parsing_instructions_validity(self.parsing_instructions)


class GoogleImagesOpts(BaseGoogleOpts):
    def __init__(
        self,
        geo_location=None,
        user_agent_type=DEFAULT_USER_AGENT,
        render=None,
        callback_url=None,
        parsing_instructions=None,
        parse=False,
        context=None,
        domain=DEFAULT_DOMAIN,
        start_page=DEFAULT_START_PAGE,
        pages=DEFAULT_PAGES,
        limit=DEFAULT_LIMIT_SERP,
        locale=None,
    ):
        super().__init__(
            geo_location,
            user_agent_type,
            render,
            callback_url,
            parsing_instructions,
            parse,
            context,
        )
        self.domain = domain
        self.start_page = start_page
        self.pages = pages
        self.limit = limit
        self.locale = locale

    def check_parameter_validity(self):
        utils.check_render_validity(self.render)
        utils.check_start_page_validity(self.start_page)
        utils.check_parsing_instructions_validity(self.parsing_instructions)


class GoogleTrendsExploreOpts(BaseGoogleOpts):

    def check_parameter_validity(self):
        utils.check_user_agent_validity(self.user_agent_type)
        utils.check_parsing_instructions_validity(self.parsing_instructions)


class GoogleBase:
    def _prepare_search_payload(self, query, opts):
        opts = GoogleSearchOpts(**opts if opts is not None else {})

        if (
            (
                opts.limit is not None
                or opts.start_page is not None
                or opts.pages is not None
            )
            and opts.context
            and any(opt.get("key") == "limit_per_page" for opt in opts.context)
        ):
            raise ValueError(
                "limit, start_page, and pages parameters cannot be used together with limit_per_page context parameter"
            )

        # Set defaults and check validity
        opts.domain = set_default_domain(opts.domain)
        opts.start_page = set_default_start_page(opts.start_page)
        opts.limit = set_default_limit(opts.limit, DEFAULT_LIMIT_SERP)
        opts.pages = set_default_pages(opts.pages)
        opts.user_agent_type = set_default_user_agent(opts.user_agent_type)
        opts.check_parameter_validity()

        # Prepare payload
        payload = {
            "source": Source.GoogleSearch.value,
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

    def _prepare_url_payload(self, url, opts):
        validate_url(url, "google")
        opts = GoogleUrlOpts(**opts if opts is not None else {})

        # Set defaults and check validity
        opts.user_agent_type = set_default_user_agent(opts.user_agent_type)
        opts.check_parameter_validity()

        # Prepare payload
        payload = {
            "source": Source.GoogleUrl.value,
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

    def _prepare_ads_payload(self, query, opts):
        opts = GoogleAdsOpts(**opts if opts is not None else {})

        # Set defaults and check validity
        opts.domain = set_default_domain(opts.domain)
        opts.start_page = set_default_start_page(opts.start_page)
        opts.pages = set_default_pages(opts.pages)
        opts.user_agent_type = set_default_user_agent(opts.user_agent_type)
        opts.check_parameter_validity()

        # Prepare payload
        payload = {
            "source": Source.GoogleAds.value,
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

    def _prepare_suggestions_payload(self, query, opts):
        opts = GoogleSuggestionsOpts(**opts if opts is not None else {})

        # Set defaults and check validity
        opts.user_agent_type = set_default_user_agent(opts.user_agent_type)
        opts.check_parameter_validity()

        # Prepare payload
        payload = {
            "source": Source.GoogleSuggestions.value,
            "query": query,
            "locale": opts.locale,
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

    def _prepare_hotels_payload(self, query, opts):
        opts = GoogleHotelsOpts(**opts if opts is not None else {})

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
            "source": Source.GoogleHotels.value,
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
            "parse": opts.parse,
            "context": opts.context,
        }

        if opts.parsing_instructions is not None:
            payload["parsing_instructions"] = opts.parsing_instructions
            payload["parse"] = True

        return payload

    def _prepare_travel_hotels_payload(self, query, opts):
        opts = GoogleTravelHotelsOpts(**opts if opts is not None else {})

        # Set defaults and check validity
        opts.domain = set_default_domain(opts.domain)
        opts.start_page = set_default_start_page(opts.start_page)
        if opts.context:
            for item in opts.context:
                if item["key"] == "hotel_occupancy":
                    item["value"] = set_default_hotel_occupancy(item.get("value"))

        opts.check_parameter_validity()

        # Prepare payload
        payload = {
            "source": Source.GoogleTravelHotels.value,
            "domain": opts.domain,
            "query": query,
            "start_page": opts.start_page,
            "locale": opts.locale,
            "geo_location": opts.geo_location,
            "user_agent_type": opts.user_agent_type,
            "render": opts.render if opts.render else Render.HTML.value,
            "callback_url": opts.callback_url,
            "parse": opts.parse,
            "context": opts.context,
        }

        if opts.parsing_instructions is not None:
            payload["parsing_instructions"] = opts.parsing_instructions
            payload["parse"] = True

        return payload

    def _prepare_images_payload(self, query, opts):
        opts = GoogleImagesOpts(**opts if opts is not None else {})

        # Set defaults and check validity
        opts.user_agent_type = set_default_user_agent(opts.user_agent_type)
        opts.domain = set_default_domain(opts.domain)
        opts.start_page = set_default_start_page(opts.start_page)
        opts.pages = set_default_pages(opts.pages)
        opts.check_parameter_validity()

        # If context is None, initialize it as an empty list
        if opts.context is None:
            opts.context = []

        # Find the index of the dictionary with 'tbm' as key
        index = next(
            (index for (index, d) in enumerate(opts.context) if d["key"] == "tbm"), None
        )

        # If 'tbm' key exists, update its value to 'isch'
        if index is not None:
            opts.context[index]["value"] = "isch"
        # If 'tbm' key doesn't exist, add it to the context with value 'isch'
        else:
            opts.context.append({"key": "tbm", "value": "isch"})

        # Prepare payload
        payload = {
            "source": Source.GoogleSearch.value,
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

    def _prepare_trends_explore_payload(self, query, opts):
        opts = GoogleTrendsExploreOpts(**opts if opts is not None else {})

        # Set defaults and check validity
        opts.user_agent_type = set_default_user_agent(opts.user_agent_type)
        opts.check_parameter_validity()

        # Prepare payload
        payload = {
            "source": Source.GoogleTrendsExplore.value,
            "query": query,
            "geo_location": opts.geo_location,
            "context": opts.context,
            "user_agent_type": opts.user_agent_type,
            "callback_url": opts.callback_url,
            "parse": opts.parse,
        }

        if opts.parsing_instructions is not None:
            payload["parsing_instructions"] = opts.parsing_instructions
            payload["parse"] = True

        return payload
