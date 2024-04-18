from oxylabs.utils.defaults import (
    set_default_user_agent,
    set_default_http_method,
    set_default_content_encoding,
)
from oxylabs.utils.utils import BaseUrlOpts
from oxylabs.utils import source
import oxylabs.utils.utils as utils
from typing import Optional, Dict, Any


class UniversalUrlOpts(BaseUrlOpts):
    """
    Represents the search options for Universal.
    """

    def __init__(
        self,
        geo_location=None,
        locale=None,
        render=None,
        content_encoding="base64",
        context=None,
        parser_type=None,
        parse=None,
        **kwargs,
    ):
        super().__init__(**kwargs)
        self.geo_location = geo_location
        self.locale = locale
        self.render = render
        self.content_encoding = content_encoding
        self.context = context
        self.parser_type = parser_type
        self.parse = parse

    def check_parameter_validity(self):
        """
        Checks the validity of UniversalUrlOpts parameters.
        """
        utils.check_user_agent_validity(self.user_agent_type)
        utils.check_render_validity(self.render)
        utils.check_http_method_validity(self.context)
        utils.check_content_for_post_validity(self.context)


class UniversalBase:
    def _prepare_universal_url_payload(
        self, url: str, user_opts: Optional[dict] = None
    ) -> dict:
        """
        Prepares the payload for a URL request.

        Args:
            url (str): The URL to be requested.
            user_opts (dict): Optional user-defined options.

        Returns:
            dict: The prepared payload.

        Raises:
            ValueError: If any of the options are invalid.
        """

        opts = UniversalUrlOpts(**user_opts if user_opts is not None else {})

        opts.context = set_default_http_method(opts.context)
        opts.content_encoding = set_default_content_encoding(opts.content_encoding)

        opts.check_parameter_validity()

        payload = {
            "source": source.UNIVERSAL,
            "url": url,
            "user_agent_type": opts.user_agent_type,
            "geo_location": opts.geo_location,
            "locale": opts.locale,
            "render": opts.render,
            "content_encoding": opts.content_encoding,
            "context": opts.context,
            "callback_url": opts.callback_url,
            "parse": opts.parse,
            "parser_type": opts.parser_type,
        }

        payload["parse"] = (
            True if opts.parsing_instructions or opts.parser_type else opts.parse
        )

        if opts.parsing_instructions:
            payload["parsing_instructions"] = opts.parsing_instructions

        return payload
