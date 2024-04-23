from .bing_base import BingBase
from typing import Optional, Dict, Any

# from .serp import SERP, SERPAsync
from src.oxylabs.utils.utils import prepare_config


class Bing(BingBase):
    def __init__(self, serp_instance) -> None:
        """
        Initializes an instance of the Bing class.

        Args:
            serp_instance: The SERP instance associated with the Bing class.
        """
        self._serp_instance = serp_instance

    def scrape_search(
        self,
        query: str,
        opts: Optional[dict] = None,
        timeout: Optional[int] = None,
    ) -> dict:
        """
        Scrapes Bing search results for a given query.

        Args:
            query (str): The search query.
            opts (dict, optional): Configuration options for the search. Defaults to:
                {
                    "domain": com,
                    "start_page": 1,
                    "pages": 1,
                    "limit": 10,
                    "user_agent_type": desktop,
                    "callback_url": None,
                    "locale": None,
                    "geo_location": None,
                    "render": None,
                    "parse": None,
                }
                This parameter allows customization of the search request.
            timeout (int | 50, optional): The interval in seconds for the request to time out if no response is returned. Defaults to 50.

        Returns:
            dict: The response from the server after the job is completed.
        """
        config = prepare_config(timeout=timeout)
        payload = self._prepare_search_payload(query, opts)
        response = self._serp_instance.get_resp(payload, config)
        return response

    def scrape_url(
        self,
        url: str,
        opts: Optional[dict] = None,
        timeout: Optional[int] = None,
    ) -> dict:
        """
        Scrapes Bing search results for a given URL.

        Args:
            url (str): The URL to be scraped.
            opts (BingUrlOpts, optional): Configuration options for the search. Defaults to:
                {
                    "user_agent_type": desktop,
                    "geo_location": None,
                    "callback_url": None,
                    "render": None,
                    "parsing_instructions": None,
                    "parse": None,
                }
                This parameter allows customization of the search request.
            timeout (int | 50, optional): The interval in seconds for the request to time out if no response is returned. Defaults to 50.

        Returns:
            dict: The response from the server after the job is completed.
        """

        config = prepare_config(timeout=timeout)
        payload = self._prepare_url_payload(url, opts)
        response = self._serp_instance.get_resp(payload, config)
        return response


class BingAsync(BingBase):
    def __init__(self, serp_async_instance) -> None:
        """
        Initializes an instance of the BingAsync class.

        Args:
            serp_async_instance: The SERPAsync instance associated with the BingAsync class.
        """
        self._serp_async_instance = serp_async_instance

    async def scrape_search(
        self,
        query: str,
        opts: Optional[dict] = None,
        timeout: Optional[int] = None,
        poll_interval: Optional[int] = None,
    ) -> dict:
        """
        Asynchronously scrapes Bing search results for a given query.

        Args:
            query (str): The search query.
            opts (dict, optional): Configuration options for the search. Defaults to:
                {
                    "domain": com,
                    "start_page": 1,
                    "pages": 1,
                    "limit": 10,
                    "user_agent_type": desktop,
                    "callback_url": None,
                    "locale": None,
                    "geo_location": None,
                    "render": None,
                    "parse": None,
                }
                This parameter allows customization of the search request.
            timeout (int | 50, optional): The interval in seconds for the request to time out if no response is returned. Defaults to 50.
            poll_interval (int | 2, optional): The interval in seconds between status checks for the asynchronous job. Defaults to 2.

        Returns:
            dict: The response from the server after the job is completed.
        """

        config = prepare_config(poll_interval=poll_interval, timeout=timeout)
        payload = self._prepare_search_payload(query, opts)
        response = await self._serp_async_instance.get_resp(payload, config)
        return response

    async def scrape_url(
        self,
        url: str,
        opts: Optional[dict] = None,
        timeout: Optional[int] = None,
        poll_interval: Optional[int] = None,
    ) -> dict:
        """
        Asynchronously scrapes Bing search results for a given URL.

        Args:
            url (str): The URL to be scraped.
            opts (BingUrlOpts, optional): Configuration options for the search. Defaults to:
                {
                    "user_agent_type": desktop,
                    "geo_location": None,
                    "callback_url": None,
                    "render": None,
                    "parsing_instructions": None,
                    "parse": None,
                }
                This parameter allows customization of the search request.
            timeout (int | 50, optional): The interval in seconds for the request to time out if no response is returned. Defaults to 50.
            poll_interval (int | 2, optional): The interval in seconds between status checks for the asynchronous job. Defaults to 2.

        Returns:
            dict: The response from the server after the job is completed.
        """

        config = prepare_config(poll_interval=poll_interval, timeout=timeout)
        payload = self._prepare_url_payload(url, opts)
        response = await self._serp_async_instance.get_resp(payload, config)
        return response
