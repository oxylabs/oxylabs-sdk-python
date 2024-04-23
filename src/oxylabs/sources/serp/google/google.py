from src.oxylabs.utils.utils import prepare_config
from .google_base import GoogleBase
from typing import Optional, Dict, Any


class Google(GoogleBase):
    def __init__(self, serp_instance) -> None:
        """
        Initializes an instance of the Google class.

        Args:
            serp_instance: The SERP instance associated with the Google class.
        """
        self._serp_instance = serp_instance

    def scrape_search(
        self,
        query: str,
        opts: Optional[dict] = None,
        request_timeout: Optional[int] = None,
    ) -> dict:
        """
        Scrapes Google search results for a given query.

        Args:

            query (str): The search query.
            opts (GoogleSearchOpts, optional): Configuration options for the search. Defaults to:
                {
                    "domain": "com",
                    "start_page": 1,
                    "pages": 1,
                    "limit": 10,
                    "user_agent_type": "desktop",
                    "locale": None,
                    "geo_location": None,
                    "render": "None",
                    "callback_url": None,
                    "parse": None,
                    "context": None,
                    "parsing_instructions": None,
                }
                This parameter allows customization of the search request.

            timeout (int | 50, optional): The interval in seconds for the request to time out if no response is returned. Defaults to 50.

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
        Scrapes Google search results for a given URL.

        Args:
            url (str): The URL to be scraped.
            opts (GoogleUrlOpts, optional): Configuration options for the search. Defaults to:
                {
                    "user_agent_type": desktop,
                    "callback_url": None,
                    "render": None,
                    "geo_location": None,
                    "parse": None,
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

    def scrape_ads(
        self,
        query: str,
        opts: Optional[dict] = None,
        request_timeout: Optional[int] = None,
    ) -> dict:
        """
        Scrapes Google Ads search results for a given query.

        Args:
            query (str): The search query.
            opts (GoogleAdsOpts, optional): Configuration options for the search. Defaults to:
                {
                    "domain": "com",
                    "start_page": 1,
                    "pages": 1,
                    "user_agent_type": "desktop",
                    "locale": None,
                    "geo_location": None,
                    "render": "None",
                    "callback_url": None,
                    "parse": None,
                    "context": None,
                    "parsing_instructions": None,
                }
                This parameter allows customization of the search request.
            timeout (int | 50, optional): The interval in seconds for the request to time out if no response is returned. Defaults to 50.

        Returns:
            dict: The response from the server after the job is completed.
        """

        config = prepare_config(request_timeout=request_timeout)
        payload = self._prepare_ads_payload(query, opts)
        response = self._serp_instance.get_resp(payload, config)
        return response

    def scrape_suggestions(
        self,
        query: str,
        opts: Optional[dict] = None,
        request_timeout: Optional[int] = None,
    ) -> dict:
        """
        Scrapes Google suggestions for a given query.

        Args:
            query (str): The search query.
            opts (GoogleSuggestionsOpts, optional): Configuration options for the search. Defaults to:
                {
                    "locale": None,
                    "geo_location": None,
                    "user_agent_type": "desktop",
                    "render": "html",
                    "callback_url": None,
                    "parsing_instructions": None,
                }
                This parameter allows customization of the search request.

            timeout (int | 50, optional): The interval in seconds for the request to time out if no response is returned. Defaults to 50.

        Returns:
            dict: The response from the server after the job is completed.
        """

        config = prepare_config(request_timeout=request_timeout)
        payload = self._prepare_suggestions_payload(query, opts)
        response = self._serp_instance.get_resp(payload, config)
        return response

    def scrape_hotels(
        self,
        query: str,
        opts: Optional[dict] = None,
        request_timeout: Optional[int] = None,
    ) -> dict:
        """
        Scrapes Google Hotels search results for a given query.

        Args:
            query (str): The search query.
            opts (GoogleHotelsOpts, optional): Configuration options for the search. Defaults to:
                {
                    "domain": "com",
                    "start_page": 1,
                    "pages": 1,
                    "limit": 10,
                    "user_agent_type": "desktop",
                    "locale": None,
                    "geo_location": None,
                    "render": "html",
                    "callback_url": None,
                    "context": None,
                    "parsing_instructions": None,
                }
                This parameter allows customization of the search request.
            timeout (int | 50, optional): The interval in seconds for the request to time out if no response is returned. Defaults to 50.

        Returns:
            dict: The response from the server after the job is completed.
        """

        config = prepare_config(request_timeout=request_timeout)
        payload = self._prepare_hotels_payload(query, opts)
        response = self._serp_instance.get_resp(payload, config)
        return response

    def scrape_travel_hotels(
        self,
        query: str,
        opts: Optional[dict] = None,
        request_timeout: Optional[int] = None,
    ) -> dict:
        """
        Scrapes Google Travel Hotels search results for a given query.

        Args:
            query (str): UTF-encoded keyword. "query": "hotels" will result list hotels in a given geo_location; "query": "hotels in <Location>" will result in a list hotels for <Location>. Eg hotels in Paris will list hotels in Paris, no matter what geo_location is given.

            opts (GoogleTravelHotelsOpts, optional): Configuration options for the search. Defaults to:
                {
                    "domain": None,
                    "start_page": None,
                    "locale": None,
                    "geo_location": None,
                    "user_agent_type": "desktop",
                    "render": "html",
                    "callback_url": None,
                    "context": None,
                    "parsing_instructions": None,
                }
                This parameter allows customization of the search request.
            timeout (int | 50, optional): The interval in seconds for the request to time out if no response is returned. Defaults to 50.

        Returns:
            dict: The response from the server after the job is completed.
        """

        config = prepare_config(request_timeout=request_timeout)
        payload = self._prepare_travel_hotels_payload(query, opts)
        response = self._serp_instance.get_resp(payload, config)
        return response

    def scrape_images(
        self,
        query: str,
        opts: Optional[dict] = None,
        request_timeout: Optional[int] = None,
    ) -> dict:
        """
        Scrapes Google Images search results for a given query.

        Args:
            query (str): The search query.
            opts (GoogleImagesOpts, optional): Configuration options for the search. Defaults to:
                {
                    "domain": com,
                    "start_page": 1,
                    "pages": 1,
                    "user_agent_type": "desktop",
                    "locale": None,
                    "geo_location": None,
                    "render": None,
                    "callback_url": None,
                    "parse": None,
                    "context": None,
                    "parsing_instructions": None,
                }
                This parameter allows customization of the search request.

            timeout (int | 50, optional): The interval in seconds for the request to time out if no response is returned. Defaults to 50.

        Returns:
            dict: The response from the server after the job is completed.
        """

        config = prepare_config(request_timeout=request_timeout)
        payload = self._prepare_images_payload(query, opts)
        response = self._serp_instance.get_resp(payload, config)
        return response

    def scrape_trends_explore(
        self,
        query: str,
        opts: Optional[dict] = None,
        request_timeout: Optional[int] = None,
    ) -> dict:
        """
        Scrapes Google Trends Explore results for a given query.

        Args:
            query (str): The search query.
            opts (GoogleTrendsExploreOpts, optional): Configuration options for the search. Defaults to:
                {
                    "user_agent_type": "desktop",
                    "geo_location": None,
                    "callback_url": None,
                    "parsing_instructions": None,
                }
                This parameter allows customization of the search request.
            timeout (int | 50, optional): The interval in seconds for the request to time out if no response is returned. Defaults to 50.

        Returns:
            dict: The response from the server after the job is completed.
        """

        config = prepare_config(request_timeout=request_timeout)
        payload = self._prepare_trends_explore_payload(query, opts)
        response = self._serp_instance.get_resp(payload, config)
        return response


class GoogleAsync(GoogleBase):
    def __init__(self, serp_async_instance) -> None:
        """
        Initializes an asynchronous Google object.

        Args:
            serp_async_instance: The SERP instance to be used for Google requests.
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
        Asynchronously scrapes Google search results for a given query.

        Args:

            query (str): The search query.
            opts (GoogleSearchOpts, optional): Configuration options for the search. Defaults to:
                {
                    "domain": "com",
                    "start_page": 1,
                    "pages": 1,
                    "limit": 10,
                    "user_agent_type": "desktop",
                    "locale": None,
                    "geo_location": None,
                    "render": "None",
                    "callback_url": None,
                    "parse": None,
                    "context": None,
                    "parsing_instructions": None,
                }
                This parameter allows customization of the search request.

            timeout (int | 50, optional): The interval in seconds for the request to time out if no response is returned. Defaults to 50.
            poll_interval (int | 2, optional): The interval in seconds for the request to poll the server for the job status. Defaults to 2.

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
        Asynchronously scrapes Google search results for a given URL.

        Args:
            url (str): The URL to be scraped.
            opts (GoogleUrlOpts, optional): Configuration options for the search. Defaults to:
                {
                    "user_agent_type": desktop,
                    "callback_url": None,
                    "render": None,
                    "geo_location": None,
                    "parse": None,
                    "parsing_instructions": None,
                }
                This parameter allows customization of the search request.
            timeout (int | 50, optional): The interval in seconds for the request to time out if no response is returned. Defaults to 50.
            poll_interval (int | 2, optional): The interval in seconds for the request to poll the server for the job status. Defaults to 2.

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

    async def scrape_ads(
        self,
        query: str,
        opts: Optional[dict] = None,
        request_timeout: Optional[int] = None,
        job_completion_timeout: Optional[int] = None,
        poll_interval: Optional[int] = None,
    ) -> dict:
        """
        Asynchronously scrapes Google Ads search results for a given query.

        Args:
            query (str): The search query.
            opts (GoogleAdsOpts, optional): Configuration options for the search. Defaults to:
                {
                    "domain": "com",
                    "start_page": 1,
                    "pages": 1,
                    "user_agent_type": "desktop",
                    "locale": None,
                    "geo_location": None,
                    "render": "None",
                    "callback_url": None,
                    "parse": None,
                    "context": None,
                    "parsing_instructions": None,
                }
                This parameter allows customization of the search request.
            timeout (int | 50, optional): The interval in seconds for the request to time out if no response is returned. Defaults to 50.
            poll_interval (int | 2, optional): The interval in seconds for the request to poll the server for the job status. Defaults to 2.

        Returns:
            dict: The response from the server after the job is completed.
        """

        config = prepare_config(
            request_timeout=request_timeout,
            poll_interval=poll_interval,
            job_completion_timeout=job_completion_timeout,
            async_integration=True,
        )
        payload = self._prepare_ads_payload(query, opts)
        response = await self._serp_async_instance.get_resp(payload, config)
        return response

    async def scrape_suggestions(
        self,
        query: str,
        opts: Optional[dict] = None,
        request_timeout: Optional[int] = None,
        job_completion_timeout: Optional[int] = None,
        poll_interval: Optional[int] = None,
    ) -> dict:
        """
        Asynchronously scrapes Google suggestions for a given query.

        Args:
            query (str): The search query.
            opts (GoogleSuggestionsOpts, optional): Configuration options for the search. Defaults to:
                {
                    "locale": None,
                    "geo_location": None,
                    "user_agent_type": "desktop",
                    "render": "html",
                    "callback_url": None,
                    "parsing_instructions": None,
                }
                This parameter allows customization of the search request.

            timeout (int | 50, optional): The interval in seconds for the request to time out if no response is returned. Defaults to 50.
            poll_interval (int | 2, optional): The interval in seconds for the request to poll the server for the job status. Defaults to 2.

        Returns:
            dict: The response from the server after the job is completed.
        """

        config = prepare_config(
            request_timeout=request_timeout,
            poll_interval=poll_interval,
            job_completion_timeout=job_completion_timeout,
            async_integration=True,
        )
        payload = self._prepare_suggestions_payload(query, opts)
        response = await self._serp_async_instance.get_resp(payload, config)
        return response

    async def scrape_hotels(
        self,
        query: str,
        opts: Optional[dict] = None,
        request_timeout: Optional[int] = None,
        job_completion_timeout: Optional[int] = None,
        poll_interval: Optional[int] = None,
    ) -> dict:
        """
        Asynchronously scrapes Google Hotels search results for a given query.

        Args:
            query (str): The search query.
            opts (GoogleHotelsOpts, optional): Configuration options for the search. Defaults to:
                {
                    "domain": "com",
                    "start_page": 1,
                    "pages": 1,
                    "limit": 10,
                    "user_agent_type": "desktop",
                    "locale": None,
                    "geo_location": None,
                    "render": "html",
                    "callback_url": None,
                    "context": None,
                    "parsing_instructions": None,
                }
                This parameter allows customization of the search request.
            timeout (int | 50, optional): The interval in seconds for the request to time out if no response is returned. Defaults to 50.
            poll_interval (int | 2, optional): The interval in seconds for the request to poll the server for the job status. Defaults to 2.

        Returns:
            dict: The response from the server after the job is completed.
        """

        config = prepare_config(
            request_timeout=request_timeout,
            poll_interval=poll_interval,
            job_completion_timeout=job_completion_timeout,
            async_integration=True,
        )
        payload = self._prepare_hotels_payload(query, opts)
        response = await self._serp_async_instance.get_resp(payload, config)
        return response

    async def scrape_travel_hotels(
        self,
        query: str,
        opts: Optional[dict] = None,
        request_timeout: Optional[int] = None,
        job_completion_timeout: Optional[int] = None,
        poll_interval: Optional[int] = None,
    ) -> dict:
        """
        Asynchronously scrapes Google Travel Hotels search results for a given query.

        Args:
            query (str): UTF-encoded keyword. "query": "hotels" will result list hotels in a given geo_location; "query": "hotels in <Location>" will result in a list hotels for <Location>. Eg hotels in Paris will list hotels in Paris, no matter what geo_location is given.

            opts (GoogleTravelHotelsOpts, optional): Configuration options for the search. Defaults to:
                {
                    "domain": None,
                    "start_page": None,
                    "locale": None,
                    "geo_location": None,
                    "user_agent_type": "desktop",
                    "render": "html",
                    "callback_url": None,
                    "context": None,
                    "parsing_instructions": None,
                }
                This parameter allows customization of the search request.
            timeout (int | 50, optional): The interval in seconds for the request to time out if no response is returned. Defaults to 50.
            poll_interval (int | 2, optional): The interval in seconds for the request to poll the server for the job status. Defaults to 2.

        Returns:
            dict: The response from the server after the job is completed.
        """

        config = prepare_config(
            request_timeout=request_timeout,
            poll_interval=poll_interval,
            job_completion_timeout=job_completion_timeout,
            async_integration=True,
        )
        payload = self._prepare_travel_hotels_payload(query, opts)
        response = await self._serp_async_instance.get_resp(payload, config)
        return response

    async def scrape_images(
        self,
        query: str,
        opts: Optional[dict] = None,
        request_timeout: Optional[int] = None,
        job_completion_timeout: Optional[int] = None,
        poll_interval: Optional[int] = None,
    ) -> dict:
        """
        Asynchronously scrapes Google Images search results for a given query.

        Args:
            query (str): The search query.
            opts (GoogleImagesOpts, optional): Configuration options for the search. Defaults to:
                {
                    "domain": com,
                    "start_page": 1,
                    "pages": 1,
                    "user_agent_type": "desktop",
                    "locale": None,
                    "geo_location": None,
                    "render": None,
                    "callback_url": None,
                    "parse": None,
                    "context": None,
                    "parsing_instructions": None,
                }
                This parameter allows customization of the search request.

            timeout (int | 50, optional): The interval in seconds for the request to time out if no response is returned. Defaults to 50.
            poll_interval (int | 2, optional): The interval in seconds for the request to poll the server for the job status. Defaults to 2.

        Returns:
            dict: The response from the server after the job is completed.
        """

        config = prepare_config(
            request_timeout=request_timeout,
            poll_interval=poll_interval,
            job_completion_timeout=job_completion_timeout,
            async_integration=True,
        )
        payload = self._prepare_images_payload(query, opts)
        response = await self._serp_async_instance.get_resp(payload, config)
        return response

    async def scrape_trends_explore(
        self,
        query: str,
        opts: Optional[dict] = None,
        request_timeout: Optional[int] = None,
        job_completion_timeout: Optional[int] = None,
        poll_interval: Optional[int] = None,
    ) -> dict:
        """
        Asynchronously scrapes Google Trends Explore results for a given query.

        Args:
            query (str): The search query.
            opts (GoogleTrendsExploreOpts, optional): Configuration options for the search. Defaults to:
                {
                    "user_agent_type": "desktop",
                    "geo_location": None,
                    "callback_url": None,
                    "parsing_instructions": None,
                }
                This parameter allows customization of the search request.
            timeout (int | 50, optional): The interval in seconds for the request to time out if no response is returned. Defaults to 50.
            poll_interval (int | 2, optional): The interval in seconds for the request to poll the server for the job status. Defaults to 2.

        Returns:
            dict: The response from the server after the job is completed.
        """

        config = prepare_config(
            request_timeout=request_timeout,
            poll_interval=poll_interval,
            job_completion_timeout=job_completion_timeout,
            async_integration=True,
        )
        payload = self._prepare_trends_explore_payload(query, opts)
        response = await self._serp_async_instance.get_resp(payload, config)
        return response
