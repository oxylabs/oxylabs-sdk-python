from typing import Optional

from src.oxylabs.sources.ecommerce.response import EcommerceResponse
from src.oxylabs.utils.types import source
from src.oxylabs.utils.utils import (
    check_parsing_instructions_validity,
    prepare_config,
)

from .universal_base import UniversalBase


class Universal(UniversalBase):
    def __init__(self, ecommerce_instance) -> None:
        """
        Initializes an instance of the Universal class.

        Args:
            ecommerce_instance: The Ecommerce instance associated with the Universal class.
        """
        self._ecommerce_instance = ecommerce_instance

    def scrape_url(
        self,
        url: str,
        user_agent_type: Optional[str] = None,
        geo_location: Optional[str] = None,
        locale: Optional[str] = None,
        render: Optional[str] = None,
        content_encoding: Optional[str] = None,
        context: Optional[list] = None,
        callback_url: Optional[str] = None,
        parse: Optional[bool] = None,
        parser_type: Optional[str] = None,
        parsing_instructions: Optional[dict] = None,
        request_timeout: int = None,
        **kwargs
    ) -> EcommerceResponse:
        """
        Scrapes Universal search results for a given URL.

        Args:
            url (str): The URL to be scraped.
            opts (UniversalUrlOpts, optional): Configuration options for the search. Defaults to:
                {
                    "user_agent_type": desktop,
                    "geo_location": None,
                    "locale": None,
                    "render": None,
                    "content_encoding": "base64",
                    "context": None,
                    "callback_url": None,
                    "parse": None,
                    "parser_type": None,
                    "parsing_instructions": None,
                }
                This parameter allows customization of the search request.
            request_timeout (int | 165, optional): The interval in seconds for
            the request to time out if no response is returned.
            Defaults to 165.

        Returns:
            dict: The response from the server after the job is completed.
        """

        config = prepare_config(request_timeout=request_timeout)
        payload = {
            "source": source.UNIVERSAL,
            "url": url,
            "user_agent_type": user_agent_type,
            "geo_location": geo_location,
            "locale": locale,
            "render": render,
            "content_encoding": content_encoding,
            "context": context,
            "callback_url": callback_url,
            "parse": parse,
            "parser_type": parser_type,
            "parsing_instructions": parsing_instructions,
            **kwargs,
        }
        check_parsing_instructions_validity(parsing_instructions)
        response = self._ecommerce_instance._get_resp(payload, config)
        return response


class UniversalAsync(UniversalBase):
    def __init__(self, ecommerce_async_instance) -> None:
        """
        Initializes an instance of the UniversalAsync class.

        Args:
            ecommerce_async_instance: The EcommerceAsync instance associated with the UniversalAsync class.
        """
        self._ecommerce_async_instance = ecommerce_async_instance

    async def scrape_url(
        self,
        url: str,
        user_agent_type: Optional[str] = None,
        geo_location: Optional[str] = None,
        locale: Optional[str] = None,
        render: Optional[str] = None,
        content_encoding: Optional[str] = None,
        context: Optional[list] = None,
        callback_url: Optional[str] = None,
        parse: Optional[bool] = None,
        parser_type: Optional[str] = None,
        parsing_instructions: Optional[dict] = None,
        request_timeout: int = None,
        job_completion_timeout: int = None,
        poll_interval: int = None,
        **kwargs
    ) -> EcommerceResponse:
        """
        Asynchronously scrapes Universal search results for a given URL.

        Args:
            url (str): The URL to be scraped.
            opts (UniversalUrlOpts, optional): Configuration options for the search. Defaults to:
                {
                    "user_agent_type": desktop,
                    "geo_location": None,
                    "locale": None,
                    "render": None,
                    "content_encoding": "base64",
                    "context": None,
                    "callback_url": None,
                    "parse": None,
                    "parser_type": None,
                    "parsing_instructions": None,
                }
                This parameter allows customization of the search request.
            request_timeout (int | 165, optional): The interval in seconds for
            the request to time out if no response is returned.
            Defaults to 165.
            poll_interval (int | 5, optional): The interval in seconds to poll
            the server for a response. Defaults to 5
            job_completion_timeout (int | 50, optional): The interval in
            seconds for the job to time out if no response is returned.
            Defaults to 50.

        Returns:
            dict: The response from the server after the job is completed.
        """

        config = prepare_config(
            request_timeout=request_timeout,
            poll_interval=poll_interval,
            job_completion_timeout=job_completion_timeout,
            async_integration=True,
        )
        payload = {
            "source": source.UNIVERSAL,
            "url": url,
            "user_agent_type": user_agent_type,
            "geo_location": geo_location,
            "locale": locale,
            "render": render,
            "content_encoding": content_encoding,
            "context": context,
            "callback_url": callback_url,
            "parse": parse,
            "parser_type": parser_type,
            "parsing_instructions": parsing_instructions,
            **kwargs,
        }
        check_parsing_instructions_validity(parsing_instructions)
        response = await self._ecommerce_async_instance._get_resp(
            payload, config
        )
        return response
