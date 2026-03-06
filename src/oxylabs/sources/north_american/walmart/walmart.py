from typing import Optional

from oxylabs.internal.api import RealtimeAPI, AsyncAPI
from oxylabs.sources.response import Response
from oxylabs.utils.types import source
from oxylabs.utils.utils import prepare_config


class Walmart:
    def __init__(self, api_instance: RealtimeAPI) -> None:
        """
        Initializes an instance of the Walmart class.

        Args:
            api_instance: An instance of the RealtimeAPI class used for making requests.
        """
        self._api_instance = api_instance

    def scrape_search(
        self,
        query: str,
        domain: Optional[str] = None,
        start_page: Optional[int] = None,
        min_price: Optional[float] = None,
        max_price: Optional[float] = None,
        sort_by: Optional[str] = None,
        delivery_zip: Optional[str] = None,
        store_id: Optional[str] = None,
        fulfillment_speed: Optional[str] = None,
        fulfillment_type: Optional[str] = None,
        user_agent_type: Optional[str] = None,
        render: Optional[str] = None,
        callback_url: Optional[str] = None,
        parse: Optional[bool] = None,
        request_timeout: Optional[int] = 165,
        **kwargs
    ) -> Response:
        """
        Scrapes Walmart search results for a given query.

        Args:
            query (str): The keyword or phrase to search for.
            domain (Optional[str]): Domain localization for Walmart.
            start_page (Optional[int]): Starting page number.
            min_price (Optional[float]): Set the minimum price.
            max_price (Optional[float]): Set the maximum price.
            sort_by (Optional[str]): Select sorting of products. Accepted values:
                            "price_low", "price_high", "best_seller", "best_match".
            delivery_zip (Optional[str]): Set the shipping to location.
            store_id (Optional[str]): Set the store location.
            fulfillment_speed (Optional[str]): Set the fulfillment speed. Accepted values:
                            "today", "2_days", "anytime", "tomorrow".
            fulfillment_type (Optional[str]): Set the fulfillment type. Accepted values:
                            "in_store".
            user_agent_type (Optional[str]): Device type and browser.
            render (Optional[str]): Enables JavaScript rendering.
            callback_url (Optional[str]): URL to your callback endpoint.
            parse (Optional[bool]): Returns parsed data when set to true.
            request_timeout (int | 165, optional): The interval in seconds for
                            the request to time out if no response is returned.
                            Defaults to 165.

        Returns:
            Response: The response from the server after the job is completed.
        """

        config = prepare_config(request_timeout=request_timeout)
        payload = {
            "source": source.WALMART_SEARCH,
            "query": query,
            "domain": domain,
            "start_page": start_page,
            "min_price": min_price,
            "max_price": max_price,
            "sort_by": sort_by,
            "delivery_zip": delivery_zip,
            "store_id": store_id,
            "fulfillment_speed": fulfillment_speed,
            "fulfillment_type": fulfillment_type,
            "user_agent_type": user_agent_type,
            "render": render,
            "callback_url": callback_url,
            "parse": parse,
            **kwargs,
        }
        api_response = self._api_instance.get_response(payload, config)
        return Response(api_response)

    def scrape_product(
        self,
        product_id: str,
        domain: Optional[str] = None,
        delivery_zip: Optional[str] = None,
        store_id: Optional[str] = None,
        user_agent_type: Optional[str] = None,
        render: Optional[str] = None,
        parse: Optional[bool] = None,
        callback_url: Optional[str] = None,
        request_timeout: Optional[int] = 165,
        **kwargs
    ) -> Response:
        """
        Scrapes a Walmart product page for a given product ID.

        Args:
            product_id (str): Walmart product ID.
            domain (Optional[str]): Domain localization for Walmart.
            delivery_zip (Optional[str]): Set the shipping to location.
            store_id (Optional[str]): Set the store location.
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
            "source": source.WALMART_PRODUCT,
            "product_id": product_id,
            "domain": domain,
            "delivery_zip": delivery_zip,
            "store_id": store_id,
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
        parse: Optional[bool] = None,
        callback_url: Optional[str] = None,
        request_timeout: Optional[int] = 165,
        **kwargs
    ) -> Response:
        """
        Scrapes content from a Walmart URL.

        Args:
            url (str): Direct URL to any Walmart page.
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
            "source": source.WALMART_URL,
            "url": url,
            "user_agent_type": user_agent_type,
            "render": render,
            "parse": parse,
            "callback_url": callback_url,
            **kwargs,
        }
        api_response = self._api_instance.get_response(payload, config)
        return Response(api_response)


