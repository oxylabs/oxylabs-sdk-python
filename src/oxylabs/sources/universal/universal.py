from typing import Optional

from oxylabs.internal.api import RealtimeAPI, AsyncAPI
from oxylabs.sources.response import Response
from oxylabs.utils.types import source
from oxylabs.utils.utils import (
    check_parsing_instructions_validity,
    prepare_config,
)


class Universal:
    def __init__(self, api_instance:RealtimeAPI) -> None:
        """
        Initializes an instance of the Universal class.

        Args:
            api_instance: An instance of the RealtimeAPI class used for making requests.
        """
        self._api_instance = api_instance

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
        browser_instructions: Optional[dict] = None,
        request_timeout: Optional[int] = 165,
        **kwargs
    ) -> Response:
        """
        Scrapes Universal search results for a given URL.

        Args:
            url (str): The URL to be scraped.
            user_agent_type (Optional[str]): Device type and browser.
            geo_location (Optional[str]): None,
            locale (Optional[str]): Accept-Language header value which changes page web interface language.
            render (Optional[str]): Enables JavaScript rendering.
            content_encoding:  Add this parameter if you are downloading images.
            context: Optional[list],
            callback_url (Optional[str]): URL to your callback endpoint.
            parse (Optional[bool]): true will return structured data.
            parser_type: Set the value to ecommerce_product to access our AI-powered Adaptive Parser.
            parsing_instructions (Optional[dict]): Instructions for parsing the results.
            browser_instructions (Optional[dict]): Browser instructions that are executed when rendering JavaScript.
            request_timeout (int | 165, optional): The interval in seconds for
                            the request to time out if no response is returned.
                            Defaults to 165.

        Returns:
            Response: The response from the server after the job is completed.
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
            "browser_instructions": browser_instructions,
            **kwargs,
        }
        check_parsing_instructions_validity(parsing_instructions)
        api_response = self._api_instance.get_response(payload, config)
        return Response(api_response)

class UniversalAsync:
    def __init__(self, api_instance:AsyncAPI) -> None:
        """
        Initializes an instance of the Universal class.

        Args:
            api_instance: An instance of the AsyncAPI class used for making requests.
        """
        self._api_instance = api_instance

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
        browser_instructions: Optional[dict] = None,
        request_timeout: Optional[int] = 165,
        job_completion_timeout: Optional[int] = None,
        poll_interval: Optional[int] = None,
        **kwargs
    ) -> Response:
        """
        Asynchronously scrapes Universal search results for a given URL.

        Args:
            url (str): The URL to be scraped.
            user_agent_type (Optional[str]): Device type and browser.
            geo_location (Optional[str]): None,
            locale (Optional[str]): Accept-Language header value which changes page web interface language.
            render (Optional[str]): Enables JavaScript rendering.
            content_encoding:  Add this parameter if you are downloading images.
            context: Optional[list],
            callback_url (Optional[str]): URL to your callback endpoint.
            parse (Optional[bool]): true will return structured data.
            parser_type: Set the value to ecommerce_product to access our AI-powered Adaptive Parser.
            parsing_instructions (Optional[dict]): Instructions for parsing the results.
            browser_instructions (Optional[dict]): Browser instructions that are executed when rendering JavaScript.
            request_timeout (int | 165, optional): The interval in seconds for
                            the request to time out if no response is returned.
                            Defaults to 165.
            poll_interval (Optional[int]): The interval in seconds to poll
                            the server for a response.
            job_completion_timeout (Optional[int]): The interval in
                            seconds for the job to time out if no response is returned.

        Returns:
            Response: The response from the server after the job is completed.
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
            "browser_instructions": browser_instructions,
            **kwargs,
        }
        check_parsing_instructions_validity(parsing_instructions)
        api_response = await self._api_instance.get_response(payload, config)
        return Response(api_response)
