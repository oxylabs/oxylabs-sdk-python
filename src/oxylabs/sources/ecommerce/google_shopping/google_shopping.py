from typing import Optional

from src.oxylabs.sources.ecommerce.response import EcommerceResponse
from src.oxylabs.utils.types import source
from src.oxylabs.utils.utils import (
    check_parsing_instructions_validity,
    prepare_config,
)

from .google_shopping_base import GoogleShoppingBase


class GoogleShopping(GoogleShoppingBase):
    def __init__(self, ecommerce_instance) -> None:
        """
        Initializes an instance of the GoogleShopping class.

        Args:
            ecommerce_instance: The Ecommerce instance associated with the
            GoogleShopping class.
        """
        self._ecommerce_instance = ecommerce_instance

    def scrape_shopping_search(
        self,
        query: str,
        domain: Optional[str] = None,
        start_page: Optional[int] = None,
        pages: Optional[int] = None,
        locale: Optional[str] = None,
        results_language: Optional[str] = None,
        geo_location: Optional[str] = None,
        user_agent_type: Optional[str] = None,
        callback_url: Optional[str] = None,
        render: Optional[str] = None,
        parse: Optional[bool] = None,
        context: Optional[list] = None,
        parsing_instructions: Optional[dict] = None,
        request_timeout: Optional[int] = None,
        **kwargs
    ) -> EcommerceResponse:
        """
        Scrapes Google Shopping search results for a given query.

        Args:
            query (str): UTF-encoded keyword
            opts (dict, optional): Configuration options for the search.
            Defaults to:
                {
                    "domain": com,
                    "start_page": 1,
                    "pages": 1,
                    "locale": None,
                    "results_language": None,
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
            "source": source.GOOGLE_SHOPPING_SEARCH,
            "domain": domain,
            "query": query,
            "start_page": start_page,
            "pages": pages,
            "locale": locale,
            "results_language": results_language,
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

    def scrape_shopping_url(
        self,
        url: str,
        user_agent_type: Optional[str] = None,
        render: Optional[str] = None,
        callback_url: Optional[str] = None,
        geo_location: Optional[str] = None,
        parse: Optional[bool] = None,
        parsing_instructions: Optional[dict] = None,
        request_timeout: Optional[int] = None,
        **kwargs
    ) -> EcommerceResponse:
        """
        Scrapes Google Shopping search results for a given URL.

        Args:
            url (str): Direct URL (link) to Google page
            opts (GoogleShoppingUrlOpts, optional): Configuration options for
            the search. Defaults to:
                {
                    "user_agent_type": desktop,
                    "render": None,
                    "callback_url": None,
                    "geo_location": None,
                    "parse": None,
                    "parsing_instructions": None,
                }
        Returns:
            dict: The response from the server after the job is completed.
        """

        config = prepare_config(request_timeout=request_timeout)
        payload = {
            "source": source.GOOGLE_SHOPPING_URL,
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
        response = self._ecommerce_instance._get_resp(payload, config)
        return response

    def scrape_shopping_products(
        self,
        query: str,
        domain: Optional[str] = None,
        locale: Optional[str] = None,
        results_language: Optional[str] = None,
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
        Scrapes Google Shopping product results for a given query.

        Args:
            query (str): UTF-encoded product code.
            opts (GoogleShoppingProductOpts, optional): Configuration options
            for the search. Defaults to:
                {
                    "domain": com,
                    "locale": None,
                    "results_language": None,
                    "geo_location": None,
                    "user_agent_type": desktop,
                    "render": None,
                    "callback_url": None,
                    "parse": None,
                    "parsing_instructions": None,
                }
        Returns:
            dict: The response from the server after the job is completed.
        """

        config = prepare_config(request_timeout=request_timeout)
        payload = {
            "source": source.GOOGLE_SHOPPING_PRODUCT,
            "query": query,
            "domain": domain,
            "locale": locale,
            "results_language": results_language,
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

    def scrape_product_pricing(
        self,
        query: str,
        domain: Optional[str] = None,
        start_page: Optional[int] = None,
        pages: Optional[int] = None,
        locale: Optional[str] = None,
        results_language: Optional[str] = None,
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
        Scrapes Google Shopping product pricing results for a given product code.

        Args:
            query (str): UTF-encoded product code.
            opts (GoogleShoppingUrlOpts, optional): Configuration options for
            the search. Defaults to:
                {
                    "domain": com,
                    "locale": None,
                    "start_page": 1,
                    "pages": 1,
                    "results_language": None,
                    "geo_location": None,
                    "user_agent_type": desktop,
                    "render": None,
                    "callback_url": None,
                    "parse": None,
                    "parsing_instructions": None,
                }
        Returns:
            dict: The response from the server after the job is completed.
        """

        config = prepare_config(request_timeout=request_timeout)
        payload = {
            "source": source.GOOGLE_SHOPPING_PRICING,
            "domain": domain,
            "query": query,
            "start_page": start_page,
            "pages": pages,
            "locale": locale,
            "results_language": results_language,
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


class GoogleShoppingAsync(GoogleShoppingBase):
    def __init__(self, ecommerce_async_instance) -> None:
        """
        Initializes an instance of the GoogleShoppingAsync class.

        Args:
            ecommerce_async_instance: The EcommerceAsync instance associated
            with the GoogleShoppingAsync class.
        """
        self._ecommerce_async_instance = ecommerce_async_instance

    async def scrape_shopping_search(
        self,
        query: str,
        domain: Optional[str] = None,
        start_page: Optional[int] = None,
        pages: Optional[int] = None,
        locale: Optional[str] = None,
        results_language: Optional[str] = None,
        geo_location: Optional[str] = None,
        user_agent_type: Optional[str] = None,
        callback_url: Optional[str] = None,
        render: Optional[str] = None,
        parse: Optional[bool] = None,
        context: Optional[list] = None,
        parsing_instructions: Optional[dict] = None,
        request_timeout: Optional[int] = None,
        job_completion_timeout: Optional[int] = None,
        poll_interval: Optional[int] = None,
        **kwargs
    ) -> EcommerceResponse:
        """
        Scrapes Google Shopping search results for a given query.

        Args:
            query (str): UTF-encoded keyword.
            opts (dict, optional): Configuration options for the search.
            Defaults to:
                {
                    "domain": com,
                    "start_page": 1,
                    "pages": 1,
                    "locale": None,
                    "results_language": None,
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
            poll_interval (int, optional): The interval in seconds for the
            request to poll the server for a response. Defaults to 5.

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
            "source": source.GOOGLE_SHOPPING_SEARCH,
            "domain": domain,
            "query": query,
            "start_page": start_page,
            "pages": pages,
            "locale": locale,
            "results_language": results_language,
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

    async def scrape_shopping_url(
        self,
        url: str,
        user_agent_type: Optional[str] = None,
        render: Optional[str] = None,
        callback_url: Optional[str] = None,
        geo_location: Optional[str] = None,
        parse: Optional[bool] = None,
        parsing_instructions: Optional[dict] = None,
        request_timeout: Optional[int] = None,
        job_completion_timeout: Optional[int] = None,
        poll_interval: Optional[int] = None,
        **kwargs
    ) -> EcommerceResponse:
        """
        Scrapes Google Shopping search results for a given URL.

        Args:
            url (str): Direct URL (link) to Google page.
            opts (GoogleShoppingUrlOpts, optional): Configuration options for
            the search. Defaults to:
                {
                    "user_agent_type": desktop,
                    "render": None,
                    "callback_url": None,
                    "geo_location": None,
                    "parse": None,
                    "parsing_instructions": None,
                }
            request_timeout (int | 165, optional): The interval in seconds
            for the request to time out if no response is returned.
            Defaults to 165.
            poll_interval (int, optional): The interval in seconds for the
            request to poll the server for a response. Defaults to 5.
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
            "source": source.GOOGLE_SHOPPING_URL,
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
        response = await self._ecommerce_async_instance._get_resp(
            payload, config
        )
        return response

    async def scrape_shopping_products(
        self,
        query: str,
        domain: Optional[str] = None,
        locale: Optional[str] = None,
        results_language: Optional[str] = None,
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
        Scrapes Google Shopping product results for a given query.

        Args:
            query (str): UTF-encoded product code.
            opts (GoogleShoppingProductOpts, optional): Configuration options
            for the search. Defaults to:
                {
                    "domain": com,
                    "locale": None,
                    "results_language": None,
                    "geo_location": None,
                    "user_agent_type": desktop,
                    "render": None,
                    "callback_url": None,
                    "parse": None,
                    "parsing_instructions": None,
                }
            request_timeout (int | 165, optional): The interval in seconds for
            the request to time out if no response is returned.
            Defaults to 165.
            poll_interval (int, optional): The interval in seconds for the
            request to poll the server for a response. Defaults to 5.
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
            "source": source.GOOGLE_SHOPPING_PRODUCT,
            "query": query,
            "domain": domain,
            "locale": locale,
            "results_language": results_language,
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

    async def scrape_product_pricing(
        self,
        query: str,
        domain: Optional[str] = None,
        start_page: Optional[int] = None,
        pages: Optional[int] = None,
        locale: Optional[str] = None,
        results_language: Optional[str] = None,
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
        Scrapes Google Shopping product pricing results for a given product code.

        Args:
            url (str): UTF-encoded product code.
            opts (GoogleShoppingUrlOpts, optional): Configuration options for
            the search. Defaults to:
                {
                    "domain": com,
                    "start_page": 1,
                    "pages": 1,
                    "locale": None,
                    "results_language": None,
                    "geo_location": None,
                    "user_agent_type": desktop,
                    "render": None,
                    "callback_url": None,
                    "parse": None,
                    "parsing_instructions": None,
                }
            request_timeout (int | 165, optional): The interval in seconds for
            the request to time out if no response is returned.
            Defaults to 165.
            poll_interval (int, optional): The interval in seconds for the
            request to poll the server for a response. Defaults to 5.
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
            "source": source.GOOGLE_SHOPPING_PRICING,
            "domain": domain,
            "query": query,
            "start_page": start_page,
            "pages": pages,
            "locale": locale,
            "results_language": results_language,
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