class WalmartAsync:
    def __init__(self, api_instance: AsyncAPI) -> None:
        """
        Initializes an instance of the WalmartAsync class.

        Args:
            api_instance: An instance of the AsyncAPI class used for making requests.
        """
        self._api_instance = api_instance

    async def scrape_search(
        self,
        query: str,
        domain: Optional[str] = None,
        start_page: Optional[int] = None,
        min_price: Optional[float] = None,
        max_price: Optional[float] = None,
        sort_by: Optional[str] = None,
        delivery_zip: Optional[str] = None,
        store_id: Optional[str] = None,
        fulfillment_speed: Optional[str] = None,
        fulfillment_type: Optional[str] = None,
        user_agent_type: Optional[str] = None,
        render: Optional[str] = None,
        callback_url: Optional[str] = None,
        parse: Optional[bool] = None,
        request_timeout: Optional[int] = 165,
        job_completion_timeout: Optional[int] = None,
        poll_interval: Optional[int] = None,
        **kwargs
    ) -> Response:
        """
        Asynchronously scrapes Walmart search results for a given query.

        Args:
            query (str): The keyword or phrase to search for.
            domain (Optional[str]): Domain localization for Walmart.
            start_page (Optional[int]): Starting page number.
            min_price (Optional[float]): Set the minimum price.
            max_price (Optional[float]): Set the maximum price.
            sort_by (Optional[str]): Select sorting of products. Accepted values:
                            "price_low", "price_high", "best_seller", "best_match".
            delivery_zip (Optional[str]): Set the shipping to location.
            store_id (Optional[str]): Set the store location.
            fulfillment_speed (Optional[str]): Set the fulfillment speed. Accepted values:
                            "today", "2_days", "anytime", "tomorrow".
            fulfillment_type (Optional[str]): Set the fulfillment type. Accepted values:
                            "in_store".
            user_agent_type (Optional[str]): Device type and browser.
            render (Optional[str]): Enables JavaScript rendering.
            callback_url (Optional[str]): URL to your callback endpoint.
            parse (Optional[bool]): Returns parsed data when set to true.
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
            "source": source.WALMART_SEARCH,
            "query": query,
            "domain": domain,
            "start_page": start_page,
            "min_price": min_price,
            "max_price": max_price,
            "sort_by": sort_by,
            "delivery_zip": delivery_zip,
            "store_id": store_id,
            "fulfillment_speed": fulfillment_speed,
            "fulfillment_type": fulfillment_type,
            "user_agent_type": user_agent_type,
            "render": render,
            "callback_url": callback_url,
            "parse": parse,
            **kwargs,
        }
        api_response = await self._api_instance.get_response(payload, config)
        return Response(api_response)

    async def scrape_product(
        self,
        product_id: str,
        domain: Optional[str] = None,
        delivery_zip: Optional[str] = None,
        store_id: Optional[str] = None,
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
        Asynchronously scrapes a Walmart product page for a given product ID.

        Args:
            product_id (str): Walmart product ID.
            domain (Optional[str]): Domain localization for Walmart.
            delivery_zip (Optional[str]): Set the shipping to location.
            store_id (Optional[str]): Set the store location.
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
            "source": source.WALMART_PRODUCT,
            "product_id": product_id,
            "domain": domain,
            "delivery_zip": delivery_zip,
            "store_id": store_id,
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
        parse: Optional[bool] = None,
        callback_url: Optional[str] = None,
        request_timeout: Optional[int] = 165,
        job_completion_timeout: Optional[int] = None,
        poll_interval: Optional[int] = None,
        **kwargs
    ) -> Response:
        """
        Asynchronously scrapes content from a Walmart URL.

        Args:
            url (str): Direct URL to any Walmart page.
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
            "source": source.WALMART_URL,
            "url": url,
            "user_agent_type": user_agent_type,
            "render": render,
            "parse": parse,
            "callback_url": callback_url,
            **kwargs,
        }
        api_response = await self._api_instance.get_response(payload, config)
        return Response(api_response)
