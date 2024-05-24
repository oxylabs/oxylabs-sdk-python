from typing import Optional

from oxylabs.sources.ecommerce.response import EcommerceResponse
from oxylabs.utils.types import source
from oxylabs.utils.utils import (
    check_parsing_instructions_validity,
    prepare_config,
)


class Amazon:
    def __init__(self, ecommerce_instance) -> None:
        """
        Initializes an instance of the Amazon class.

        Args:
            ecommerce_instance: The Ecommerce instance associated with the
            Amazon class.
        """
        self._ecommerce_instance = ecommerce_instance

    def scrape_search(
        self,
        query: str,
        domain: Optional[str] = None,
        start_page: Optional[int] = None,
        pages: Optional[int] = None,
        geo_location: Optional[str] = None,
        user_agent_type: Optional[str] = None,
        render: Optional[str] = None,
        callback_url: Optional[str] = None,
        context: Optional[list] = None,
        parse: Optional[bool] = None,
        parsing_instructions: Optional[dict] = None,
        request_timeout: Optional[int] = 165,
        **kwargs
    ) -> EcommerceResponse:
        """
        Scrapes Amazon search results for a given query.

        Args:
            query (str): The search query.
            domain (Optional[str]): The domain to limit the search results to.
            start_page (Optional[int]): The starting page number.
            pages (Optional[int]): The number of pages to scrape.
            geo_location (Optional[str]): The Deliver to location.
            user_agent_type (Optional[str]): Device type and browser.
            callback_url (Optional[str]): URL to your callback endpoint.
            render (Optional[str]): Enables JavaScript rendering.
            parse (Optional[bool]): true will return structured data.
            context: Optional[list],
            parsing_instructions (Optional[dict]): Instructions for parsing the results.
            request_timeout (int | 165, optional): The interval in seconds for
            the request to time out if no response is returned.
            Defaults to 165.

        Returns:
            EcommerceResponse: The response containing the scraped results.
        """

        config = prepare_config(request_timeout=request_timeout)
        payload = {
            "source": source.AMAZON_SEARCH,
            "query": query,
            "domain": domain,
            "start_page": start_page,
            "pages": pages,
            "geo_location": geo_location,
            "user_agent_type": user_agent_type,
            "render": render,
            "callback_url": callback_url,
            "context": context,
            "parse": parse,
            "parsing_instructions": parsing_instructions,
            **kwargs,
        }
        check_parsing_instructions_validity(parsing_instructions)
        response = self._ecommerce_instance._get_resp(payload, config)
        return response

    def scrape_url(
        self,
        url: str,
        user_agent_type: Optional[str] = None,
        render: Optional[str] = None,
        callback_url: Optional[str] = None,
        parse: Optional[bool] = None,
        parsing_instructions: Optional[dict] = None,
        request_timeout: Optional[int] = 165,
        **kwargs
    ) -> EcommerceResponse:
        """
        Scrapes Amazon search results for a given URL.

        Args:
            url (str): The URL to scrape.
            domain (Optional[str]): The domain to limit the search results to.
            user_agent_type (Optional[str]): Device type and browser.
            callback_url (Optional[str]): URL to your callback endpoint.
            render (Optional[str]): Enables JavaScript rendering.
            parse (Optional[bool]): true will return structured data.
            parsing_instructions (Optional[dict]): Instructions for parsing the results.
            request_timeout (int | 165, optional): The interval in seconds for
            the request to time out if no response is returned.
            Defaults to 165.

        Returns:
            EcommerceResponse: The response containing the scraped results.
        """

        config = prepare_config(request_timeout=request_timeout)
        payload = {
            "source": source.AMAZON_URL,
            "url": url,
            "user_agent_type": user_agent_type,
            "render": render,
            "callback_url": callback_url,
            "parse": parse,
            "parsing_instructions": parsing_instructions,
            **kwargs,
        }
        check_parsing_instructions_validity(parsing_instructions)
        response = self._ecommerce_instance._get_resp(payload, config)
        return response

    def scrape_product(
        self,
        query: str,
        domain: Optional[str] = None,
        geo_location: Optional[str] = None,
        user_agent_type: Optional[str] = None,
        render: Optional[str] = None,
        callback_url: Optional[str] = None,
        context: Optional[list] = None,
        parse: Optional[bool] = None,
        parsing_instructions: Optional[dict] = None,
        request_timeout: Optional[int] = 165,
        **kwargs
    ) -> EcommerceResponse:
        """
        Scrapes Amazon product details for a given query.

        Args:
            query (str): 10-symbol ASIN code.
            domain (Optional[str]): The domain to limit the search results to.
            geo_location (Optional[str]): The Deliver to location.
            user_agent_type (Optional[str]): Device type and browser.
            callback_url (Optional[str]): URL to your callback endpoint.
            render (Optional[str]): Enables JavaScript rendering.
            parse (Optional[bool]): true will return structured data.
            context: Optional[list],
            parsing_instructions (Optional[dict]): Instructions for parsing the results.
            request_timeout (int | 165, optional): The interval in seconds for
            the request to time out if no response is returned.
            Defaults to 165.

        Returns:
            EcommerceResponse: The response containing the scraped results.
        """

        config = prepare_config(request_timeout=request_timeout)
        payload = {
            "source": source.AMAZON_PRODUCT,
            "query": query,
            "domain": domain,
            "geo_location": geo_location,
            "user_agent_type": user_agent_type,
            "render": render,
            "callback_url": callback_url,
            "context": context,
            "parse": parse,
            "parsing_instructions": parsing_instructions,
            **kwargs,
        }
        check_parsing_instructions_validity(parsing_instructions)
        response = self._ecommerce_instance._get_resp(payload, config)
        return response

    def scrape_pricing(
        self,
        query: str,
        domain: Optional[str] = None,
        start_page: Optional[int] = None,
        pages: Optional[int] = None,
        geo_location: Optional[str] = None,
        user_agent_type: Optional[str] = None,
        render: Optional[str] = None,
        callback_url: Optional[str] = None,
        parse: Optional[bool] = None,
        parsing_instructions: Optional[dict] = None,
        request_timeout: Optional[int] = 165,
        **kwargs
    ) -> EcommerceResponse:
        """
        Scrapes Amazon pricing details for a given query.

        Args:
            query (str): 10-symbol ASIN code.
            domain (Optional[str]): The domain to limit the search results to.
            start_page (Optional[int]): The starting page number.
            pages (Optional[int]): The number of pages to scrape.
            geo_location (Optional[str]): The Deliver to location.
            user_agent_type (Optional[str]): Device type and browser.
            callback_url (Optional[str]): URL to your callback endpoint.
            render (Optional[str]): Enables JavaScript rendering.
            parse (Optional[bool]): true will return structured data.
            parsing_instructions (Optional[dict]): Instructions for parsing the results.
            request_timeout (int | 165, optional): The interval in seconds for
            the request to time out if no response is returned.
            Defaults to 165.

        Returns:
            EcommerceResponse: The response containing the scraped results.
        """

        config = prepare_config(request_timeout=request_timeout)
        payload = {
            "source": source.AMAZON_PRICING,
            "query": query,
            "domain": domain,
            "start_page": start_page,
            "pages": pages,
            "geo_location": geo_location,
            "user_agent_type": user_agent_type,
            "render": render,
            "callback_url": callback_url,
            "parse": parse,
            "parsing_instructions": parsing_instructions,
            **kwargs,
        }
        check_parsing_instructions_validity(parsing_instructions)
        response = self._ecommerce_instance._get_resp(payload, config)
        return response

    def scrape_reviews(
        self,
        query: str,
        domain: Optional[str] = None,
        start_page: Optional[int] = None,
        pages: Optional[int] = None,
        geo_location: Optional[str] = None,
        user_agent_type: Optional[str] = None,
        render: Optional[str] = None,
        callback_url: Optional[str] = None,
        parse: Optional[bool] = None,
        parsing_instructions: Optional[dict] = None,
        request_timeout: Optional[int] = 165,
        **kwargs
    ) -> EcommerceResponse:
        """
        Scrapes Amazon reviews for a given query.

        Args:
            query (str): 10-symbol ASIN code.
            domain (Optional[str]): The domain to limit the search results to.
            start_page (Optional[int]): The starting page number.
            pages (Optional[int]): The number of pages to scrape.
            geo_location (Optional[str]): The Deliver to location.
            user_agent_type (Optional[str]): Device type and browser.
            callback_url (Optional[str]): URL to your callback endpoint.
            render (Optional[str]): Enables JavaScript rendering.
            parse (Optional[bool]): true will return structured data.
            parsing_instructions (Optional[dict]): Instructions for parsing the results.
            request_timeout (int | 165, optional): The interval in seconds for
            the request to time out if no response is returned.
            Defaults to 165.

        Returns:
            EcommerceResponse: The response containing the scraped results.
        """

        config = prepare_config(request_timeout=request_timeout)
        payload = {
            "source": source.AMAZON_REVIEWS,
            "query": query,
            "domain": domain,
            "start_page": start_page,
            "pages": pages,
            "geo_location": geo_location,
            "user_agent_type": user_agent_type,
            "render": render,
            "callback_url": callback_url,
            "parse": parse,
            "parsing_instructions": parsing_instructions,
            **kwargs,
        }
        check_parsing_instructions_validity(parsing_instructions)
        response = self._ecommerce_instance._get_resp(payload, config)
        return response

    def scrape_questions(
        self,
        query: str,
        domain: Optional[str] = None,
        geo_location: Optional[str] = None,
        user_agent_type: Optional[str] = None,
        render: Optional[str] = None,
        callback_url: Optional[str] = None,
        parse: Optional[bool] = None,
        parsing_instructions: Optional[dict] = None,
        request_timeout: Optional[int] = 165,
        **kwargs
    ) -> EcommerceResponse:
        """
        Scrapes Amazon questions for a given query.

        Args:
            query (str): 10-symbol ASIN code.
            domain (Optional[str]): The domain to limit the search results to.
            geo_location (Optional[str]): The Deliver to location.
            user_agent_type (Optional[str]): Device type and browser.
            callback_url (Optional[str]): URL to your callback endpoint.
            render (Optional[str]): Enables JavaScript rendering.
            parse (Optional[bool]): true will return structured data.
            parsing_instructions (Optional[dict]): Instructions for parsing the results.
            request_timeout (int | 165, optional): The interval in seconds for
            the request to time out if no response is returned.
            Defaults to 165.

        Returns:
            EcommerceResponse: The response containing the scraped results.
        """

        config = prepare_config(request_timeout=request_timeout)
        payload = {
            "source": source.AMAZON_QUESTIONS,
            "query": query,
            "domain": domain,
            "geo_location": geo_location,
            "user_agent_type": user_agent_type,
            "render": render,
            "callback_url": callback_url,
            "parse": parse,
            "parsing_instructions": parsing_instructions,
            **kwargs,
        }
        check_parsing_instructions_validity(parsing_instructions)
        response = self._ecommerce_instance._get_resp(payload, config)
        return response

    def scrape_bestsellers(
        self,
        query: str,
        domain: Optional[str] = None,
        start_page: Optional[int] = None,
        pages: Optional[int] = None,
        geo_location: Optional[str] = None,
        user_agent_type: Optional[str] = None,
        render: Optional[str] = None,
        callback_url: Optional[str] = None,
        parse: Optional[bool] = None,
        parsing_instructions: Optional[dict] = None,
        request_timeout: Optional[int] = 165,
        **kwargs
    ) -> EcommerceResponse:
        """
        Scrapes Amazon bestsellers.

        Args:
            query (str): Browse node ID.
            domain (Optional[str]): The domain to limit the search results to.
            start_page (Optional[int]): The starting page number.
            pages (Optional[int]): The number of pages to scrape.
            geo_location (Optional[str]): The Deliver to location.
            user_agent_type (Optional[str]): Device type and browser.
            callback_url (Optional[str]): URL to your callback endpoint.
            render (Optional[str]): Enables JavaScript rendering.
            parse (Optional[bool]): true will return structured data.
            parsing_instructions (Optional[dict]): Instructions for parsing the results.
            request_timeout (int | 165, optional): The interval in seconds for
            the request to time out if no response is returned.
            Defaults to 165.

        Returns:
            EcommerceResponse: The response containing the scraped results.
        """

        config = prepare_config(request_timeout=request_timeout)
        payload = {
            "source": source.AMAZON_BEST_SELLERS,
            "query": query,
            "domain": domain,
            "start_page": start_page,
            "pages": pages,
            "geo_location": geo_location,
            "user_agent_type": user_agent_type,
            "render": render,
            "callback_url": callback_url,
            "parse": parse,
            "parsing_instructions": parsing_instructions,
            **kwargs,
        }
        check_parsing_instructions_validity(parsing_instructions)
        response = self._ecommerce_instance._get_resp(payload, config)
        return response

    def scrape_sellers(
        self,
        query: str,
        domain: Optional[str] = None,
        geo_location: Optional[str] = None,
        user_agent_type: Optional[str] = None,
        render: Optional[str] = None,
        callback_url: Optional[str] = None,
        parse: Optional[bool] = None,
        parsing_instructions: Optional[dict] = None,
        request_timeout: Optional[int] = 165,
        **kwargs
    ) -> EcommerceResponse:
        """
        Scrapes Amazon sellers for a given query.

        Args:
            query (str): 13-character seller ID.
            domain (Optional[str]): The domain to limit the search results to.
            geo_location (Optional[str]): The Deliver to location.
            user_agent_type (Optional[str]): Device type and browser.
            callback_url (Optional[str]): URL to your callback endpoint.
            render (Optional[str]): Enables JavaScript rendering.
            parse (Optional[bool]): true will return structured data.
            parsing_instructions (Optional[dict]): Instructions for parsing the results.
            request_timeout (int | 165, optional): The interval in seconds for
            the request to time out if no response is returned.
            Defaults to 165.

        Returns:
            EcommerceResponse: The response containing the scraped results.
        """

        config = prepare_config(request_timeout=request_timeout)
        payload = {
            "source": source.AMAZON_SELLERS,
            "query": query,
            "domain": domain,
            "geo_location": geo_location,
            "user_agent_type": user_agent_type,
            "render": render,
            "callback_url": callback_url,
            "parse": parse,
            "parsing_instructions": parsing_instructions,
            **kwargs,
        }
        check_parsing_instructions_validity(parsing_instructions)
        response = self._ecommerce_instance._get_resp(payload, config)
        return response


