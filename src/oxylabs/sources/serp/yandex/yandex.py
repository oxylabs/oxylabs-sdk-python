from .yandex_base import YandexBase

# from .serp import SERP, SERPAsync
from src.oxylabs.utils.utils import prepare_config
from typing import Optional, Dict, Any


class Yandex(YandexBase):
    def __init__(self, serp_instance) -> None:
        """
        Initializes an instance of the Yandex class.

        Args:
            serp_instance: The SERP instance associated with the Yandex class.
        """
        self._serp_instance = serp_instance

    def scrape_search(
        self,
        query: str,
        opts: Optional[dict] = None,
        request_timeout: Optional[int] = None,
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

        config = prepare_config(request_timeout=request_timeout)
        payload = self._prepare_search_payload(query, opts)
        response = self._serp_instance.get_resp(payload, config)
        return response

    def scrape_url(
        self,
        url: str,
        opts: Optional[dict] = None,
        request_timeout: Optional[int] = None,
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

        config = prepare_config(request_timeout=request_timeout)
        payload = self._prepare_url_payload(url, opts)
        response = self._serp_instance.get_resp(payload, config)
        return response


class YandexAsync(YandexBase):
    def __init__(self, serp_async_instance):
        """
        Initializes an asynchronous Yandex client.

        Args:
            serp_async_instance (SERPAsync): The SERPAsync instance to be used for Yandex requests.
        """
        self._serp_async_instance = serp_async_instance

    async def scrape_search(
        self,
        query: str,
        opts: Optional[dict] = None,
        request_timeout: Optional[int] = None,
        job_completion_timeout: Optional[int] = None,
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

        config = prepare_config(
            request_timeout=request_timeout,
            poll_interval=poll_interval,
            job_completion_timeout=job_completion_timeout,
            async_integration=True,
        )
        payload = self._prepare_search_payload(query, opts)
        response = await self._serp_async_instance.get_resp(payload, config)
        return response

    async def scrape_url(
        self,
        url: str,
        opts: Optional[dict] = None,
        request_timeout: Optional[int] = None,
        job_completion_timeout: Optional[int] = None,
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

        config = prepare_config(
            request_timeout=request_timeout,
            poll_interval=poll_interval,
            job_completion_timeout=job_completion_timeout,
            async_integration=True,
        )
        payload = self._prepare_url_payload(url, opts)
        response = await self._serp_async_instance.get_resp(payload, config)
        return response
