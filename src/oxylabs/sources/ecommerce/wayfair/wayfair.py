from .wayfair_base import WayfairBase
from typing import Optional, Dict, Any
from src.oxylabs.utils.utils import prepare_config


class Wayfair(WayfairBase):
    def __init__(self, ecommerce_instance) -> None:
        """
        Initializes an instance of the Wayfair class.

        Args:
            ecommerce_instance: The Ecommerce instance associated with the Wayfair class.
        """
        self._ecommerce_instance = ecommerce_instance

    def scrape_search(
        self,
        query: str,
        opts: Optional[dict] = None,
        timeout: Optional[int] = None,
    ) -> dict:
        """
        Scrapes Wayfair search results for a given query.

        Args:
            query (str): The search query.
            opts (dict, optional): Configuration options for the search. Defaults to:
                {
                    "start_page": 1,
                    "pages": 1,
                    "limit": 48,
                    "user_agent_type": desktop,
                    "callback_url": None,
                    "parsing_instructions": None,
                }
                This parameter allows customization of the search request.
            timeout (int | 50, optional): The interval in seconds for the request to time out if no response is returned. Defaults to 50.

        Returns:
            dict: The response from the server after the job is completed.
        """

        config = prepare_config(timeout=timeout)
        payload = self._prepare_search_payload(query, opts)
        response = self._ecommerce_instance.get_resp(payload, config)
        return response

    def scrape_url(
        self,
        url: str,
        opts: Optional[dict] = None,
        timeout: Optional[int] = None,
    ) -> dict:
        """
        Scrapes Wayfair search results for a given URL.

        Args:
            url (str): The URL to be scraped.
            opts (WayfairUrlOpts, optional): Configuration options for the search. Defaults to:
                {
                    "user_agent_type": desktop,
                    "callback_url": None,
                    "parsing_instructions": None,
                }
                This parameter allows customization of the search request.
            timeout (int | 50, optional): The interval in seconds for the request to time out if no response is returned. Defaults to 50.

        Returns:
            dict: The response from the server after the job is completed.
        """

        config = prepare_config(timeout=timeout)
        payload = self._prepare_url_payload(url, opts)
        response = self._ecommerce_instance.get_resp(payload, config)
        return response


class WayfairAsync(WayfairBase):
    def __init__(self, ecommerce_async_instance) -> None:
        """
        Initializes an instance of the WayfairAsync class.

        Args:
            ecommerce_async_instance: The EcommerceAsync instance associated with the WayfairAsync class.
        """
        self._ecommerce_async_instance = ecommerce_async_instance

    async def scrape_search(
        self,
        query: str,
        opts: Optional[dict] = None,
        timeout: Optional[int] = None,
        poll_interval: Optional[int] = None,
    ) -> dict:
        """
        Asynchronously scrapes Wayfair search results for a given query.

        Args:
            query (str): The search query.
            opts (dict, optional): Configuration options for the search. Defaults to:
                {
                    "start_page": 1,
                    "pages": 1,
                    "limit": 48,
                    "user_agent_type": desktop,
                    "callback_url": None,
                    "parsing_instructions": None,
                }
                This parameter allows customization of the search request.
            timeout (int | 50, optional): The interval in seconds for the request to time out if no response is returned. Defaults to 50.
            poll_interval (int | 2, optional): The interval in seconds between status checks for the asynchronous job. Defaults to 2.

        Returns:
            dict: The response from the server after the job is completed.
        """

        config = prepare_config(timeout=timeout, poll_interval=poll_interval)
        payload = self._prepare_search_payload(query, opts)
        response = await self._ecommerce_async_instance.get_resp(payload, config)
        return response

    async def scrape_url(
        self,
        url: str,
        opts: Optional[dict] = None,
        timeout: Optional[int] = None,
        poll_interval: Optional[int] = None,
    ) -> dict:
        """
        Asynchronously scrapes Wayfair search results for a given URL.

        Args:
            url (str): The URL to be scraped.
            opts (WayfairUrlOpts, optional): Configuration options for the search. Defaults to:
                {
                    "user_agent_type": desktop,
                    "callback_url": None,
                    "parsing_instructions": None,
                }
                This parameter allows customization of the search request.
            timeout (int | 50, optional): The interval in seconds for the request to time out if no response is returned. Defaults to 50.
            poll_interval (int | 2, optional): The interval in seconds between status checks for the asynchronous job. Defaults to 2.

        Returns:
            dict: The response from the server after the job is completed.
        """

        config = prepare_config(timeout=timeout, poll_interval=poll_interval)
        payload = self._prepare_url_payload(url, opts)
        response = await self._ecommerce_async_instance.get_resp(payload, config)
        return response
