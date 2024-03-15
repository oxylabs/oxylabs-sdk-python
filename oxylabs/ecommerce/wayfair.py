from .wayfair_base import WayfairBase
from typing import Optional, Dict, Any
from .ecommerce import InitEcommerce, InitEcommerceAsync
from utils.utils import prepare_config


class Wayfair(WayfairBase):
    def __init__(self, client):
        if not isinstance(client, InitEcommerce):
            raise TypeError("Wayfair requires a Ecommerce instance")
        self.client = client

    def scrape_wayfair_search(
        self,
        query: str,
        opts: Optional[Dict[str, Any]] = None,
        timeout: Optional[int] = None,
    ) -> Dict[str, Any]:
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
                }
                This parameter allows customization of the search request.
            timeout (int | 50, optional): The interval in seconds for the request to time out if no response is returned. Defaults to 50.

        Returns:
            dict: The response from the server after the job is completed.
        """

        config = prepare_config(timeout=timeout)
        payload = self._prepare_wayfair_search_payload(query, opts)
        response = self.client.get_resp(payload, config)
        return response

    def scrape_wayfair_url(
        self,
        url: str,
        opts: Optional[Dict[str, Any]] = None,
        timeout: Optional[int] = None,
    ) -> Dict[str, Any]:
        """
        Scrapes Wayfair search results for a given URL.

        Args:
            url (str): The URL to be scraped.
            opts (WayfairUrlOpts, optional): Configuration options for the search. Defaults to:
                {
                    "user_agent_type": desktop,
                    "callback_url": None,
                }
                This parameter allows customization of the search request.
            timeout (int | 50, optional): The interval in seconds for the request to time out if no response is returned. Defaults to 50.

        Returns:
            dict: The response from the server after the job is completed.
        """

        config = prepare_config(timeout=timeout)
        payload = self._prepare_wayfair_url_payload(url, opts)
        response = self.client.get_resp(payload, config)
        return response


class WayfairAsync(WayfairBase):
    def __init__(self, client):
        if not isinstance(client, InitEcommerceAsync):
            raise TypeError("WayfairAsync requires a EcommerceAsync instance")
        self.client = client

    async def scrape_wayfair_search(
        self,
        query: str,
        opts: Optional[Dict[str, Any]] = None,
        timeout: Optional[int] = None,
        poll_interval: Optional[int] = None,
    ) -> Dict[str, Any]:
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
                }
                This parameter allows customization of the search request.
            timeout (int | 50, optional): The interval in seconds for the request to time out if no response is returned. Defaults to 50.
            poll_interval (int | 2, optional): The interval in seconds between status checks for the asynchronous job. Defaults to 2.

        Returns:
            dict: The response from the server after the job is completed.
        """

        config = prepare_config(timeout=timeout, poll_interval=poll_interval)
        payload = self._prepare_wayfair_search_payload(query, opts)
        response = await self.client.get_resp(payload, config)
        return response

    async def scrape_wayfair_url(
        self,
        url: str,
        opts: Optional[Dict[str, Any]] = None,
        timeout: Optional[int] = None,
        poll_interval: Optional[int] = None,
    ) -> Dict[str, Any]:
        """
        Asynchronously scrapes Wayfair search results for a given URL.

        Args:
            url (str): The URL to be scraped.
            opts (WayfairUrlOpts, optional): Configuration options for the search. Defaults to:
                {
                    "user_agent_type": desktop,
                    "geo_location": None,
                    "callback_url": None,
                    "render": None,
                    "parsing_instructions": None,
                }
                This parameter allows customization of the search request.
            timeout (int | 50, optional): The interval in seconds for the request to time out if no response is returned. Defaults to 50.
            poll_interval (int | 2, optional): The interval in seconds between status checks for the asynchronous job. Defaults to 2.

        Returns:
            dict: The response from the server after the job is completed.
        """

        config = prepare_config(timeout=timeout, poll_interval=poll_interval)
        payload = self._prepare_wayfair_url_payload(url, opts)
        response = await self.client.get_resp(payload, config)
        return response
