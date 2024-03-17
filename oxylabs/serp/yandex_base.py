from oxylabs.utils.defaults import (
    DEFAULT_LIMIT_SERP,
    set_default_domain,
    set_default_limit,
    set_default_pages,
    set_default_start_page,
    set_default_user_agent,
)
from oxylabs.utils.utils import BaseSearchOpts, BaseUrlOpts, validate_url
from oxylabs.utils import source, domain, locale
import oxylabs.utils.utils as utils
from typing import Optional

YandexSearchAcceptedDomainParameters = [
    domain.COM,
    domain.RU,
    domain.UA,
    domain.BY,
    domain.KZ,
    domain.TR,
]

YandexSearchAcceptedLocaleParameters = [
    locale.EN,
    locale.RU,
    locale.BY,
    locale.DE,
    locale.FR,
    locale.ID,
    locale.KK,
    locale.TT,
    locale.TR,
    locale.UK,
]


class YandexSearchOpts(BaseSearchOpts):
    def __init__(
        self,
        locale: str = None,
        geo_location: str = None,
        **kwargs,
    ):
        """
        Initialize a YandexBase object.

        Args:
            locale (str, optional): The locale to be used for the Yandex search. Defaults to None.
            geo_location (str, optional): The geo location to be used for the Yandex search. Defaults to None.
            **kwargs: Additional keyword arguments to be passed to the parent class.

        """
        super().__init__(
            **kwargs,
        )
        self.locale = locale
        self.geo_location = geo_location

    def check_parameter_validity(self):
        """
        Checks the validity of YandexSearchOpts parameters.
        """
        utils.check_user_agent_validity(self.user_agent_type)
        utils.check_domain_validity(self.domain, YandexSearchAcceptedDomainParameters)
        utils.check_locale_validity(self.locale, YandexSearchAcceptedLocaleParameters)
        utils.check_limit_validity(self.limit)
        utils.check_pages_validity(self.pages)
        utils.check_start_page_validity(self.start_page)
        utils.check_parsing_instructions_validity(self.parsing_instructions)


class YandexUrlOpts(BaseUrlOpts):
    def __init__(
        self,
        render=None,
        **kwargs,
    ):
        super().__init__(**kwargs)
        self.render = render

    def check_parameter_validity(self):
        """
        Checks the validity of YandexUrlOpts parameters.
        """
        utils.check_render_validity(self.render)
        utils.check_parsing_instructions_validity(self.parsing_instructions)


class YandexBase:
    def _prepare_yandex_search_payload(
        self, query: str, user_opts: Optional[dict]
    ) -> dict:
        """
        Prepare the search payload for Yandex search.

        Args:
            query (str): The search query.
            opts (dict): The options for the search.

        Returns:
            dict: The prepared search payload.
        """
        opts = YandexSearchOpts(**user_opts if user_opts is not None else {})

        # Set defaults and check validity
        opts.domain = set_default_domain(opts.domain)
        opts.start_page = set_default_start_page(opts.start_page)
        opts.pages = set_default_pages(opts.pages)
        opts.limit = set_default_limit(opts.limit, DEFAULT_LIMIT_SERP)
        opts.user_agent_type = set_default_user_agent(opts.user_agent_type)
        opts.check_parameter_validity()

        payload = {
            "source": source.YANDEX_SEARCH,
            "domain": opts.domain,
            "query": query,
            "start_page": opts.start_page,
            "pages": opts.pages,
            "limit": opts.limit,
            "locale": opts.locale,
            "geo_location": opts.geo_location,
            "user_agent_type": opts.user_agent_type,
            "callback_url": opts.callback_url,
        }

        if opts.parsing_instructions is not None:
            payload["parsing_instructions"] = opts.parsing_instructions
            payload["parse"] = True

        return payload

    def _prepare_yandex_url_payload(self, url: str, user_opts: Optional[dict]) -> dict:
        """
        Prepare the payload for a Yandex URL request.

        Args:
            url (str): The URL to be queried.
            opts (dict): Optional parameters for the Yandex URL request.

        Returns:
            dict: The prepared payload for the Yandex URL request.
        """
        validate_url(url, "yandex")
        opts = YandexUrlOpts(**user_opts if user_opts is not None else {})

        # Set defaults and check validity
        opts.user_agent_type = set_default_user_agent(opts.user_agent_type)
        opts.check_parameter_validity()

        payload = {
            "source": source.YANDEX_URL,
            "url": url,
            "user_agent_type": opts.user_agent_type,
            "render": opts.render,
            "callback_url": opts.callback_url,
        }

        if opts.parsing_instructions is not None:
            payload["parsing_instructions"] = opts.parsing_instructions
            payload["parse"] = True

        return payload
