from typing import Optional

from oxylabs.internal.api import RealtimeAPI, AsyncAPI
from oxylabs.sources.response import Response
from oxylabs.utils.types import source
from oxylabs.utils.utils import (
    check_parsing_instructions_validity,
    prepare_config,
)


class Bing:
    def __init__(self, api_instance:RealtimeAPI) -> None:
        """
        Initializes an instance of the Bing class.

        Args:
            api_instance: An instance of the RealtimeAPI class used for making requests.
        """
        self._api_instance = api_instance

    def scrape_search(
        self,
        query: str,
        domain: Optional[str] = None,
        start_page: Optional[int] = None,
        pages: Optional[int] = None,
        limit: Optional[int] = None,
        user_agent_type: Optional[str] = None,
        callback_url: Optional[str] = None,
        locale: Optional[str] = None,
        geo_location: Optional[str] = None,
        render: Optional[str] = None,
        parse: Optional[bool] = None,
        parsing_instructions: Optional[dict] = None,
        request_timeout: Optional[int] = 165,
        **kwargs,
    ) -> Response:
        """
        Scrapes search results from Bing.

        Args:
            query (str): UTF-encoded keyword.
            domain (Optional[str]): The domain to limit the search results to.
            start_page (Optional[int]): The starting page number.
            pages (Optional[int]): The number of pages to scrape.
            limit (Optional[int]): Number of results to retrieve in each page.
            user_agent_type (Optional[str]): Device type and browser.
            callback_url (Optional[str]): URL to your callback endpoint.
            locale (Optional[str]): Accept-Language header value which changes page web interface language.
            geo_location (Optional[str]):  It goes like this: City,Region,Country.
            render (Optional[str]): Enables JavaScript rendering.
            parse (Optional[bool]): true will return structured data.
            parsing_instructions (Optional[dict]): Instructions for parsing the results.
            request_timeout (Optional[int]): The timeout for the request in seconds.
            **kwargs: Additional keyword arguments.
        Returns:
            Response: The response containing the scraped results.
        """

        config = prepare_config(request_timeout=request_timeout)
        payload = {
            "source": source.BING_SEARCH,
            "domain": domain,
            "query": query,
            "start_page": start_page,
            "pages": pages,
            "limit": limit,
            "locale": locale,
            "geo_location": geo_location,
            "user_agent_type": user_agent_type,
            "callback_url": callback_url,
            "render": render,
            "parse": parse,
            "parsing_instructions": parsing_instructions,
            **kwargs,
        }

        check_parsing_instructions_validity(parsing_instructions)
        api_response = self._api_instance.get_response(payload, config)
        return Response(api_response)

    def scrape_url(
        self,
        url: str,
        user_agent_type: Optional[str] = None,
        geo_location: Optional[str] = None,
        callback_url: Optional[str] = None,
        render: Optional[str] = None,
        parse: Optional[bool] = None,
        parsing_instructions: Optional[dict] = None,
        request_timeout: Optional[int] = 165,
        **kwargs,
    ) -> Response:
        """
        Scrapes Bing search results for a given URL.

        Args:
            url (str): The URL to be scraped.
            user_agent_type (Optional[str]): Device type and browser.
            geo_location (Optional[str]): The API uses Canonical Geo Location format to
                            determine request location. It goes like this: City,Region,Country
            callback_url (Optional[str]): URL to your callback endpoint.
            render (Optional[str]): Enables JavaScript rendering.
            parsing_instructions (Optional[dict]): Instructions for parsing the results.
            parse (Optional[bool]): true will return structured data.
            request_timeout (int | 165, optional): The interval in seconds for
                            the request to time out if no response is returned.
                            Defaults to 165.

        Returns:
            Response: The response containing the scraped results.
        """

        config = prepare_config(request_timeout=request_timeout)
        payload = {
            "source": source.BING_URL,
            "url": url,
            "user_agent_type": user_agent_type,
            "geo_location": geo_location,
            "callback_url": callback_url,
            "render": render,
            "parse": parse,
            "parsing_instructions": parsing_instructions,
            **kwargs,
        }
        check_parsing_instructions_validity(parsing_instructions)
        api_response = self._api_instance.get_response(payload, config)
        return Response(api_response)