class AmazonAsync:
    def __init__(self, ecommerce_async_instance) -> None:
        """
        Initializes an instance of the AmazonAsync class.

        Args:
            ecommerce_async_instance: The EcommerceAsync instance associated
            with the AmazonAsync class.
        """
        self._ecommerce_async_instance = ecommerce_async_instance

    async def scrape_search(
        self,
        query: str,
        domain: Optional[str] = None,
        start_page: Optional[int] = None,
        pages: Optional[int] = None,
        geo_location: Optional[str] = None,
        user_agent_type: Optional[str] = None,
        render: Optional[str] = None,
        callback_url: Optional[str] = None,
        context: Optional[list] = None,
        parse: Optional[bool] = None,
        parsing_instructions: Optional[dict] = None,
        request_timeout: Optional[int] = 165,
        job_completion_timeout: Optional[int] = None,
        poll_interval: Optional[int] = None,
        **kwargs
    ) -> EcommerceResponse:
        """
        Scrapes Amazon search results for a given query.

        Args:
            query (str): The search query.
            domain (Optional[str]): The domain to limit the search results to.
            start_page (Optional[int]): The starting page number.
            pages (Optional[int]): The number of pages to scrape.
            geo_location (Optional[str]): The Deliver to location.
            user_agent_type (Optional[str]): Device type and browser.
            callback_url (Optional[str]): URL to your callback endpoint.
            render (Optional[str]): Enables JavaScript rendering.
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
            EcommerceResponse: The response containing the scraped results.
        """

        config = prepare_config(
            request_timeout=request_timeout,
            poll_interval=poll_interval,
            job_completion_timeout=job_completion_timeout,
            async_integration=True,
        )
        payload = {
            "source": source.AMAZON_SEARCH,
            "query": query,
            "domain": domain,
            "start_page": start_page,
            "pages": pages,
            "geo_location": geo_location,
            "user_agent_type": user_agent_type,
            "render": render,
            "callback_url": callback_url,
            "context": context,
            "parse": parse,
            "parsing_instructions": parsing_instructions,
            **kwargs,
        }
        check_parsing_instructions_validity(parsing_instructions)
        response = await self._ecommerce_async_instance._get_resp(
            payload, config
        )
        return response

    async def scrape_url(
        self,
        url: str,
        user_agent_type: Optional[str] = None,
        render: Optional[str] = None,
        callback_url: Optional[str] = None,
        parse: Optional[bool] = None,
        parsing_instructions: Optional[dict] = None,
        request_timeout: Optional[int] = 165,
        job_completion_timeout: Optional[int] = None,
        poll_interval: Optional[int] = None,
        **kwargs
    ) -> EcommerceResponse:
        """
        Scrapes Amazon search results for a given URL.

        Args:
            url (str): The URL to scrape.
            domain (Optional[str]): The domain to limit the search results to.
            user_agent_type (Optional[str]): Device type and browser.
            callback_url (Optional[str]): URL to your callback endpoint.
            render (Optional[str]): Enables JavaScript rendering.
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
            EcommerceResponse: The response containing the scraped results.
        """

        config = prepare_config(
            request_timeout=request_timeout,
            poll_interval=poll_interval,
            job_completion_timeout=job_completion_timeout,
            async_integration=True,
        )
        payload = {
            "source": source.AMAZON_URL,
            "url": url,
            "user_agent_type": user_agent_type,
            "render": render,
            "callback_url": callback_url,
            "parse": parse,
            "parsing_instructions": parsing_instructions,
            **kwargs,
        }
        check_parsing_instructions_validity(parsing_instructions)
        response = await self._ecommerce_async_instance._get_resp(
            payload, config
        )
        return response

    async def scrape_product(
        self,
        query: str,
        domain: Optional[str] = None,
        geo_location: Optional[str] = None,
        user_agent_type: Optional[str] = None,
        render: Optional[str] = None,
        callback_url: Optional[str] = None,
        context: Optional[list] = None,
        parse: Optional[bool] = None,
        parsing_instructions: Optional[dict] = None,
        request_timeout: Optional[int] = 165,
        job_completion_timeout: Optional[int] = None,
        poll_interval: Optional[int] = None,
        **kwargs
    ) -> EcommerceResponse:
        """
        Scrapes Amazon product details for a given query.

        Args:
            query (str): 10-symbol ASIN code.
            domain (Optional[str]): The domain to limit the search results to.
            geo_location (Optional[str]): The Deliver to location.
            user_agent_type (Optional[str]): Device type and browser.
            callback_url (Optional[str]): URL to your callback endpoint.
            render (Optional[str]): Enables JavaScript rendering.
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
            EcommerceResponse: The response containing the scraped results.
        """

        config = prepare_config(
            request_timeout=request_timeout,
            poll_interval=poll_interval,
            job_completion_timeout=job_completion_timeout,
            async_integration=True,
        )
        payload = {
            "source": source.AMAZON_PRODUCT,
            "query": query,
            "domain": domain,
            "geo_location": geo_location,
            "user_agent_type": user_agent_type,
            "render": render,
            "callback_url": callback_url,
            "context": context,
            "parse": parse,
            "parsing_instructions": parsing_instructions,
            **kwargs,
        }
        check_parsing_instructions_validity(parsing_instructions)
        response = await self._ecommerce_async_instance._get_resp(
            payload, config
        )
        return response

    async def scrape_pricing(
        self,
        query: str,
        domain: Optional[str] = None,
        start_page: Optional[int] = None,
        pages: Optional[int] = None,
        geo_location: Optional[str] = None,
        user_agent_type: Optional[str] = None,
        render: Optional[str] = None,
        callback_url: Optional[str] = None,
        parse: Optional[bool] = None,
        parsing_instructions: Optional[dict] = None,
        request_timeout: Optional[int] = 165,
        job_completion_timeout: Optional[int] = None,
        poll_interval: Optional[int] = None,
        **kwargs
    ) -> EcommerceResponse:
        """
        Scrapes Amazon pricing details for a given query.

        Args:
            query (str): 10-symbol ASIN code.
            domain (Optional[str]): The domain to limit the search results to.
            start_page (Optional[int]): The starting page number.
            pages (Optional[int]): The number of pages to scrape.
            geo_location (Optional[str]): The Deliver to location.
            user_agent_type (Optional[str]): Device type and browser.
            callback_url (Optional[str]): URL to your callback endpoint.
            render (Optional[str]): Enables JavaScript rendering.
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
            EcommerceResponse: The response containing the scraped results.
        """

        config = prepare_config(
            request_timeout=request_timeout,
            poll_interval=poll_interval,
            job_completion_timeout=job_completion_timeout,
            async_integration=True,
        )
        payload = {
            "source": source.AMAZON_PRICING,
            "query": query,
            "domain": domain,
            "start_page": start_page,
            "pages": pages,
            "geo_location": geo_location,
            "user_agent_type": user_agent_type,
            "render": render,
            "callback_url": callback_url,
            "parse": parse,
            "parsing_instructions": parsing_instructions,
            **kwargs,
        }
        check_parsing_instructions_validity(parsing_instructions)
        response = await self._ecommerce_async_instance._get_resp(
            payload, config
        )
        return response

    async def scrape_reviews(
        self,
        query: str,
        domain: Optional[str] = None,
        start_page: Optional[int] = None,
        pages: Optional[int] = None,
        geo_location: Optional[str] = None,
        user_agent_type: Optional[str] = None,
        render: Optional[str] = None,
        callback_url: Optional[str] = None,
        parse: Optional[bool] = None,
        parsing_instructions: Optional[dict] = None,
        request_timeout: Optional[int] = 165,
        job_completion_timeout: Optional[int] = None,
        poll_interval: Optional[int] = None,
        **kwargs
    ) -> EcommerceResponse:
        """
        Scrapes Amazon reviews for a given query.

        Args:
            query (str): 10-symbol ASIN code.
            domain (Optional[str]): The domain to limit the search results to.
            start_page (Optional[int]): The starting page number.
            pages (Optional[int]): The number of pages to scrape.
            geo_location (Optional[str]): The Deliver to location.
            user_agent_type (Optional[str]): Device type and browser.
            callback_url (Optional[str]): URL to your callback endpoint.
            render (Optional[str]): Enables JavaScript rendering.
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
            EcommerceResponse: The response containing the scraped results.
        """

        config = prepare_config(
            request_timeout=request_timeout,
            poll_interval=poll_interval,
            job_completion_timeout=job_completion_timeout,
            async_integration=True,
        )
        payload = {
            "source": source.AMAZON_REVIEWS,
            "query": query,
            "domain": domain,
            "start_page": start_page,
            "pages": pages,
            "geo_location": geo_location,
            "user_agent_type": user_agent_type,
            "render": render,
            "callback_url": callback_url,
            "parse": parse,
            "parsing_instructions": parsing_instructions,
            **kwargs,
        }
        check_parsing_instructions_validity(parsing_instructions)
        response = await self._ecommerce_async_instance._get_resp(
            payload, config
        )
        return response

    async def scrape_questions(
        self,
        query: str,
        domain: Optional[str] = None,
        geo_location: Optional[str] = None,
        user_agent_type: Optional[str] = None,
        render: Optional[str] = None,
        callback_url: Optional[str] = None,
        parse: Optional[bool] = None,
        parsing_instructions: Optional[dict] = None,
        request_timeout: Optional[int] = 165,
        job_completion_timeout: Optional[int] = None,
        poll_interval: Optional[int] = None,
        **kwargs
    ) -> EcommerceResponse:
        """
        Scrapes Amazon questions for a given query.

        Args:
            query (str): 10-symbol ASIN code.
            domain (Optional[str]): The domain to limit the search results to.
            geo_location (Optional[str]): The Deliver to location.
            user_agent_type (Optional[str]): Device type and browser.
            callback_url (Optional[str]): URL to your callback endpoint.
            render (Optional[str]): Enables JavaScript rendering.
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
            EcommerceResponse: The response containing the scraped results.
        """

        config = prepare_config(
            request_timeout=request_timeout,
            poll_interval=poll_interval,
            job_completion_timeout=job_completion_timeout,
            async_integration=True,
        )
        payload = {
            "source": source.AMAZON_QUESTIONS,
            "query": query,
            "domain": domain,
            "geo_location": geo_location,
            "user_agent_type": user_agent_type,
            "render": render,
            "callback_url": callback_url,
            "parse": parse,
            "parsing_instructions": parsing_instructions,
            **kwargs,
        }
        check_parsing_instructions_validity(parsing_instructions)
        response = await self._ecommerce_async_instance._get_resp(
            payload, config
        )
        return response

    async def scrape_bestsellers(
        self,
        query,
        domain: Optional[str] = None,
        start_page: Optional[int] = None,
        pages: Optional[int] = None,
        geo_location: Optional[str] = None,
        user_agent_type: Optional[str] = None,
        render: Optional[str] = None,
        callback_url: Optional[str] = None,
        parse: Optional[bool] = None,
        parsing_instructions: Optional[dict] = None,
        request_timeout: Optional[int] = 165,
        job_completion_timeout: Optional[int] = None,
        poll_interval: Optional[int] = None,
        **kwargs
    ) -> EcommerceResponse:
        """
        Scrapes Amazon bestsellers.

        Args:
            query (str): Browse node ID.
            domain (Optional[str]): The domain to limit the search results to.
            start_page (Optional[int]): The starting page number.
            pages (Optional[int]): The number of pages to scrape.
            geo_location (Optional[str]): The Deliver to location.
            user_agent_type (Optional[str]): Device type and browser.
            callback_url (Optional[str]): URL to your callback endpoint.
            render (Optional[str]): Enables JavaScript rendering.
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
            EcommerceResponse: The response containing the scraped results.
        """

        config = prepare_config(
            request_timeout=request_timeout,
            poll_interval=poll_interval,
            job_completion_timeout=job_completion_timeout,
            async_integration=True,
        )
        payload = {
            "source": source.AMAZON_BEST_SELLERS,
            "query": query,
            "domain": domain,
            "start_page": start_page,
            "pages": pages,
            "geo_location": geo_location,
            "user_agent_type": user_agent_type,
            "render": render,
            "callback_url": callback_url,
            "parse": parse,
            "parsing_instructions": parsing_instructions,
            **kwargs,
        }
        check_parsing_instructions_validity(parsing_instructions)
        response = await self._ecommerce_async_instance._get_resp(
            payload, config
        )
        return response

    async def scrape_sellers(
        self,
        query: str,
        domain: Optional[str] = None,
        geo_location: Optional[str] = None,
        user_agent_type: Optional[str] = None,
        render: Optional[str] = None,
        callback_url: Optional[str] = None,
        parse: Optional[bool] = None,
        parsing_instructions: Optional[dict] = None,
        request_timeout: Optional[int] = 165,
        job_completion_timeout: Optional[int] = None,
        poll_interval: Optional[int] = None,
        **kwargs
    ) -> EcommerceResponse:
        """
        Scrapes Amazon sellers for a given query.

        Args:
            query (str): 13-character seller ID.
            domain (Optional[str]): The domain to limit the search results to.
            geo_location (Optional[str]): The Deliver to location.
            user_agent_type (Optional[str]): Device type and browser.
            callback_url (Optional[str]): URL to your callback endpoint.
            render (Optional[str]): Enables JavaScript rendering.
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
            EcommerceResponse: The response containing the scraped results.
        """

        config = prepare_config(
            request_timeout=request_timeout,
            poll_interval=poll_interval,
            job_completion_timeout=job_completion_timeout,
            async_integration=True,
        )
        payload = {
            "source": source.AMAZON_SELLERS,
            "query": query,
            "domain": domain,
            "geo_location": geo_location,
            "user_agent_type": user_agent_type,
            "render": render,
            "callback_url": callback_url,
            "parse": parse,
            "parsing_instructions": parsing_instructions,
            **kwargs,
        }
        check_parsing_instructions_validity(parsing_instructions)
        response = await self._ecommerce_async_instance._get_resp(
            payload, config
        )
        return response
