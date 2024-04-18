from .yandex_base import YandexBase
from .serp import InitSerp, InitSerpAsync
from oxylabs.utils.utils import prepare_config
from typing import Optional, Dict, Any


class Yandex(YandexBase):
    def __init__(self, client: InitSerp):
        """
        Initializes a Yandex instance.

        Args:
            client (Serp): The Serp instance to be used for Yandex requests.

        Raises:
            TypeError: If the client parameter is not an instance of Serp.
        """
        if not isinstance(client, InitSerp):
            raise TypeError("Yandex requires a Serp instance")
        self.client = client

    def scrape_yandex_search(
        self,
        query: str,
        opts: Optional[dict] = None,
        timeout: Optional[int] = None,
    ) -> dict:
        """
        Scrapes the search results from Yandex.

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
                }
                This parameter allows customization of the search request.

            timeout (int, optional): The interval in seconds for the request to time out if no response is returned. Defaults to 50.

        Returns:

            dict: The response from the server after the job is completed.
        """

        config = prepare_config(timeout=timeout)
        payload = self._prepare_yandex_search_payload(query, opts)
        response = self.client.get_resp(payload, config)
        return response

    def scrape_yandex_url(
        self,
        url: str,
        opts: Optional[dict] = None,
        timeout: Optional[int] = None,
    ) -> dict:
        """
        Scrapes Yandex search results for a given URL.

        Args:
            url (str): The URL to be scraped.
            opts (YandexUrlOpts, optional): Configuration options for the search. Defaults to:
                {
                    "user_agent_type": desktop,
                    "callback_url": None,
                    "render": None,
                    "parsing_instructions": None,
                }
                This parameter allows customization of the search request.
            timeout (int | 50, optional): The interval in seconds for the request to time out if no response is returned. Defaults to 50.

        Returns:
            dict: The response from the server after the job is completed.
        """

        config = prepare_config(timeout=timeout)
        payload = self._prepare_yandex_url_payload(url, opts)
        response = self.client.get_resp(payload, config)
        return response


class YandexAsync(YandexBase):
    def __init__(self, client: InitSerpAsync):
        """
        Initializes a YandexAsync instance.

        Args:
            client (SerpAsync): The SerpAsync instance to be used for making requests.

        Raises:
            TypeError: If the client parameter is not an instance of SerpAsync.
        """
        if not isinstance(client, InitSerpAsync):
            raise TypeError("YandexAsync requires a SerpAsync instance")
        self.client = client

    async def scrape_yandex_search(
        self,
        query: str,
        opts: Optional[dict] = None,
        timeout: Optional[int] = None,
        poll_interval: Optional[int] = None,
    ) -> dict:
        """
        Asynchronously scrapes the search results from Yandex.

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
                }
                This parameter allows customization of the search request.

            timeout (int, optional): The interval in seconds for the request to time out if no response is returned. Defaults to 50.
            poll_interval (int, optional): The interval in seconds for the request to poll the server for the job completion status. Defaults to 2.

        Returns:

            dict: The response from the server after the job is completed.
        """

        config = prepare_config(timeout=timeout, poll_interval=poll_interval)
        payload = self._prepare_yandex_search_payload(query, opts)
        response = await self.client.get_resp(payload, config)
        return response

    async def scrape_yandex_url(
        self,
        url: str,
        opts: Optional[dict] = None,
        timeout: Optional[int] = None,
        poll_interval: Optional[int] = None,
    ) -> dict:
        """
        Asynchronously scrapes Yandex search results for a given URL.

        Args:
            url (str): The URL to be scraped.
            opts (YandexUrlOpts, optional): Configuration options for the search. Defaults to:
                {
                    "user_agent_type": desktop,
                    "callback_url": None,
                    "render": None,
                    "parsing_instructions": None,
                }
                This parameter allows customization of the search request.
            timeout (int | 50, optional): The interval in seconds for the request to time out if no response is returned. Defaults to 50.
            poll_interval (int | 2, optional): The interval in seconds for the request to poll the server for a response. Defaults to 2.

        Returns:
            dict: The response from the server after the job is completed.
        """

        config = prepare_config(timeout=timeout, poll_interval=poll_interval)
        payload = self._prepare_yandex_url_payload(url, opts)
        response = await self.client.get_resp(payload, config)
        return response
