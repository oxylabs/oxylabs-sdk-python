from typing import Optional

from oxylabs.internal.api import RealtimeAPI, AsyncAPI
from oxylabs.sources.response import Response
from oxylabs.utils.types import source
from oxylabs.utils.utils import prepare_config


class Etsy:
    def __init__(self, api_instance: RealtimeAPI) -> None:
        """
        Initializes an instance of the Etsy class.

        Args:
            api_instance: An instance of the RealtimeAPI class used for making requests.
        """
        self._api_instance = api_instance

    def scrape_search(
        self,
        query: str,
        start_page: Optional[int] = None,
        store_id: Optional[int] = None,
        geo_location: Optional[str] = None,
        user_agent_type: Optional[str] = None,
        render: Optional[str] = None,
        callback_url: Optional[str] = None,
        request_timeout: Optional[int] = 165,
        **kwargs
    ) -> Response:
        """
        Scrapes Etsy search results for a given query.

        Args:
            query (str): The keyword or phrase to search for.
            start_page (Optional[int]): Starting page number.
            store_id (Optional[int]): Specify a store.
            geo_location (Optional[str]): Set the shipping to location.
            user_agent_type (Optional[str]): Device type and browser.
            render (Optional[str]): Enables JavaScript rendering.
            callback_url (Optional[str]): URL to your callback endpoint.
            request_timeout (int | 165, optional): The interval in seconds for
                            the request to time out if no response is returned.
                            Defaults to 165.

        Returns:
            Response: The response from the server after the job is completed.
        """

        config = prepare_config(request_timeout=request_timeout)
        payload = {
            "source": source.ETSY_SEARCH,
            "query": query,
            "start_page": start_page,
            "store_id": store_id,
            "geo_location": geo_location,
            "user_agent_type": user_agent_type,
            "render": render,
            "callback_url": callback_url,
            **kwargs,
        }
        api_response = self._api_instance.get_response(payload, config)
        return Response(api_response)

    def scrape_product(
        self,
        product_id: str,
        user_agent_type: Optional[str] = None,
        render: Optional[str] = None,
        parse: Optional[bool] = None,
        callback_url: Optional[str] = None,
        request_timeout: Optional[int] = 165,
        **kwargs
    ) -> Response:
        """
        Scrapes an Etsy product page for a given product ID.

        Args:
            product_id (str): 10-symbol product ID.
            user_agent_type (Optional[str]): Device type and browser.
            render (Optional[str]): Enables JavaScript rendering.
            parse (Optional[bool]): Returns parsed data when set to true.
            callback_url (Optional[str]): URL to your callback endpoint.
            request_timeout (int | 165, optional): The interval in seconds for
                            the request to time out if no response is returned.
                            Defaults to 165.

        Returns:
            Response: The response from the server after the job is completed.
        """

        config = prepare_config(request_timeout=request_timeout)
        payload = {
            "source": source.ETSY_PRODUCT,
            "product_id": product_id,
            "user_agent_type": user_agent_type,
            "render": render,
            "parse": parse,
            "callback_url": callback_url,
            **kwargs,
        }
        api_response = self._api_instance.get_response(payload, config)
        return Response(api_response)

    def scrape_url(
        self,
        url: str,
        user_agent_type: Optional[str] = None,
        render: Optional[str] = None,
        callback_url: Optional[str] = None,
        request_timeout: Optional[int] = 165,
        **kwargs
    ) -> Response:
        """
        Scrapes content from an Etsy URL.

        Args:
            url (str): Direct URL to any Etsy page.
            user_agent_type (Optional[str]): Device type and browser.
            render (Optional[str]): Enables JavaScript rendering.
            callback_url (Optional[str]): URL to your callback endpoint.
            request_timeout (int | 165, optional): The interval in seconds for
                            the request to time out if no response is returned.
                            Defaults to 165.

        Returns:
            Response: The response from the server after the job is completed.
        """

        config = prepare_config(request_timeout=request_timeout)
        payload = {
            "source": source.ETSY_URL,
            "url": url,
            "user_agent_type": user_agent_type,
            "render": render,
            "callback_url": callback_url,
            **kwargs,
        }
        api_response = self._api_instance.get_response(payload, config)
        return Response(api_response)


