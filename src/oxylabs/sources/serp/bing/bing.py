from typing import Optional

from src.oxylabs.utils.types import source
from src.oxylabs.utils.utils import prepare_config, check_parsing_instructions_validity

from .bing_base import BingBase


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
        domain: Optional[str] = None,
        start_page: Optional[int] = None,
        pages: Optional[int] = None,
        limit: Optional[int] = None,
        user_agent_type: Optional[str] = None,
        callback_url: Optional[str] = None,
        locale: Optional[str] = None,
        geo_location: Optional[str] = None,
        render: Optional[str] = None,
        parse: Optional[bool] = None,
        parsing_instructions: Optional[dict] = None,
        request_timeout: Optional[int] = None,
        **kwargs,
    ) -> dict:
        """
        Scrapes Bing search results for a given query.

        Args:
            query (str): The search query.
            opts (dict, optional): Configuration options for the search.
            Defaults to:
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
            request_timeout (int | 165, optional): The interval in seconds for
            the request to time out if no response is returned.
            Defaults to 165.

        Returns:
            dict: The response from the server after the job is completed.
        """

        config = prepare_config(request_timeout=request_timeout)
        payload = {
            "source": source.BING_SEARCH,
            "domain": domain,
            "query": query,
            "start_page": start_page,
            "pages": pages,
            "limit": limit,
            "locale": locale,
            "geo_location": geo_location,
            "user_agent_type": user_agent_type,
            "callback_url": callback_url,
            "render": render,
            "parse": parse,
            "parsing_instructions": parsing_instructions,
            **kwargs,
        }

        check_parsing_instructions_validity(parsing_instructions)

        response = self._serp_instance._get_resp(payload, config)
        return response

    def scrape_url(
        self,
        url: str,
        user_agent_type: Optional[str] = None,
        geo_location: Optional[str] = None,
        callback_url: Optional[str] = None,
        render: Optional[str] = None,
        parse: Optional[bool] = None,
        parsing_instructions: Optional[dict] = None,
        request_timeout: Optional[int] = None,
        **kwargs,
    ) -> dict:
        """
        Scrapes Bing search results for a given URL.

        Args:
            url (str): The URL to be scraped.
            opts (BingUrlOpts, optional): Configuration options for the search.
            Defaults to:
                {
                    "user_agent_type": desktop,
                    "geo_location": None,
                    "callback_url": None,
                    "render": None,
                    "parsing_instructions": None,
                    "parse": None,
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
            "source": source.BING_URL,
            "url": url,
            "user_agent_type": user_agent_type,
            "geo_location": geo_location,
            "callback_url": callback_url,
            "render": render,
            "parse": parse,
            "parsing_instructions": parsing_instructions,
            **kwargs,
        }
        check_parsing_instructions_validity(parsing_instructions)
        response = self._serp_instance._get_resp(payload, config)
        return response


class BingAsync(BingBase):
    def __init__(self, serp_async_instance) -> None:
        """
        Initializes an instance of the BingAsync class.

        Args:
            serp_async_instance: The SERPAsync instance associated with the
            BingAsync class.
        """
        self._serp_async_instance = serp_async_instance

    async def scrape_search(
        self,
        query: str,
        domain: Optional[str] = None,
        start_page: Optional[int] = None,
        pages: Optional[int] = None,
        limit: Optional[int] = None,
        user_agent_type: Optional[str] = None,
        callback_url: Optional[str] = None,
        locale: Optional[str] = None,
        geo_location: Optional[str] = None,
        render: Optional[str] = None,
        parse: Optional[bool] = None,
        parsing_instructions: Optional[dict] = None,
        request_timeout: Optional[int] = None,
        job_completion_timeout: Optional[int] = None,
        poll_interval: Optional[int] = None,
        **kwargs,
    ) -> dict:
        """
        Asynchronously scrapes Bing search results for a given query.

        Args:
            query (str): The search query.
            opts (dict, optional): Configuration options for the search.
            Defaults to:
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
            request_timeout (int | 165, optional): The interval in seconds for
            the request to time out if no response is returned.
            Defaults to 165.
            poll_interval (int | 5, optional): The interval in seconds to poll
            the server for a response. Defaults to 5
            job_completion_timeout (int | 50, optional): The interval in
            seconds for the job to time out if no response is returned.
            Defaults to 50

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
            "source": source.BING_SEARCH,
            "domain": domain,
            "query": query,
            "start_page": start_page,
            "pages": pages,
            "limit": limit,
            "locale": locale,
            "geo_location": geo_location,
            "user_agent_type": user_agent_type,
            "callback_url": callback_url,
            "render": render,
            "parse": parse,
            "parsing_instructions": parsing_instructions,
            **kwargs,
        }
        check_parsing_instructions_validity(parsing_instructions)
        response = await self._serp_async_instance._get_resp(payload, config)
        return response

    async def scrape_url(
        self,
        url: str,
        user_agent_type: Optional[str] = None,
        geo_location: Optional[str] = None,
        callback_url: Optional[str] = None,
        render: Optional[str] = None,
        parse: Optional[bool] = None,
        parsing_instructions: Optional[dict] = None,
        request_timeout: Optional[int] = None,
        job_completion_timeout: Optional[int] = None,
        poll_interval: Optional[int] = None,
        **kwargs,
    ) -> dict:
        """
        Asynchronously scrapes Bing search results for a given URL.

        Args:
            url (str): The URL to be scraped.
            opts (BingUrlOpts, optional): Configuration options for the search.
            Defaults to:
                {
                    "user_agent_type": desktop,
                    "geo_location": None,
                    "callback_url": None,
                    "render": None,
                    "parsing_instructions": None,
                    "parse": None,
                }
                This parameter allows customization of the search request.
            request_timeout (int | 165, optional): The interval in seconds for
            the request to time out if no response is returned.
            Defaults to 165.
            poll_interval (int | 5, optional): The interval in seconds to poll
            the server for a response. Defaults to 5
            job_completion_timeout (int | 50, optional): The interval in
            seconds for the job to time out if no response is returned.
            Defaults to 50

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
            "source": source.BING_URL,
            "url": url,
            "user_agent_type": user_agent_type,
            "geo_location": geo_location,
            "callback_url": callback_url,
            "render": render,
            "parse": parse,
            "parsing_instructions": parsing_instructions,
        }
        check_parsing_instructions_validity(parsing_instructions)
        response = await self._serp_async_instance._get_resp(payload, config)
        return response
