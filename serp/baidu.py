from serp.baidu_base import BaiduBase
from serp.serp import Serp, SerpAsync
from utils.utils import prepare_config
from typing import Optional, Dict, Any


class Baidu(BaiduBase):
    def __init__(self, client):
        if not isinstance(client, Serp):
            raise TypeError("Baidu requires a Serp instance")
        self.client = client

    def scrape_baidu_search(
        self, query: str, opts: Optional[Dict[str, Any]] = None, timeout: int = None
    ) -> Dict[str, Any]:
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
                    "parse_instructions": None,
                }
                This parameter allows customization of the search request.
            timeout (int | None, optional): The interval in seconds for the request to time out if no response is returned. Defaults to None.

        Returns:
            dict: The response from the server after the job is completed.
        """

        config = prepare_config(timeout=timeout)
        payload = self.prepare_search_payload(query, opts)
        response = self.client.get_resp(payload, config)
        return response

    def scrape_baidu_url(
        self, url: str, opts: Optional[Dict[str, Any]] = None, timeout: int = None
    ) -> Dict[str, Any]:
        """
        Scrapes Baidu search results for a given URL.

        Args:
            url (str): The URL to be scraped.
            opts (BaiduUrlOpts, optional): Configuration options for the search. Defaults to:
                {
                    "user_agent_type": desktop,
                    "callback_url": None,
                    "parse_instructions": None,
                }
                This parameter allows customization of the search request.
            timeout (int | None, optional): The interval in seconds for the request to time out if no response is returned. Defaults to None.

        Returns:
            dict: The response from the server after the job is completed.
        """
        
        config = prepare_config(timeout=timeout)
        payload = self.prepare_url_payload(url, opts)
        response = self.client.get_resp(payload, config)
        return response
    
class BaiduAsync(BaiduBase):
    def __init__(self, client):
        if not isinstance(client, SerpAsync):
            raise TypeError("BaiduAsync requires a SerpAsync instance")
        self.client = client

    async def scrape_baidu_search(
        self, query: str, opts: Optional[Dict[str, Any]] = None, timeout: int = None
    ) -> Dict[str, Any]:
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
                    "parse_instructions": None,
                }
                This parameter allows customization of the search request.
            timeout (int | None, optional): The interval in seconds for the request to time out if no response is returned. Defaults to None.

        Returns:
            dict: The response from the server after the job is completed.
        """

        config = prepare_config(timeout=timeout)
        payload = self.prepare_search_payload(query, opts)
        response = await self.client.get_resp(payload, config)
        return response

    async def scrape_baidu_url(
        self, url: str, opts: Optional[Dict[str, Any]] = None, timeout: int = None
    ) -> Dict[str, Any]:
        """
        Asynchronously scrapes Baidu search results for a given URL.

        Args:
            url (str): The URL to be scraped.
            opts (BaiduUrlOpts, optional): Configuration options for the search. Defaults to:
                {
                    "user_agent_type": desktop,
                    "callback_url": None,
                    "parse_instructions": None,
                }
                This parameter allows customization of the search request.
            timeout (int | None, optional): The interval in seconds for the request to time out if no response is returned. Defaults to None.

        Returns:
            dict: The response from the server after the job is completed.
        """
        
        config = prepare_config(timeout=timeout)
        payload = self.prepare_url_payload(url, opts)
        response = await self.client.get_resp(payload, config)
        return response