class EtsyAsync:
    def __init__(self, api_instance: AsyncAPI) -> None:
        """
        Initializes an instance of the EtsyAsync class.

        Args:
            api_instance: An instance of the AsyncAPI class used for making requests.
        """
        self._api_instance = api_instance

    async def scrape_search(
        self,
        query: str,
        start_page: Optional[int] = None,
        store_id: Optional[int] = None,
        geo_location: Optional[str] = None,
        user_agent_type: Optional[str] = None,
        render: Optional[str] = None,
        callback_url: Optional[str] = None,
        request_timeout: Optional[int] = 165,
        job_completion_timeout: Optional[int] = None,
        poll_interval: Optional[int] = None,
        **kwargs
    ) -> Response:
        """
        Asynchronously scrapes Etsy search results for a given query.

        Args:
            query (str): The keyword or phrase to search for.
            start_page (Optional[int]): Starting page number.
            store_id (Optional[int]): Specify a store.
            geo_location (Optional[str]): Set the shipping to location.
            user_agent_type (Optional[str]): Device type and browser.
            render (Optional[str]): Enables JavaScript rendering.
            callback_url (Optional[str]): URL to your callback endpoint.
            request_timeout (int | 165, optional): The interval in seconds for
                            the request to time out if no response is returned.
                            Defaults to 165.
            poll_interval (Optional[int]): The interval in seconds to poll
                            the server for a response.
            job_completion_timeout (Optional[int]): The interval in
                            seconds for the job to time out if no response is returned.

        Returns:
            Response: The response from the server after the job is completed.
        """

        config = prepare_config(
            request_timeout=request_timeout,
            poll_interval=poll_interval,
            job_completion_timeout=job_completion_timeout,
            async_integration=True,
        )
        payload = {
            "source": source.ETSY_SEARCH,
            "query": query,
            "start_page": start_page,
            "store_id": store_id,
            "geo_location": geo_location,
            "user_agent_type": user_agent_type,
            "render": render,
            "callback_url": callback_url,
            **kwargs,
        }
        api_response = await self._api_instance.get_response(payload, config)
        return Response(api_response)

    async def scrape_product(
        self,
        product_id: str,
        user_agent_type: Optional[str] = None,
        render: Optional[str] = None,
        parse: Optional[bool] = None,
        callback_url: Optional[str] = None,
        request_timeout: Optional[int] = 165,
        job_completion_timeout: Optional[int] = None,
        poll_interval: Optional[int] = None,
        **kwargs
    ) -> Response:
        """
        Asynchronously scrapes an Etsy product page for a given product ID.

        Args:
            product_id (str): 10-symbol product ID.
            user_agent_type (Optional[str]): Device type and browser.
            render (Optional[str]): Enables JavaScript rendering.
            parse (Optional[bool]): Returns parsed data when set to true.
            callback_url (Optional[str]): URL to your callback endpoint.
            request_timeout (int | 165, optional): The interval in seconds for
                            the request to time out if no response is returned.
                            Defaults to 165.
            poll_interval (Optional[int]): The interval in seconds to poll
                            the server for a response.
            job_completion_timeout (Optional[int]): The interval in
                            seconds for the job to time out if no response is returned.

        Returns:
            Response: The response from the server after the job is completed.
        """

        config = prepare_config(
            request_timeout=request_timeout,
            poll_interval=poll_interval,
            job_completion_timeout=job_completion_timeout,
            async_integration=True,
        )
        payload = {
            "source": source.ETSY_PRODUCT,
            "product_id": product_id,
            "user_agent_type": user_agent_type,
            "render": render,
            "parse": parse,
            "callback_url": callback_url,
            **kwargs,
        }
        api_response = await self._api_instance.get_response(payload, config)
        return Response(api_response)

    async def scrape_url(
        self,
        url: str,
        user_agent_type: Optional[str] = None,
        render: Optional[str] = None,
        callback_url: Optional[str] = None,
        request_timeout: Optional[int] = 165,
        job_completion_timeout: Optional[int] = None,
        poll_interval: Optional[int] = None,
        **kwargs
    ) -> Response:
        """
        Asynchronously scrapes content from an Etsy URL.

        Args:
            url (str): Direct URL to any Etsy page.
            user_agent_type (Optional[str]): Device type and browser.
            render (Optional[str]): Enables JavaScript rendering.
            callback_url (Optional[str]): URL to your callback endpoint.
            request_timeout (int | 165, optional): The interval in seconds for
                            the request to time out if no response is returned.
                            Defaults to 165.
            poll_interval (Optional[int]): The interval in seconds to poll
                            the server for a response.
            job_completion_timeout (Optional[int]): The interval in
                            seconds for the job to time out if no response is returned.

        Returns:
            Response: The response from the server after the job is completed.
        """

        config = prepare_config(
            request_timeout=request_timeout,
            poll_interval=poll_interval,
            job_completion_timeout=job_completion_timeout,
            async_integration=True,
        )
        payload = {
            "source": source.ETSY_URL,
            "url": url,
            "user_agent_type": user_agent_type,
            "render": render,
            "callback_url": callback_url,
            **kwargs,
        }
        api_response = await self._api_instance.get_response(payload, config)
        return Response(api_response)
