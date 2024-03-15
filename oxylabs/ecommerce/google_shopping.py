from .google_shopping_base import GoogleShoppingBase
from typing import Optional, Dict, Any
from .ecommerce import Ecommerce, EcommerceAsync
from utils.utils import prepare_config


class GoogleShopping(GoogleShoppingBase):
    def __init__(self, client):
        if not isinstance(client, Ecommerce):
            raise TypeError("GoogleShopping requires an Ecommerce instance")
        self.client = client

    def scrape_google_shopping_search(
        self,
        query: str,
        opts: Optional[Dict[str, Any]] = None,
        timeout: Optional[int] = None,
    ) -> Dict[str, Any]:
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
            timeout (int | 50, optional): The interval in seconds for the request to time out if no response is returned. Defaults to 50.

        Returns:
            dict: The response from the server after the job is completed.
        """

        config = prepare_config(timeout=timeout)
        payload = self._prepare_google_shopping_search_payload(query, opts)
        response = self.client.get_resp(payload, config)
        return response

    def scrape_google_shopping_url(
        self,
        url: str,
        opts: Optional[Dict[str, Any]] = None,
        timeout: Optional[int] = None,
    ) -> Dict[str, Any]:
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

        config = prepare_config(timeout=timeout)
        payload = self._prepare_google_shopping_url_payload(url, opts)
        response = self.client.get_resp(payload, config)
        return response

    def scrape_google_shopping_products(
        self,
        query: str,
        opts: Optional[Dict[str, Any]] = None,
        timeout: Optional[int] = None,
    ) -> Dict[str, Any]:
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

        config = prepare_config(timeout=timeout)
        payload = self._prepare_google_shopping_product_payload(query, opts)
        response = self.client.get_resp(payload, config)
        return response

    def scrape_google_product_pricing(
        self,
        query: str,
        opts: Optional[Dict[str, Any]] = None,
        timeout: Optional[int] = None,
    ) -> Dict[str, Any]:
        """
        Scrapes Google Shopping product pricing results for a given product code.

        Args:
            query (str): UTF-encoded product code.
            opts (GoogleShoppingUrlOpts, optional): Configuration options for the search. Defaults to:
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

        config = prepare_config(timeout=timeout)
        payload = self._prepare_google_shopping_product_pricing_payload(query, opts)
        response = self.client.get_resp(payload, config)
        return response


class GoogleShoppingAsync(GoogleShoppingBase):
    def __init__(self, client):
        if not isinstance(client, EcommerceAsync):
            raise TypeError("GoogleShoppingAsync requires an EcommerceAsync instance")
        self.client = client

    async def scrape_google_shopping_search(
        self,
        query: str,
        opts: Optional[Dict[str, Any]] = None,
        timeout: Optional[int] = None,
        poll_interval: Optional[int] = None,
    ) -> Dict[str, Any]:
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
            timeout (int | 50, optional): The interval in seconds for the request to time out if no response is returned. Defaults to 50.
            poll_interval (int, optional): The interval in seconds for the request to poll the server for a response. Defaults to 2.

        Returns:
            dict: The response from the server after the job is completed.
        """

        config = prepare_config(timeout=timeout, poll_interval=poll_interval)
        payload = self._prepare_google_shopping_search_payload(query, opts)
        response = await self.client.get_resp(payload, config)
        return response

    async def scrape_google_shopping_url(
        self,
        url: str,
        opts: Optional[Dict[str, Any]] = None,
        timeout: Optional[int] = None,
        poll_interval: Optional[int] = None,
    ) -> Dict[str, Any]:
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
                timeout (int | 50, optional): The interval in seconds for the request to time out if no response is returned. Defaults to 50.
                poll_interval (int, optional): The interval in seconds for the request to poll the server for a response. Defaults to 2.
        Returns:
            dict: The response from the server after the job is completed.
        """

        config = prepare_config(timeout=timeout, poll_interval=poll_interval)
        payload = self._prepare_google_shopping_url_payload(url, opts)
        response = await self.client.get_resp(payload, config)
        return response

    async def scrape_google_shopping_products(
        self,
        query: str,
        opts: Optional[Dict[str, Any]] = None,
        timeout: Optional[int] = None,
        poll_interval: Optional[int] = None,
    ) -> Dict[str, Any]:
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
            timeout (int | 50, optional): The interval in seconds for the request to time out if no response is returned. Defaults to 50.
            poll_interval (int, optional): The interval in seconds for the request to poll the server for a response. Defaults to 2.
        Returns:
            dict: The response from the server after the job is completed.
        """

        config = prepare_config(timeout=timeout, poll_interval=poll_interval)
        payload = self._prepare_google_shopping_product_payload(query, opts)
        response = await self.client.get_resp(payload, config)
        return response

    async def scrape_google_product_pricing(
        self,
        query: str,
        opts: Optional[Dict[str, Any]] = None,
        timeout: Optional[int] = None,
        poll_interval: Optional[int] = None,
    ) -> Dict[str, Any]:
        """
        Scrapes Google Shopping product pricing results for a given product code.

        Args:
            url (str): UTF-encoded product code.
            opts (GoogleShoppingUrlOpts, optional): Configuration options for the search. Defaults to:
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
            timeout (int | 50, optional): The interval in seconds for the request to time out if no response is returned. Defaults to 50.
            poll_interval (int, optional): The interval in seconds for the request to poll the server for a response. Defaults to 2.
        Returns:
            dict: The response from the server after the job is completed.
        """

        config = prepare_config(timeout=timeout, poll_interval=poll_interval)
        payload = self._prepare_google_shopping_product_pricing_payload(query, opts)
        response = await self.client.get_resp(payload, config)
        return response
