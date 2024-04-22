from .baidu_base import BaiduBase

# from .serp import SERP, SERPAsync
from oxylabs.utils.utils import prepare_config
from typing import Optional, Dict, Any


class Baidu(BaiduBase):
    def __init__(self, serp_instance) -> None:
        """
        Initializes an instance of the Baidu class.

        Args:
            serp_instance: The SERP instance associated with the Baidu class.
        """
        self._serp_instance = serp_instance

    def scrape_search(
        self,
        query: str,
        opts: Optional[dict] = None,
        timeout: Optional[int] = None,
    ) -> dict:
        """
        Scrapes Baidu search results for a given query.

        Args:
            query (str): The search query.
            opts (BaiduSearchOpts, optional): Configuration options for the search. Defaults to:
                {
                    "domain": com,
                    "start_page": 1,
                    "pages": 1,
                    "limit": 10,
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
        response = self._serp_instance.get_resp(payload, config)
        return response

    def scrape_url(
        self,
        url: str,
        opts: Optional[dict] = None,
        timeout: Optional[int] = None,
    ) -> dict:
        """
        Scrapes Baidu search results for a given URL.

        Args:
            url (str): The URL to be scraped.
            opts (BaiduUrlOpts, optional): Configuration options for the search. Defaults to:
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
        response = self._serp_instance.get_resp(payload, config)
        return response


class BaiduAsync(BaiduBase):
    def __init__(self, serp_async_instance) -> None:
        """
        Initializes an instance of the BaiduAsync class.

        Args:
            serp_async_instance: The SERPAsync instance associated with the BaiduAsync class.
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
        Asynchronously scrapes Baidu search results for a given query.

        Args:
            query (str): The search query.
            opts (BaiduSearchOpts, optional): Configuration options for the search. Defaults to:
                {
                    "domain": com,
                    "start_page": 1,
                    "pages": 1,
                    "limit": 10,
                    "user_agent_type": desktop,
                    "callback_url": None,
                    "parsing_instructions": None,
                }
                This parameter allows customization of the search request.
            timeout (int | 50, optional): The interval in seconds for the request to time out if no response is returned. Defaults to 50.
            poll_interval (int | 2, optional): The interval in seconds for the request to poll the server for a response. Defaults to 2.

        Returns:
            dict: The response from the server after the job is completed.
        """

        config = prepare_config(timeout=timeout, poll_interval=poll_interval)
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
        Asynchronously scrapes Baidu search results for a given URL.

        Args:
            url (str): The URL to be scraped.
            opts (BaiduUrlOpts, optional): Configuration options for the search. Defaults to:
                {
                    "user_agent_type": desktop,
                    "callback_url": None,
                    "parsing_instructions": None,
                }
                This parameter allows customization of the search request.
            timeout (int | 50, optional): The interval in seconds for the request to time out if no response is returned. Defaults to 50.
            poll_interval (int | 2, optional): The interval in seconds for the request to poll the server for a response. Defaults to 2.

        Returns:
            dict: The response from the server after the job is completed.
        """

        config = prepare_config(timeout=timeout, poll_interval=poll_interval)
        payload = self._prepare_url_payload(url, opts)
        response = await self._serp_async_instance.get_resp(payload, config)
        return response
