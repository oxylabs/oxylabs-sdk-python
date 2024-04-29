from typing import Optional

from src.oxylabs.utils.utils import prepare_config

from .google_shopping_base import GoogleShoppingBase


class GoogleShopping(GoogleShoppingBase):
    def __init__(self, ecommerce_instance) -> None:
        """
        Initializes an instance of the GoogleShopping class.

        Args:
            ecommerce_instance: The Ecommerce instance associated with the GoogleShopping class.
        """
        self._ecommerce_instance = ecommerce_instance

    def scrape_shopping_search(
        self,
        query: str,
        opts: Optional[dict] = None,
        request_timeout: Optional[int] = None,
    ) -> dict:
        """
        Scrapes Google Shopping search results for a given query.

        Args:
            query (str): UTF-encoded keyword
            opts (dict, optional): Configuration options for the search. Defaults to:
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
            request_timeout (int | 160, optional): The interval in seconds for the request to time out if no response is returned. Defaults to 160.

        Returns:
            dict: The response from the server after the job is completed.
        """

        config = prepare_config(request_timeout=request_timeout)
        payload = self._prepare_shopping_search_payload(query, opts)
        response = self._ecommerce_instance._get_resp(payload, config)
        return response

    def scrape_shopping_url(
        self,
        url: str,
        opts: Optional[dict] = None,
        request_timeout: Optional[int] = None,
    ) -> dict:
        """
        Scrapes Google Shopping search results for a given URL.

        Args:
            url (str): Direct URL (link) to Google page
            opts (GoogleShoppingUrlOpts, optional): Configuration options for the search. Defaults to:
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
        payload = self._prepare_shopping_url_payload(url, opts)
        response = self._ecommerce_instance._get_resp(payload, config)
        return response

    def scrape_shopping_products(
        self,
        query: str,
        opts: Optional[dict] = None,
        request_timeout: Optional[int] = None,
    ) -> dict:
        """
        Scrapes Google Shopping product results for a given query.

        Args:
            query (str): UTF-encoded product code.
            opts (GoogleShoppingProductOpts, optional): Configuration options for the search. Defaults to:
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
        payload = self._prepare_shopping_product_payload(query, opts)
        response = self._ecommerce_instance._get_resp(payload, config)
        return response

    def scrape_product_pricing(
        self,
        query: str,
        opts: Optional[dict] = None,
        request_timeout: Optional[int] = None,
    ) -> dict:
        """
        Scrapes Google Shopping product pricing results for a given product code.

        Args:
            query (str): UTF-encoded product code.
            opts (GoogleShoppingUrlOpts, optional): Configuration options for the search. Defaults to:
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
        payload = self._prepare_shopping_product_pricing_payload(query, opts)
        response = self._ecommerce_instance._get_resp(payload, config)
        return response


class GoogleShoppingAsync(GoogleShoppingBase):
    def __init__(self, ecommerce_async_instance) -> None:
        """
        Initializes an instance of the GoogleShoppingAsync class.

        Args:
            ecommerce_async_instance: The EcommerceAsync instance associated with the GoogleShoppingAsync class.
        """
        self._ecommerce_async_instance = ecommerce_async_instance

    async def scrape_shopping_search(
        self,
        query: str,
        opts: Optional[dict] = None,
        request_timeout: Optional[int] = None,
        job_completion_timeout: Optional[int] = None,
        poll_interval: Optional[int] = None,
    ) -> dict:
        """
        Scrapes Google Shopping search results for a given query.

        Args:
            query (str): UTF-encoded keyword.
            opts (dict, optional): Configuration options for the search. Defaults to:
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
            request_timeout (int | 160, optional): The interval in seconds for the request to time out if no response is returned. Defaults to 160.
            poll_interval (int, optional): The interval in seconds for the request to poll the server for a response. Defaults to 2.

        Returns:
            dict: The response from the server after the job is completed.
        """

        config = prepare_config(
            request_timeout=request_timeout,
            poll_interval=poll_interval,
            job_completion_timeout=job_completion_timeout,
            async_integration=True,
        )
        payload = self._prepare_shopping_search_payload(query, opts)
        response = await self._ecommerce_async_instance._get_resp(
            payload, config
        )
        return response

    async def scrape_shopping_url(
        self,
        url: str,
        opts: Optional[dict] = None,
        request_timeout: Optional[int] = None,
        job_completion_timeout: Optional[int] = None,
        poll_interval: Optional[int] = None,
    ) -> dict:
        """
        Scrapes Google Shopping search results for a given URL.

        Args:
            url (str): Direct URL (link) to Google page.
            opts (GoogleShoppingUrlOpts, optional): Configuration options for the search. Defaults to:
                {
                    "user_agent_type": desktop,
                    "render": None,
                    "callback_url": None,
                    "geo_location": None,
                    "parse": None,
                    "parsing_instructions": None,
                }
                request_timeout (int | 160, optional): The interval in seconds for the request to time out if no response is returned. Defaults to 160.
                poll_interval (int, optional): The interval in seconds for the request to poll the server for a response. Defaults to 2.
        Returns:
            dict: The response from the server after the job is completed.
        """

        config = prepare_config(
            request_timeout=request_timeout,
            poll_interval=poll_interval,
            job_completion_timeout=job_completion_timeout,
            async_integration=True,
        )
        payload = self._prepare_shopping_url_payload(url, opts)
        response = await self._ecommerce_async_instance._get_resp(
            payload, config
        )
        return response

    async def scrape_shopping_products(
        self,
        query: str,
        opts: Optional[dict] = None,
        request_timeout: Optional[int] = None,
        job_completion_timeout: Optional[int] = None,
        poll_interval: Optional[int] = None,
    ) -> dict:
        """
        Scrapes Google Shopping product results for a given query.

        Args:
            query (str): UTF-encoded product code.
            opts (GoogleShoppingProductOpts, optional): Configuration options for the search. Defaults to:
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
            request_timeout (int | 160, optional): The interval in seconds for the request to time out if no response is returned. Defaults to 160.
            poll_interval (int, optional): The interval in seconds for the request to poll the server for a response. Defaults to 2.
        Returns:
            dict: The response from the server after the job is completed.
        """

        config = prepare_config(
            request_timeout=request_timeout,
            poll_interval=poll_interval,
            job_completion_timeout=job_completion_timeout,
            async_integration=True,
        )
        payload = self._prepare_shopping_product_payload(query, opts)
        response = await self._ecommerce_async_instance._get_resp(
            payload, config
        )
        return response

    async def scrape_product_pricing(
        self,
        query: str,
        opts: Optional[dict] = None,
        request_timeout: Optional[int] = None,
        job_completion_timeout: Optional[int] = None,
        poll_interval: Optional[int] = None,
    ) -> dict:
        """
        Scrapes Google Shopping product pricing results for a given product code.

        Args:
            url (str): UTF-encoded product code.
            opts (GoogleShoppingUrlOpts, optional): Configuration options for the search. Defaults to:
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
            request_timeout (int | 160, optional): The interval in seconds for the request to time out if no response is returned. Defaults to 160.
            poll_interval (int, optional): The interval in seconds for the request to poll the server for a response. Defaults to 2.
        Returns:
            dict: The response from the server after the job is completed.
        """

        config = prepare_config(
            request_timeout=request_timeout,
            poll_interval=poll_interval,
            job_completion_timeout=job_completion_timeout,
            async_integration=True,
        )
        payload = self._prepare_shopping_product_pricing_payload(query, opts)
        response = await self._ecommerce_async_instance._get_resp(
            payload, config
        )
        return response
