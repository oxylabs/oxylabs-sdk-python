from utils.utils import prepare_config
from .google_base import GoogleBase
from .serp import Serp, SerpAsync
from typing import Optional, Dict, Any


class Google(GoogleBase):
    def __init__(self, client: Serp):
        """
        Initializes a Google object.

        Args:
            client (Serp): The Serp instance to be used for Google requests.

        Raises:
            TypeError: If the client is not an instance of Serp.
        """
        if not isinstance(client, Serp):
            raise TypeError("Google requires a Serp instance")
        self.client = client

    def scrape_google_search(
        self,
        query: str,
        opts: Optional[Dict[str, Any]] = None,
        timeout: Optional[int] = None,
    ) -> Dict[str, Any]:
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

        config = prepare_config(timeout=timeout)
        payload = self._prepare_search_payload(query, opts)
        response = self.client.get_resp(payload, config)
        return response

    def scrape_google_url(
        self,
        url: str,
        opts: Optional[Dict[str, Any]] = None,
        timeout: Optional[int] = None,
    ) -> Dict[str, Any]:
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

        config = prepare_config(timeout=timeout)
        payload = self._prepare_url_payload(url, opts)
        response = self.client.get_resp(payload, config)
        return response

    def scrape_google_ads(
        self,
        query: str,
        opts: Optional[Dict[str, Any]] = None,
        timeout: Optional[int] = None,
    ) -> Dict[str, Any]:
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

        config = prepare_config(timeout=timeout)
        payload = self._prepare_ads_payload(query, opts)
        response = self.client.get_resp(payload, config)
        return response

    def scrape_google_suggestions(
        self,
        query: str,
        opts: Optional[Dict[str, Any]] = None,
        timeout: Optional[int] = None,
    ) -> Dict[str, Any]:
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

        config = prepare_config(timeout=timeout)
        payload = self._prepare_suggestions_payload(query, opts)
        response = self.client.get_resp(payload, config)
        return response

    def scrape_google_hotels(
        self,
        query: str,
        opts: Optional[Dict[str, Any]] = None,
        timeout: Optional[int] = None,
    ) -> Dict[str, Any]:
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

        config = prepare_config(timeout=timeout)
        payload = self._prepare_hotels_payload(query, opts)
        response = self.client.get_resp(payload, config)
        return response

    def scrape_google_travel_hotels(
        self,
        query: str,
        opts: Optional[Dict[str, Any]] = None,
        timeout: Optional[int] = None,
    ) -> Dict[str, Any]:
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

        config = prepare_config(timeout=timeout)
        payload = self._prepare_travel_hotels_payload(query, opts)
        response = self.client.get_resp(payload, config)
        return response

    def scrape_google_images(
        self,
        query: str,
        opts: Optional[Dict[str, Any]] = None,
        timeout: Optional[int] = None,
    ) -> Dict[str, Any]:
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

        config = prepare_config(timeout=timeout)
        payload = self._prepare_images_payload(query, opts)
        response = self.client.get_resp(payload, config)
        return response

    def scrape_google_trends_explore(
        self,
        query: str,
        opts: Optional[Dict[str, Any]] = None,
        timeout: Optional[int] = None,
    ) -> Dict[str, Any]:
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

        config = prepare_config(timeout=timeout)
        payload = self._prepare_trends_explore_payload(query, opts)
        response = self.client.get_resp(payload, config)
        return response


class GoogleAsync(GoogleBase):
    def __init__(self, client: SerpAsync):
        """
        Initializes a GoogleAsync instance.

        Args:
            client (SerpAsync): An instance of SerpAsync.

        Raises:
            TypeError: If the client parameter is not an instance of SerpAsync.
        """
        if not isinstance(client, SerpAsync):
            raise TypeError("GoogleAsync requires a SerpAsync instance")
        self.client = client

    async def scrape_google_search(
        self,
        query: str,
        opts: Optional[Dict[str, Any]] = None,
        timeout: Optional[int] = None,
        poll_interval: Optional[int] = None,
    ) -> Dict[str, Any]:
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

        config = prepare_config(timeout=timeout, poll_interval=poll_interval)
        payload = self._prepare_search_payload(query, opts)
        response = await self.client.get_resp(payload, config)
        return response

    async def scrape_google_url(
        self,
        url: str,
        opts: Optional[Dict[str, Any]] = None,
        timeout: Optional[int] = None,
        poll_interval: Optional[int] = None,
    ) -> Dict[str, Any]:
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

        config = prepare_config(timeout=timeout, poll_interval=poll_interval)
        payload = self._prepare_url_payload(url, opts)
        response = await self.client.get_resp(payload, config)
        return response

    async def scrape_google_ads(
        self,
        query: str,
        opts: Optional[Dict[str, Any]] = None,
        timeout: Optional[int] = None,
        poll_interval: Optional[int] = None,
    ) -> Dict[str, Any]:
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

        config = prepare_config(timeout=timeout, poll_interval=poll_interval)
        payload = self._prepare_ads_payload(query, opts)
        response = await self.client.get_resp(payload, config)
        return response

    async def scrape_google_suggestions(
        self,
        query: str,
        opts: Optional[Dict[str, Any]] = None,
        timeout: Optional[int] = None,
        poll_interval: Optional[int] = None,
    ) -> Dict[str, Any]:
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

        config = prepare_config(timeout=timeout, poll_interval=poll_interval)
        payload = self._prepare_suggestions_payload(query, opts)
        response = await self.client.get_resp(payload, config)
        return response

    async def scrape_google_hotels(
        self,
        query: str,
        opts: Optional[Dict[str, Any]] = None,
        timeout: Optional[int] = None,
        poll_interval: Optional[int] = None,
    ) -> Dict[str, Any]:
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

        config = prepare_config(timeout=timeout, poll_interval=poll_interval)
        payload = self._prepare_hotels_payload(query, opts)
        response = await self.client.get_resp(payload, config)
        return response

    async def scrape_google_travel_hotels(
        self,
        query: str,
        opts: Optional[Dict[str, Any]] = None,
        timeout: Optional[int] = None,
        poll_interval: Optional[int] = None,
    ) -> Dict[str, Any]:
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

        config = prepare_config(timeout=timeout, poll_interval=poll_interval)
        payload = self._prepare_travel_hotels_payload(query, opts)
        response = await self.client.get_resp(payload, config)
        return response

    async def scrape_google_images(
        self,
        query: str,
        opts: Optional[Dict[str, Any]] = None,
        timeout: Optional[int] = None,
        poll_interval: Optional[int] = None,
    ) -> Dict[str, Any]:
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

        config = prepare_config(timeout=timeout, poll_interval=poll_interval)
        payload = self._prepare_images_payload(query, opts)
        response = await self.client.get_resp(payload, config)
        return response

    async def scrape_google_trends_explore(
        self,
        query: str,
        opts: Optional[Dict[str, Any]] = None,
        timeout: Optional[int] = None,
        poll_interval: Optional[int] = None,
    ) -> Dict[str, Any]:
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

        config = prepare_config(timeout=timeout, poll_interval=poll_interval)
        payload = self._prepare_trends_explore_payload(query, opts)
        response = await self.client.get_resp(payload, config)
        return response
