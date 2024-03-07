from utils.defaults import (
    DEFAULT_USER_AGENT,
    set_default_user_agent,
    set_default_http_method,
    set_default_content_encoding,
)
from utils.utils import BaseUrlOpts
from utils.constants import Source
import utils.utils as utils


class UniversalUrlOpts(BaseUrlOpts):
    """
    Represents the search options for Universal.
    """

    def __init__(
        self,
        user_agent_type=DEFAULT_USER_AGENT,
        geo_location=None,
        locale=None,
        render=None,
        content_encoding="base64",
        context=None,
        callback_url=None,
        parse=False,
        parser_type=None,
        parse_instructions=None,
    ):
        super().__init__(user_agent_type, callback_url, parse_instructions, parse)
        self.geo_location = geo_location
        self.locale = locale
        self.render = render
        self.content_encoding = content_encoding
        self.context = context
        self.parser_type = parser_type

    def check_parameter_validity(self):
        """
        Checks the validity of UniversalUrlOpts parameters.
        """
        utils.check_user_agent_validity(self.user_agent_type)
        utils.check_render_validity(self.render)

        if self.context and not any(
            d.get("key") == "http_method" and d.get("value") in ["post", "get"]
            for d in self.context
        ):
            raise ValueError("Invalid http method in context")

        if (
            self.context
            # and self.context.get("content") is not None
            # and self.context.get("http_method") != "post"
            and any(d.get("key") == "content" for d in self.context)
            and not any(
                d.get("key") == "http_method" and d.get("value") == "post"
                for d in self.context
            )
        ):
            raise ValueError("Content is only allowed for POST requests")


class UniversalBase:
    def _prepare_url_payload(self, url, opts):

        opts = UniversalUrlOpts(**opts if opts is not None else {})

        opts.user_agent_type = set_default_user_agent(opts.user_agent_type)
        opts.context = set_default_http_method(opts.context)
        opts.content_encoding = set_default_content_encoding(opts.content_encoding)

        opts.check_parameter_validity()

        payload = {
            "source": Source.Universal.value,
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

        if opts.parse_instructions:
            payload["parse"] = True
            payload["parse_instructions"] = opts.parse_instructions

        return payload