class BingAsync:
    def __init__(self, api_instance:AsyncAPI) -> None:
        """
        Initializes an instance of the Bing class.

        Args:
            api_instance: An instance of the AsyncAPI class used for making requests.
        """
        self._api_instance = api_instance

    async def scrape_search(
        self,
        query: str,
        domain: Optional[str] = None,
        start_page: Optional[int] = None,
        pages: Optional[int] = None,
        limit: Optional[int] = None,
        user_agent_type: Optional[str] = None,
        callback_url: Optional[str] = None,
        locale: Optional[str] = None,
        geo_location: Optional[str] = None,
        render: Optional[str] = None,
        parse: Optional[bool] = None,
        parsing_instructions: Optional[dict] = None,
        request_timeout: Optional[int] = 165,
        job_completion_timeout: Optional[int] = None,
        poll_interval: Optional[int] = None,
        **kwargs,
    ) -> Response:
        """
        Asynchronously scrapes Bing search results for a given query.

        Args:
            query (str): The search query.
            domain (Optional[str]): The domain to limit the search results to.
            start_page (Optional[int]): The starting page number.
            pages (Optional[int]): The number of pages to scrape.
            limit (Optional[int]): Number of results to retrieve in each page.
            user_agent_type (Optional[str]): Device type and browser.
            callback_url (Optional[str]): URL to your callback endpoint.
            locale (Optional[str]): Accept-Language header value which changes page web interface language.
            geo_location (Optional[str]): The API uses Canonical Geo Location format to
                            determine request location. It goes like this: City,Region,Country
            render (Optional[str]): Enables JavaScript rendering.
            parse (Optional[bool]): true will return structured data.
            request_timeout (int | 165, optional): The interval in seconds for
                            the request to time out if no response is returned.
                            Defaults to 165.
            poll_interval (Optional[int]): The interval in seconds to poll
                            the server for a response.
            job_completion_timeout (Optional[int]): The interval in
                            seconds for the job to time out if no response is returned.

        Returns:
            Response: The response containing the scraped results.
        """

        config = prepare_config(
            request_timeout=request_timeout,
            poll_interval=poll_interval,
            job_completion_timeout=job_completion_timeout,
            async_integration=True,
        )

        payload = {
            "source": source.BING_SEARCH,
            "domain": domain,
            "query": query,
            "start_page": start_page,
            "pages": pages,
            "limit": limit,
            "locale": locale,
            "geo_location": geo_location,
            "user_agent_type": user_agent_type,
            "callback_url": callback_url,
            "render": render,
            "parse": parse,
            "parsing_instructions": parsing_instructions,
            **kwargs,
        }
        check_parsing_instructions_validity(parsing_instructions)
        api_response = await self._api_instance.get_response(payload, config)
        return Response(api_response)

    async def scrape_url(
        self,
        url: str,
        user_agent_type: Optional[str] = None,
        geo_location: Optional[str] = None,
        callback_url: Optional[str] = None,
        render: Optional[str] = None,
        parse: Optional[bool] = None,
        parsing_instructions: Optional[dict] = None,
        request_timeout: Optional[int] = 165,
        job_completion_timeout: Optional[int] = None,
        poll_interval: Optional[int] = None,
        **kwargs,
    ) -> Response:
        """
        Asynchronously scrapes Bing search results for a given URL.

        Args:
            url (str): The URL to be scraped.

            user_agent_type (Optional[str]): Device type and browser.
            geo_location (Optional[str]): The API uses Canonical Geo Location format to
                            determine request location. It goes like this: City,Region,Country
            callback_url (Optional[str]): URL to your callback endpoint.
            render (Optional[str]): Enables JavaScript rendering.
            parsing_instructions (Optional[dict]): Instructions for parsing the results.
            parse (Optional[bool]): true will return structured data.
            request_timeout (int | 165, optional): The interval in seconds for
                            the request to time out if no response is returned.
                            Defaults to 165.
            poll_interval (Optional[int]): The interval in seconds to poll
                            the server for a response.
            job_completion_timeout (Optional[int]): The interval in
                            seconds for the job to time out if no response is returned.

        Returns:
            Response: The response containing the scraped results.
        """

        config = prepare_config(
            request_timeout=request_timeout,
            poll_interval=poll_interval,
            job_completion_timeout=job_completion_timeout,
            async_integration=True,
        )

        payload = {
            "source": source.BING_URL,
            "url": url,
            "user_agent_type": user_agent_type,
            "geo_location": geo_location,
            "callback_url": callback_url,
            "render": render,
            "parse": parse,
            "parsing_instructions": parsing_instructions,
        }
        check_parsing_instructions_validity(parsing_instructions)
        api_response = await self._api_instance.get_response(payload, config)
        return Response(api_response)
