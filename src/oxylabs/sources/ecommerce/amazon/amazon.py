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
        request_timeout: Optional[int] = None,
        **kwargs
    ) -> EcommerceResponse:
        """
        Scrapes Amazon search results for a given query.

        Args:
            query (str): The search query.
            opts (dict, optional): Configuration options for the search.
            Defaults to:
                {
                    "domain": com,
                    "start_page": 1,
                    "pages": 1,
                    "geo_location": None,
                    "user_agent_type": desktop,
                    "callback_url": None,
                    "render": None,
                    "parse": None,
                    "context": None,
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
        request_timeout: Optional[int] = None,
        **kwargs
    ) -> EcommerceResponse:
        """
        Scrapes Amazon search results for a given URL.

        Args:
            url (str): The URL to scrape.
            opts (dict, optional): Configuration options for the search.
            Defaults to:
                {
                    "domain": com,
                    "user_agent_type": desktop,
                    "callback_url": None,
                    "render": None,
                    "parse": None,
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
        request_timeout: Optional[int] = None,
        **kwargs
    ) -> EcommerceResponse:
        """
        Scrapes Amazon product details for a given query.

        Args:
            query (str): 10-symbol ASIN code.
            opts (dict, optional): Configuration options for the search.
            Defaults to:
                {
                    "domain": com,
                    "geo_location": None,
                    "user_agent_type": desktop,
                    "callback_url": None,
                    "render": None,
                    "parse": None,
                    "context": None,
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
        request_timeout: Optional[int] = None,
        **kwargs
    ) -> EcommerceResponse:
        """
        Scrapes Amazon pricing details for a given query.

        Args:
            query (str): 10-symbol ASIN code.
            opts (dict, optional): Configuration options for the search.
            Defaults to:
                {
                    "domain": com,
                    "start_page": 1,
                    "pages": 1,
                    "geo_location": None,
                    "user_agent_type": desktop,
                    "callback_url": None,
                    "render": None,
                    "parse": None,
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
        request_timeout: Optional[int] = None,
        **kwargs
    ) -> EcommerceResponse:
        """
        Scrapes Amazon reviews for a given query.

        Args:
            query (str): 10-symbol ASIN code.
            opts (dict, optional): Configuration options for the search.
            Defaults to:
                {
                    "domain": com,
                    "start_page": 1,
                    "pages": 1,
                    "geo_location": None,
                    "user_agent_type": desktop,
                    "callback_url": None,
                    "render": None,
                    "parse": None,
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
        request_timeout: Optional[int] = None,
        **kwargs
    ) -> EcommerceResponse:
        """
        Scrapes Amazon questions for a given query.

        Args:
            query (str): 10-symbol ASIN code.
            opts (dict, optional): Configuration options for the search.
            Defaults to:
                {
                    "domain": com,
                    "geo_location": None,
                    "user_agent_type": desktop,
                    "callback_url": None,
                    "render": None,
                    "parse": None,
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
        request_timeout: Optional[int] = None,
        **kwargs
    ) -> EcommerceResponse:
        """
        Scrapes Amazon bestsellers.

        Args:
            query (str): Browse node ID.
            opts (dict, optional): Configuration options for the search.
            Defaults to:
                {
                    "domain": com,
                    "start_page": 1,
                    "pages": 1,
                    "geo_location": None,
                    "user_agent_type": desktop,
                    "callback_url": None,
                    "render": None,
                    "parse": None,
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
        request_timeout: Optional[int] = None,
        **kwargs
    ) -> EcommerceResponse:
        """
        Scrapes Amazon sellers for a given query.

        Args:
            query (str): 13-character seller ID.
            opts (dict, optional): Configuration options for the search.
            Defaults to:
                {
                    "domain": com,
                    "geo_location": None,
                    "user_agent_type": desktop,
                    "callback_url": None,
                    "render": None,
                    "parse": None,
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
        request_timeout: Optional[int] = None,
        job_completion_timeout: Optional[int] = None,
        poll_interval: Optional[int] = None,
        **kwargs
    ) -> EcommerceResponse:
        """
        Scrapes Amazon search results for a given query.

        Args:
            query (str): The search query.
            opts (dict, optional): Configuration options for the search.
            Defaults to:
                {
                    "domain": com,
                    "start_page": 1,
                    "pages": 1,
                    "geo_location": None,
                    "user_agent_type": desktop,
                    "callback_url": None,
                    "render": None,
                    "parse": None,
                    "context": None,
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
            Defaults to 50

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
        request_timeout: Optional[int] = None,
        job_completion_timeout: Optional[int] = None,
        poll_interval: Optional[int] = None,
        **kwargs
    ) -> EcommerceResponse:
        """
        Scrapes Amazon search results for a given URL.

        Args:
            url (str): The URL to scrape.
            opts (dict, optional): Configuration options for the search.
            Defaults to:
                {
                    "domain": com,
                    "user_agent_type": desktop,
                    "callback_url": None,
                    "render": None,
                    "parse": None,
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
            Defaults to 50

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
        request_timeout: Optional[int] = None,
        job_completion_timeout: Optional[int] = None,
        poll_interval: Optional[int] = None,
        **kwargs
    ) -> EcommerceResponse:
        """
        Scrapes Amazon product details for a given query.

        Args:
            query (str): 10-symbol ASIN code.
            opts (dict, optional): Configuration options for the search.
            Defaults to:
                {
                    "domain": com,
                    "geo_location": None,
                    "user_agent_type": desktop,
                    "callback_url": None,
                    "render": None,
                    "parse": None,
                    "context": None,
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
            Defaults to 50

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
        request_timeout: Optional[int] = None,
        job_completion_timeout: Optional[int] = None,
        poll_interval: Optional[int] = None,
        **kwargs
    ) -> EcommerceResponse:
        """
        Scrapes Amazon pricing details for a given query.

        Args:
            query (str): 10-symbol ASIN code.
            opts (dict, optional): Configuration options for the search.
            Defaults to:
                {
                    "domain": com,
                    "start_page": 1,
                    "pages": 1,
                    "geo_location": None,
                    "user_agent_type": desktop,
                    "callback_url": None,
                    "render": None,
                    "parse": None,
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
            Defaults to 50

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
        request_timeout: Optional[int] = None,
        job_completion_timeout: Optional[int] = None,
        poll_interval: Optional[int] = None,
        **kwargs
    ) -> EcommerceResponse:
        """
        Scrapes Amazon reviews for a given query.

        Args:
            query (str): 10-symbol ASIN code.
            opts (dict, optional): Configuration options for the search.
            Defaults to:
                {
                    "domain": com,
                    "start_page": 1,
                    "pages": 1,
                    "geo_location": None,
                    "user_agent_type": desktop,
                    "callback_url": None,
                    "render": None,
                    "parse": None,
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
            Defaults to 50

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
        request_timeout: Optional[int] = None,
        job_completion_timeout: Optional[int] = None,
        poll_interval: Optional[int] = None,
        **kwargs
    ) -> EcommerceResponse:
        """
        Scrapes Amazon questions for a given query.

        Args:
            query (str): 10-symbol ASIN code.
            opts (dict, optional): Configuration options for the search.
            Defaults to:
                {
                    "domain": com,
                    "geo_location": None,
                    "user_agent_type": desktop,
                    "callback_url": None,
                    "render": None,
                    "parse": None,
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
            Defaults to 50

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
        request_timeout: Optional[int] = None,
        job_completion_timeout: Optional[int] = None,
        poll_interval: Optional[int] = None,
        **kwargs
    ) -> EcommerceResponse:
        """
        Scrapes Amazon bestsellers.

        Args:
            query (str): Browse node ID.
            opts (dict, optional): Configuration options for the search.
            Defaults to:
                {
                    "domain": com,
                    "start_page": 1,
                    "pages": 1,
                    "geo_location": None,
                    "user_agent_type": desktop,
                    "callback_url": None,
                    "render": None,
                    "parse": None,
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
            Defaults to 50

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
        request_timeout: Optional[int] = None,
        job_completion_timeout: Optional[int] = None,
        poll_interval: Optional[int] = None,
        **kwargs
    ) -> EcommerceResponse:
        """
        Scrapes Amazon sellers for a given query.

        Args:
            query (str): 13-character seller ID.
            opts (dict, optional): Configuration options for the search.
            Defaults to:
                {
                    "domain": com,
                    "geo_location": None,
                    "user_agent_type": desktop,
                    "callback_url": None,
                    "render": None,
                    "parse": None,
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
            Defaults to 50

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
