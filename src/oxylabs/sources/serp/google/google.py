from typing import Optional

from oxylabs.sources.serp.response import SERPResponse
from oxylabs.utils.types import source
from oxylabs.utils.utils import (
    check_parsing_instructions_validity,
    prepare_config,
)


class Google:
    def __init__(self, serp_instance) -> None:
        """
        Initializes an instance of the Google class.

        Args:
            serp_instance: The SERP instance associated with the Google class.
        """
        self._serp_instance = serp_instance

    def scrape_search(
        self,
        query: str,
        domain: Optional[str] = None,
        start_page: Optional[int] = None,
        pages: Optional[int] = None,
        limit: Optional[int] = None,
        locale: Optional[str] = None,
        geo_location: Optional[str] = None,
        user_agent_type: Optional[str] = None,
        render: Optional[str] = None,
        callback_url: Optional[str] = None,
        parse: Optional[bool] = None,
        parsing_instructions: Optional[dict] = None,
        context: Optional[list] = None,
        request_timeout: Optional[int] = 165,
        **kwargs,
    ) -> SERPResponse:
        """
        Scrapes Google search results for a given query.

        Args:
            query (str): The search query.
            domain (Optional[str]): The domain to limit the search results to.
            start_page (Optional[int]): The starting page number.
                        pages (Optional[int]): The number of pages to scrape.
            limit (Optional[int]): Number of results to retrieve in each page.
            user_agent_type (Optional[str]): Device type and browser.
            locale (Optional[str]): Accept-Language header value which changes your Bing search 
                            page web interface language.
            geo_location (Optional[str]): None,
            render (Optional[str]): Enables JavaScript rendering.
            callback_url (Optional[str]): URL to your callback endpoint.
            parse (Optional[bool]): true will return structured data.
            context: Optional[list],
            parsing_instructions (Optional[dict]): Instructions for parsing the results.
            request_timeout (int | 165, optional): The interval in seconds for
            the request to time out if no response is returned.
            Defaults to 165.

        Returns:
            SERPResponse: The response from the server after the job is completed.
        """

        config = prepare_config(request_timeout=request_timeout)
        payload = {
            "source": source.GOOGLE_SEARCH,
            "query": query,
            "domain": domain,
            "start_page": start_page,
            "pages": pages,
            "limit": limit,
            "locale": locale,
            "geo_location": geo_location,
            "user_agent_type": user_agent_type,
            "render": render,
            "callback_url": callback_url,
            "parse": parse,
            "context": context,
            "parsing_instructions": parsing_instructions,
            **kwargs,
        }
        check_parsing_instructions_validity(parsing_instructions)
        response = self._serp_instance._get_resp(payload, config)
        return response

    def scrape_url(
        self,
        url: str,
        user_agent_type: Optional[str] = None,
        render: Optional[str] = None,
        callback_url: Optional[str] = None,
        geo_location: Optional[str] = None,
        parse: Optional[bool] = None,
        parsing_instructions: Optional[dict] = None,
        request_timeout: Optional[int] = 165,
        **kwargs,
    ) -> SERPResponse:
        """
        Scrapes Google search results for a given URL.

        Args:
            url (str): The URL to be scraped.
            user_agent_type (Optional[str]): Device type and browser.
            callback_url (Optional[str]): URL to your callback endpoint.
            render (Optional[str]): Enables JavaScript rendering.
            geo_location (Optional[str]): None,
            parse (Optional[bool]): true will return structured data.
            parsing_instructions (Optional[dict]): Instructions for parsing the results.
            request_timeout (int | 165, optional): The interval in seconds for
            the request to time out if no response is returned.
            Defaults to 165.

        Returns:
            SERPResponse: The response from the server after the job is completed.
        """

        config = prepare_config(request_timeout=request_timeout)
        payload = {
            "source": source.GOOGLE_URL,
            "url": url,
            "user_agent_type": user_agent_type,
            "render": render,
            "callback_url": callback_url,
            "geo_location": geo_location,
            "parse": parse,
            "parsing_instructions": parsing_instructions,
            **kwargs,
        }
        check_parsing_instructions_validity(parsing_instructions)

        response = self._serp_instance._get_resp(payload, config)
        return response

    def scrape_ads(
        self,
        query: str,
        domain: Optional[str] = None,
        start_page: Optional[int] = None,
        pages: Optional[int] = None,
        locale: Optional[str] = None,
        geo_location: Optional[str] = None,
        user_agent_type: Optional[str] = None,
        render: Optional[str] = None,
        callback_url: Optional[str] = None,
        parse: Optional[bool] = None,
        parsing_instructions: Optional[dict] = None,
        context: Optional[list] = None,
        request_timeout: Optional[int] = 165,
        **kwargs,
    ) -> SERPResponse:
        """
        Scrapes Google Ads search results for a given query.

        Args:
            query (str): The search query.
            domain (Optional[str]): The domain to limit the search results to.
            start_page (Optional[int]): The starting page number.
            pages (Optional[int]): The number of pages to scrape.
            user_agent_type (Optional[str]): Device type and browser.
            locale (Optional[str]): Accept-Language header value which changes your Bing search 
                            page web interface language.
            geo_location (Optional[str]): None,
            render (Optional[str]): Enables JavaScript rendering.
            callback_url (Optional[str]): URL to your callback endpoint.
            parse (Optional[bool]): true will return structured data.
            context: Optional[list],
            parsing_instructions (Optional[dict]): Instructions for parsing the results.
            request_timeout (int | 165, optional): The interval in seconds for
            the request to time out if no response is returned.
            Defaults to 165.

        Returns:
            SERPResponse: The response from the server after the job is completed.
        """

        config = prepare_config(request_timeout=request_timeout)
        payload = {
            "source": source.GOOGLE_ADS,
            "query": query,
            "domain": domain,
            "start_page": start_page,
            "pages": pages,
            "locale": locale,
            "geo_location": geo_location,
            "user_agent_type": user_agent_type,
            "render": render,
            "callback_url": callback_url,
            "parse": parse,
            "parsing_instructions": parsing_instructions,
            "context": context,
            **kwargs,
        }
        check_parsing_instructions_validity(parsing_instructions)
        response = self._serp_instance._get_resp(payload, config)
        return response

    def scrape_suggestions(
        self,
        query: str,
        locale: Optional[str] = None,
        geo_location: Optional[str] = None,
        user_agent_type: Optional[str] = None,
        render: Optional[str] = None,
        callback_url: Optional[str] = None,
        request_timeout: Optional[int] = 165,
        **kwargs,
    ) -> SERPResponse:
        """
        Scrapes Google suggestions for a given query.

        Args:
            query (str): The search query.
            locale (Optional[str]): Accept-Language header value which changes your Bing search 
                            page web interface language.
            geo_location (Optional[str]): None,
            user_agent_type (Optional[str]): Device type and browser.
            render (Optional[str]): Enables JavaScript rendering.
            callback_url (Optional[str]): URL to your callback endpoint.
            parsing_instructions (Optional[dict]): Instructions for parsing the results.
            request_timeout (int | 165, optional): The interval in seconds for
            the request to time out if no response is returned.
            Defaults to 165.

        Returns:
            SERPResponse: The response from the server after the job is completed.
        """

        config = prepare_config(request_timeout=request_timeout)
        payload = {
            "source": source.GOOGLE_SUGGESTIONS,
            "query": query,
            "locale": locale,
            "geo_location": geo_location,
            "user_agent_type": user_agent_type,
            "render": render,
            "callback_url": callback_url,
            **kwargs,
        }
        response = self._serp_instance._get_resp(payload, config)
        return response

    def scrape_hotels(
        self,
        query: str,
        domain: Optional[str] = None,
        start_page: Optional[int] = None,
        pages: Optional[int] = None,
        limit: Optional[int] = None,
        locale: Optional[str] = None,
        geo_location: Optional[str] = None,
        user_agent_type: Optional[str] = None,
        render: Optional[str] = None,
        callback_url: Optional[str] = None,
        context: Optional[list] = None,
        request_timeout: Optional[int] = 165,
        **kwargs,
    ) -> SERPResponse:
        """
        Scrapes Google Hotels search results for a given query.

        Args:
            query (str): The search query.
            domain (Optional[str]): The domain to limit the search results to.
            start_page (Optional[int]): The starting page number.
            pages (Optional[int]): The number of pages to scrape.
            limit (Optional[int]): Number of results to retrieve in each page.
            user_agent_type (Optional[str]): Device type and browser.
            locale (Optional[str]): Accept-Language header value which changes your Bing search 
                            page web interface language.
            geo_location (Optional[str]): None,
            render (Optional[str]): Enables JavaScript rendering.
            callback_url (Optional[str]): URL to your callback endpoint.
            context: Optional[list],
            parsing_instructions (Optional[dict]): Instructions for parsing the results.
            request_timeout (int | 165, optional): The interval in seconds for
            the request to time out if no response is returned.
            Defaults to 165.

        Returns:
            SERPResponse: The response from the server after the job is completed.
        """

        config = prepare_config(request_timeout=request_timeout)
        payload = {
            "source": source.GOOGLE_HOTELS,
            "query": query,
            "domain": domain,
            "start_page": start_page,
            "pages": pages,
            "limit": limit,
            "locale": locale,
            "geo_location": geo_location,
            "user_agent_type": user_agent_type,
            "render": render,
            "callback_url": callback_url,
            "context": context,
            **kwargs,
        }
        response = self._serp_instance._get_resp(payload, config)
        return response

    def scrape_travel_hotels(
        self,
        query: str,
        domain: Optional[str] = None,
        start_page: Optional[int] = None,
        locale: Optional[str] = None,
        geo_location: Optional[str] = None,
        user_agent_type: Optional[str] = None,
        render: Optional[str] = None,
        callback_url: Optional[str] = None,
        context: Optional[list] = None,
        request_timeout: Optional[int] = 165,
        **kwargs,
    ) -> SERPResponse:
        """
        Scrapes Google Travel Hotels search results for a given query.

        Args:
            query (str): UTF-encoded keyword. "query": "hotels" will result
            list hotels in a given geo_location; "query": "hotels in
            <Location>" will result in a list hotels for <Location>. Eg hotels
            in Paris will list hotels in Paris, no matter what geo_location is
            given.
            domain (Optional[str]): The domain to limit the search results to.
            start_page (Optional[int]): The starting page number.
            locale (Optional[str]): Accept-Language header value which changes your Bing search 
                            page web interface language.
            geo_location (Optional[str]): None,
            user_agent_type (Optional[str]): Device type and browser.
            render (Optional[str]): Enables JavaScript rendering.
            callback_url (Optional[str]): URL to your callback endpoint.
            context: Optional[list],
            parsing_instructions (Optional[dict]): Instructions for parsing the results.
            request_timeout (int | 165, optional): The interval in seconds for
            the request to time out if no response is returned.
            Defaults to 165.

        Returns:
            SERPResponse: The response from the server after the job is completed.
        """

        config = prepare_config(request_timeout=request_timeout)
        payload = {
            "source": source.GOOGLE_TRAVEL_HOTELS,
            "query": query,
            "domain": domain,
            "start_page": start_page,
            "locale": locale,
            "geo_location": geo_location,
            "user_agent_type": user_agent_type,
            "render": render,
            "callback_url": callback_url,
            "context": context,
            **kwargs,
        }
        response = self._serp_instance._get_resp(payload, config)
        return response

    def scrape_images(
        self,
        query: str,
        domain: Optional[str] = None,
        start_page: Optional[int] = None,
        pages: Optional[int] = None,
        locale: Optional[str] = None,
        geo_location: Optional[str] = None,
        user_agent_type: Optional[str] = None,
        render: Optional[str] = None,
        callback_url: Optional[str] = None,
        parse: Optional[bool] = None,
        parsing_instructions: Optional[dict] = None,
        context: Optional[list] = None,
        request_timeout: Optional[int] = 165,
        **kwargs,
    ) -> SERPResponse:
        """
        Scrapes Google Images search results for a given query.

        Args:
            query (str): The search query.
            domain (Optional[str]): The domain to limit the search results to.
            start_page (Optional[int]): The starting page number.
            pages (Optional[int]): The number of pages to scrape.
            user_agent_type (Optional[str]): Device type and browser.
            locale (Optional[str]): Accept-Language header value which changes your Bing search 
                            page web interface language.
            geo_location (Optional[str]): None,
            render (Optional[str]): Enables JavaScript rendering.
            callback_url (Optional[str]): URL to your callback endpoint.
            parse (Optional[bool]): true will return structured data.
            context: Optional[list],
            parsing_instructions (Optional[dict]): Instructions for parsing the results.
            request_timeout (int | 165, optional): The interval in seconds for
            the request to time out if no response is returned.
            Defaults to 165.

        Returns:
            SERPResponse: The response from the server after the job is completed.
        """

        config = prepare_config(request_timeout=request_timeout)
        payload = {
            "source": source.GOOGLE_SEARCH,
            "query": query,
            "domain": domain,
            "start_page": start_page,
            "pages": pages,
            "locale": locale,
            "geo_location": geo_location,
            "user_agent_type": user_agent_type,
            "render": render,
            "callback_url": callback_url,
            "parse": parse,
            "parsing_instructions": parsing_instructions,
            "context": context,
            **kwargs,
        }
        payload.setdefault("context", [])

        for item in payload["context"]:
            if item.get("key") == "tbm":
                item["value"] = item.get("value", "isch")
                break
        else:
            payload["context"].append({"key": "tbm", "value": "isch"})

        check_parsing_instructions_validity(parsing_instructions)
        response = self._serp_instance._get_resp(payload, config)
        return response

    def scrape_trends_explore(
        self,
        query: str,
        geo_location: Optional[str] = None,
        user_agent_type: Optional[str] = None,
        callback_url: Optional[str] = None,
        context: Optional[list] = None,
        request_timeout: Optional[int] = 165,
        **kwargs,
    ) -> SERPResponse:
        """
        Scrapes Google Trends Explore results for a given query.

        Args:
            query (str): The search query.
            user_agent_type (Optional[str]): Device type and browser.
            geo_location (Optional[str]): None,
            callback_url (Optional[str]): URL to your callback endpoint.
            parsing_instructions (Optional[dict]): Instructions for parsing the results.
            request_timeout (int | 165, optional): The interval in seconds for
            the request to time out if no response is returned.
            Defaults to 165.

        Returns:
            SERPResponse: The response from the server after the job is completed.
        """

        config = prepare_config(request_timeout=request_timeout)
        payload = {
            "source": source.GOOGLE_TRENDS_EXPLORE,
            "query": query,
            "geo_location": geo_location,
            "user_agent_type": user_agent_type,
            "callback_url": callback_url,
            "context": context,
            **kwargs,
        }
        response = self._serp_instance._get_resp(payload, config)
        return response


class GoogleAsync:
    def __init__(self, serp_async_instance) -> None:
        """
        Initializes an asynchronous Google object.

        Args:
            serp_async_instance: The SERP instance to be used for Google
            requests.
        """

        self._serp_async_instance = serp_async_instance

    async def scrape_search(
        self,
        query: str,
        domain: Optional[str] = None,
        start_page: Optional[int] = None,
        pages: Optional[int] = None,
        limit: Optional[int] = None,
        locale: Optional[str] = None,
        geo_location: Optional[str] = None,
        user_agent_type: Optional[str] = None,
        render: Optional[str] = None,
        callback_url: Optional[str] = None,
        parse: Optional[bool] = None,
        parsing_instructions: Optional[dict] = None,
        context: Optional[list] = None,
        request_timeout: Optional[int] = 165,
        job_completion_timeout: Optional[int] = None,
        poll_interval: Optional[int] = None,
        **kwargs,
    ) -> SERPResponse:
        """
        Asynchronously scrapes Google search results for a given query.

        Args:

            query (str): The search query.
            domain (Optional[str]): The domain to limit the search results to.
            start_page (Optional[int]): The starting page number.
            pages (Optional[int]): The number of pages to scrape.
            limit (Optional[int]): Number of results to retrieve in each page.
            user_agent_type (Optional[str]): Device type and browser.
            locale (Optional[str]): Accept-Language header value which changes your Bing search 
                            page web interface language.
            geo_location (Optional[str]): None,
            render (Optional[str]): Enables JavaScript rendering.
            callback_url (Optional[str]): URL to your callback endpoint.
            parse (Optional[bool]): true will return structured data.
            context: Optional[list],
            parsing_instructions (Optional[dict]): Instructions for parsing the results.
            request_timeout (int | 165, optional): The interval in seconds for
            the request to time out if no response is returned.
            Defaults to 165.
            poll_interval (int | 5, optional): The interval in seconds to poll
            the server for a response. Defaults to 5
            job_completion_timeout (int | 50, optional): The interval in
            seconds for the job to time out if no response is returned.
            Defaults to 50

        Returns:
            SERPResponse: The response from the server after the job is completed.
        """

        config = prepare_config(
            request_timeout=request_timeout,
            poll_interval=poll_interval,
            job_completion_timeout=job_completion_timeout,
            async_integration=True,
        )
        payload = {
            "source": source.GOOGLE_SEARCH,
            "query": query,
            "domain": domain,
            "start_page": start_page,
            "pages": pages,
            "limit": limit,
            "locale": locale,
            "geo_location": geo_location,
            "user_agent_type": user_agent_type,
            "render": render,
            "callback_url": callback_url,
            "parse": parse,
            "context": context,
            "parsing_instructions": parsing_instructions,
            **kwargs,
        }
        check_parsing_instructions_validity(parsing_instructions)
        response = await self._serp_async_instance._get_resp(payload, config)
        return response

    async def scrape_url(
        self,
        url: str,
        request_timeout: Optional[int] = 165,
        job_completion_timeout: Optional[int] = None,
        poll_interval: Optional[int] = None,
        user_agent_type: Optional[str] = None,
        render: Optional[str] = None,
        callback_url: Optional[str] = None,
        geo_location: Optional[str] = None,
        parse: Optional[bool] = None,
        parsing_instructions: Optional[dict] = None,
        **kwargs,
    ) -> SERPResponse:
        """
        Asynchronously scrapes Google search results for a given URL.

        Args:
            url (str): The URL to be scraped.
            user_agent_type (Optional[str]): Device type and browser.
            callback_url (Optional[str]): URL to your callback endpoint.
            render (Optional[str]): Enables JavaScript rendering.
            geo_location (Optional[str]): None,
            parse (Optional[bool]): true will return structured data.
            parsing_instructions (Optional[dict]): Instructions for parsing the results.
            request_timeout (int | 165, optional): The interval in seconds for
            the request to time out if no response is returned.
            Defaults to 165.
            poll_interval (int | 5, optional): The interval in seconds to poll
            the server for a response. Defaults to 5
            job_completion_timeout (int | 50, optional): The interval in
            seconds for the job to time out if no response is returned.
            Defaults to 50

        Returns:
            SERPResponse: The response from the server after the job is completed.
        """

        config = prepare_config(
            request_timeout=request_timeout,
            poll_interval=poll_interval,
            job_completion_timeout=job_completion_timeout,
            async_integration=True,
        )
        payload = {
            "source": source.GOOGLE_URL,
            "url": url,
            "user_agent_type": user_agent_type,
            "render": render,
            "callback_url": callback_url,
            "geo_location": geo_location,
            "parse": parse,
            "parsing_instructions": parsing_instructions,
            **kwargs,
        }
        check_parsing_instructions_validity(parsing_instructions)

        response = await self._serp_async_instance._get_resp(payload, config)
        return response

    async def scrape_ads(
        self,
        query: str,
        domain: Optional[str] = None,
        start_page: Optional[int] = None,
        pages: Optional[int] = None,
        locale: Optional[str] = None,
        geo_location: Optional[str] = None,
        user_agent_type: Optional[str] = None,
        render: Optional[str] = None,
        callback_url: Optional[str] = None,
        parse: Optional[bool] = None,
        parsing_instructions: Optional[dict] = None,
        context: Optional[list] = None,
        request_timeout: Optional[int] = 165,
        job_completion_timeout: Optional[int] = None,
        poll_interval: Optional[int] = None,
        **kwargs,
    ) -> SERPResponse:
        """
        Asynchronously scrapes Google Ads search results for a given query.

        Args:
            query (str): The search query.
            domain (Optional[str]): The domain to limit the search results to.
            start_page (Optional[int]): The starting page number.
            pages (Optional[int]): The number of pages to scrape.
            user_agent_type (Optional[str]): Device type and browser.
            locale (Optional[str]): Accept-Language header value which changes your Bing search 
                            page web interface language.
            geo_location (Optional[str]): None,
            render (Optional[str]): Enables JavaScript rendering.
            callback_url (Optional[str]): URL to your callback endpoint.
            parse (Optional[bool]): true will return structured data.
            context: Optional[list],
            parsing_instructions (Optional[dict]): Instructions for parsing the results.
            request_timeout (int | 165, optional): The interval in seconds for
            the request to time out if no response is returned.
            Defaults to 165.
            poll_interval (int | 5, optional): The interval in seconds to poll
            the server for a response. Defaults to 5
            job_completion_timeout (int | 50, optional): The interval in
            seconds for the job to time out if no response is returned.
            Defaults to 50

        Returns:
            SERPResponse: The response from the server after the job is completed.
        """

        config = prepare_config(
            request_timeout=request_timeout,
            poll_interval=poll_interval,
            job_completion_timeout=job_completion_timeout,
            async_integration=True,
        )
        payload = {
            "source": source.GOOGLE_ADS,
            "query": query,
            "domain": domain,
            "start_page": start_page,
            "pages": pages,
            "locale": locale,
            "geo_location": geo_location,
            "user_agent_type": user_agent_type,
            "render": render,
            "callback_url": callback_url,
            "parse": parse,
            "parsing_instructions": parsing_instructions,
            "context": context,
            **kwargs,
        }
        check_parsing_instructions_validity(parsing_instructions)
        response = await self._serp_async_instance._get_resp(payload, config)
        return response

    async def scrape_suggestions(
        self,
        query: str,
        locale: Optional[str] = None,
        geo_location: Optional[str] = None,
        user_agent_type: Optional[str] = None,
        render: Optional[str] = None,
        callback_url: Optional[str] = None,
        request_timeout: Optional[int] = 165,
        job_completion_timeout: Optional[int] = None,
        poll_interval: Optional[int] = None,
        **kwargs,
    ) -> SERPResponse:
        """
        Asynchronously scrapes Google suggestions for a given query.

        Args:
            query (str): The search query.
            locale (Optional[str]): Accept-Language header value which changes your Bing search 
                            page web interface language.
            geo_location (Optional[str]): None,
            user_agent_type (Optional[str]): Device type and browser.
            render (Optional[str]): Enables JavaScript rendering.
            callback_url (Optional[str]): URL to your callback endpoint.
            parsing_instructions (Optional[dict]): Instructions for parsing the results.
            request_timeout (int | 165, optional): The interval in seconds for
            the request to time out if no response is returned.
            Defaults to 165.
            poll_interval (int | 5, optional): The interval in seconds to poll
            the server for a response. Defaults to 5
            job_completion_timeout (int | 50, optional): The interval in
            seconds for the job to time out if no response is returned.
            Defaults to 50

        Returns:
            SERPResponse: The response from the server after the job is completed.
        """

        config = prepare_config(
            request_timeout=request_timeout,
            poll_interval=poll_interval,
            job_completion_timeout=job_completion_timeout,
            async_integration=True,
        )
        payload = {
            "source": source.GOOGLE_SUGGESTIONS,
            "query": query,
            "locale": locale,
            "geo_location": geo_location,
            "user_agent_type": user_agent_type,
            "render": render,
            "callback_url": callback_url,
            **kwargs,
        }
        response = await self._serp_async_instance._get_resp(payload, config)
        return response

    async def scrape_hotels(
        self,
        query: str,
        domain: Optional[str] = None,
        start_page: Optional[int] = None,
        pages: Optional[int] = None,
        limit: Optional[int] = None,
        locale: Optional[str] = None,
        geo_location: Optional[str] = None,
        user_agent_type: Optional[str] = None,
        render: Optional[str] = None,
        callback_url: Optional[str] = None,
        context: Optional[list] = None,
        request_timeout: Optional[int] = 165,
        job_completion_timeout: Optional[int] = None,
        poll_interval: Optional[int] = None,
        **kwargs,
    ) -> SERPResponse:
        """
        Asynchronously scrapes Google Hotels search results for a given query.

        Args:
            query (str): The search query.
            
                    domain (Optional[str]): The domain to limit the search results to.
                    start_page (Optional[int]): The starting page number.
                    pages (Optional[int]): The number of pages to scrape.
                    limit (Optional[int]): Number of results to retrieve in each page.
                    user_agent_type (Optional[str]): Device type and browser.
                    locale (Optional[str]): Accept-Language header value which changes your Bing search 
                                    page web interface language.
                    geo_location (Optional[str]): None,
                    render (Optional[str]): Enables JavaScript rendering.
                    callback_url (Optional[str]): URL to your callback endpoint.
                    context: Optional[list],
                    parsing_instructions (Optional[dict]): Instructions for parsing the results.
            request_timeout (int | 165, optional): The interval in seconds for
            the request to time out if no response is returned.
            Defaults to 165.
            poll_interval (int | 5, optional): The interval in seconds to poll
            the server for a response. Defaults to 5
            job_completion_timeout (int | 50, optional): The interval in
            seconds for the job to time out if no response is returned.
            Defaults to 50

        Returns:
            SERPResponse: The response from the server after the job is completed.
        """

        config = prepare_config(
            request_timeout=request_timeout,
            poll_interval=poll_interval,
            job_completion_timeout=job_completion_timeout,
            async_integration=True,
        )
        payload = {
            "source": source.GOOGLE_HOTELS,
            "query": query,
            "domain": domain,
            "start_page": start_page,
            "pages": pages,
            "limit": limit,
            "locale": locale,
            "geo_location": geo_location,
            "user_agent_type": user_agent_type,
            "render": render,
            "callback_url": callback_url,
            "context": context,
            **kwargs,
        }
        response = await self._serp_async_instance._get_resp(payload, config)
        return response

    async def scrape_travel_hotels(
        self,
        query: str,
        domain: Optional[str] = None,
        start_page: Optional[int] = None,
        locale: Optional[str] = None,
        geo_location: Optional[str] = None,
        user_agent_type: Optional[str] = None,
        render: Optional[str] = None,
        callback_url: Optional[str] = None,
        context: Optional[list] = None,
        request_timeout: Optional[int] = 165,
        job_completion_timeout: Optional[int] = None,
        poll_interval: Optional[int] = None,
        **kwargs,
    ) -> SERPResponse:
        """
        Asynchronously scrapes Google Travel Hotels search results for a given
        query.

        Args:
            query (str): UTF-encoded keyword. "query": "hotels" will result
            list hotels in a given geo_location;
            "query": "hotels in <Location>" will result in a list hotels for
            <Location>. Eg hotels in Paris will list hotels in Paris, no matter
            what geo_location is given.
            domain (Optional[str]): The domain to limit the search results to.
            start_page (Optional[int]): The starting page number.
            locale (Optional[str]): Accept-Language header value which changes your Bing search 
                            page web interface language.
            geo_location (Optional[str]): None,
            user_agent_type (Optional[str]): Device type and browser.
            render (Optional[str]): Enables JavaScript rendering.
            callback_url (Optional[str]): URL to your callback endpoint.
            context: Optional[list],
            parsing_instructions (Optional[dict]): Instructions for parsing the results.
            request_timeout (int | 165, optional): The interval in seconds for
            the request to time out if no response is returned.
            Defaults to 165.
            poll_interval (int | 5, optional): The interval in seconds to poll
            the server for a response. Defaults to 5
            job_completion_timeout (int | 50, optional): The interval in
            seconds for the job to time out if no response is returned.
            Defaults to 50

        Returns:
            SERPResponse: The response from the server after the job is completed.
        """

        config = prepare_config(
            request_timeout=request_timeout,
            poll_interval=poll_interval,
            job_completion_timeout=job_completion_timeout,
            async_integration=True,
        )
        payload = {
            "source": source.GOOGLE_TRAVEL_HOTELS,
            "query": query,
            "domain": domain,
            "start_page": start_page,
            "locale": locale,
            "geo_location": geo_location,
            "user_agent_type": user_agent_type,
            "render": render,
            "callback_url": callback_url,
            "context": context,
            **kwargs,
        }
        response = await self._serp_async_instance._get_resp(payload, config)
        return response

    async def scrape_images(
        self,
        query: str,
        domain: Optional[str] = None,
        start_page: Optional[int] = None,
        pages: Optional[int] = None,
        locale: Optional[str] = None,
        geo_location: Optional[str] = None,
        user_agent_type: Optional[str] = None,
        render: Optional[str] = None,
        callback_url: Optional[str] = None,
        parse: Optional[bool] = None,
        parsing_instructions: Optional[dict] = None,
        context: Optional[list] = None,
        request_timeout: Optional[int] = 165,
        job_completion_timeout: Optional[int] = None,
        poll_interval: Optional[int] = None,
        **kwargs,
    ) -> SERPResponse:
        """
        Asynchronously scrapes Google Images search results for a given query.

        Args:
            query (str): The search query.
            domain (Optional[str]): The domain to limit the search results to.
            start_page (Optional[int]): The starting page number.
            pages (Optional[int]): The number of pages to scrape.
            user_agent_type (Optional[str]): Device type and browser.
            locale (Optional[str]): Accept-Language header value which changes your Bing search 
                            page web interface language.
            geo_location (Optional[str]): None,
            render (Optional[str]): Enables JavaScript rendering.
            callback_url (Optional[str]): URL to your callback endpoint.
            parse (Optional[bool]): true will return structured data.
            context: Optional[list],
            parsing_instructions (Optional[dict]): Instructions for parsing the results.
            request_timeout (int | 165, optional): The interval in seconds for
            the request to time out if no response is returned.
            Defaults to 165.
            poll_interval (int | 5, optional): The interval in seconds to poll
            the server for a response. Defaults to 5
            job_completion_timeout (int | 50, optional): The interval in
            seconds for the job to time out if no response is returned.
            Defaults to 50

        Returns:
            SERPResponse: The response from the server after the job is completed.
        """

        config = prepare_config(
            request_timeout=request_timeout,
            poll_interval=poll_interval,
            job_completion_timeout=job_completion_timeout,
            async_integration=True,
        )
        payload = {
            "source": source.GOOGLE_SEARCH,
            "query": query,
            "domain": domain,
            "start_page": start_page,
            "pages": pages,
            "locale": locale,
            "geo_location": geo_location,
            "user_agent_type": user_agent_type,
            "render": render,
            "callback_url": callback_url,
            "parse": parse,
            "parsing_instructions": parsing_instructions,
            "context": context,
            **kwargs,
        }
        payload.setdefault("context", [])

        for item in payload["context"]:
            if item.get("key") == "tbm":
                item["value"] = item.get("value", "isch")
                break
        else:
            payload["context"].append({"key": "tbm", "value": "isch"})

        check_parsing_instructions_validity(parsing_instructions)
        response = await self._serp_async_instance._get_resp(payload, config)
        return response

    async def scrape_trends_explore(
        self,
        query: str,
        geo_location: Optional[str] = None,
        user_agent_type: Optional[str] = None,
        callback_url: Optional[str] = None,
        context: Optional[list] = None,
        request_timeout: Optional[int] = 165,
        job_completion_timeout: Optional[int] = None,
        poll_interval: Optional[int] = None,
        **kwargs,
    ) -> SERPResponse:
        """
        Asynchronously scrapes Google Trends Explore results for a given query.

        Args:
            query (str): The search query.
            user_agent_type (Optional[str]): Device type and browser.
            geo_location (Optional[str]): None,
            callback_url (Optional[str]): URL to your callback endpoint.
            parsing_instructions (Optional[dict]): Instructions for parsing the results.
            request_timeout (int | 165, optional): The interval in seconds for
            the request to time out if no response is returned.
            Defaults to 165.
            poll_interval (int | 5, optional): The interval in seconds to poll
            the server for a response. Defaults to 5
            job_completion_timeout (int | 50, optional): The interval in
            seconds for the job to time out if no response is returned.
            Defaults to 50

        Returns:
            SERPResponse: The response from the server after the job is completed.
        """

        config = prepare_config(
            request_timeout=request_timeout,
            poll_interval=poll_interval,
            job_completion_timeout=job_completion_timeout,
            async_integration=True,
        )
        payload = {
            "source": source.GOOGLE_TRENDS_EXPLORE,
            "query": query,
            "geo_location": geo_location,
            "user_agent_type": user_agent_type,
            "callback_url": callback_url,
            "context": context,
            **kwargs,
        }
        response = await self._serp_async_instance._get_resp(payload, config)
        return response
