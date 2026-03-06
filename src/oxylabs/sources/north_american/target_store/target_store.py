from typing import Optional

from oxylabs.internal.api import RealtimeAPI, AsyncAPI
from oxylabs.sources.response import Response
from oxylabs.utils.types import source
from oxylabs.utils.utils import prepare_config


class TargetStore:
    def __init__(self, api_instance: RealtimeAPI) -> None:
        """
        Initializes an instance of the TargetStore class.

        Args:
            api_instance: An instance of the RealtimeAPI class used for making requests.
        """
        self._api_instance = api_instance

    def scrape_search(
        self,
        query: str,
        store_id: Optional[int] = None,
        delivery_zip: Optional[str] = None,
        fulfillment_type: Optional[str] = None,
        user_agent_type: Optional[str] = None,
        render: Optional[str] = None,
        callback_url: Optional[str] = None,
        parse: Optional[bool] = None,
        request_timeout: Optional[int] = 165,
        **kwargs
    ) -> Response:
        """
        Scrapes Target search results for a given query.

        Args:
            query (str): The keyword or phrase to search for.
            store_id (Optional[int]): Set store location.
            delivery_zip (Optional[str]): Set shipping destination.
            fulfillment_type (Optional[str]): Order fulfillment method.
                            Accepted values: "pickup", "shipping", "shop_in_store", "same_day_delivery".
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
            "source": source.TARGET_SEARCH,
            "query": query,
            "store_id": store_id,
            "delivery_zip": delivery_zip,
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
        store_id: Optional[int] = None,
        delivery_zip: Optional[str] = None,
        fulfillment_type: Optional[str] = None,
        user_agent_type: Optional[str] = None,
        render: Optional[str] = None,
        callback_url: Optional[str] = None,
        parse: Optional[bool] = None,
        request_timeout: Optional[int] = 165,
        **kwargs
    ) -> Response:
        """
        Scrapes a Target product page for a given product ID.

        Args:
            product_id (str): Target product ID.
            store_id (Optional[int]): Set store location.
            delivery_zip (Optional[str]): Set shipping destination.
            fulfillment_type (Optional[str]): Order fulfillment method.
                            Accepted values: "pickup", "delivery", "shipping".
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
            "source": source.TARGET_PRODUCT,
            "product_id": product_id,
            "store_id": store_id,
            "delivery_zip": delivery_zip,
            "fulfillment_type": fulfillment_type,
            "user_agent_type": user_agent_type,
            "render": render,
            "callback_url": callback_url,
            "parse": parse,
            **kwargs,
        }
        api_response = self._api_instance.get_response(payload, config)
        return Response(api_response)

    def scrape_category(
        self,
        category_id: str,
        store_id: Optional[int] = None,
        delivery_zip: Optional[str] = None,
        fulfillment_type: Optional[str] = None,
        user_agent_type: Optional[str] = None,
        render: Optional[str] = None,
        callback_url: Optional[str] = None,
        request_timeout: Optional[int] = 165,
        **kwargs
    ) -> Response:
        """
        Scrapes a Target category page for a given category ID.

        Args:
            category_id (str): Target taxonomy node ID.
            store_id (Optional[int]): Set store location.
            delivery_zip (Optional[str]): Set shipping destination.
            fulfillment_type (Optional[str]): Order fulfillment method.
                            Accepted values: "pickup", "shipping", "shop_in_store", "same_day_delivery".
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
            "source": source.TARGET_CATEGORY,
            "category_id": category_id,
            "store_id": store_id,
            "delivery_zip": delivery_zip,
            "fulfillment_type": fulfillment_type,
            "user_agent_type": user_agent_type,
            "render": render,
            "callback_url": callback_url,
            **kwargs,
        }
        api_response = self._api_instance.get_response(payload, config)
        return Response(api_response)

    def scrape_url(
        self,
        url: str,
        store_id: Optional[int] = None,
        delivery_zip: Optional[str] = None,
        user_agent_type: Optional[str] = None,
        render: Optional[str] = None,
        callback_url: Optional[str] = None,
        request_timeout: Optional[int] = 165,
        **kwargs
    ) -> Response:
        """
        Scrapes content from a Target URL.

        Args:
            url (str): Direct URL to any Target page.
            store_id (Optional[int]): Set store location.
            delivery_zip (Optional[str]): Set shipping destination.
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
            "source": source.TARGET_URL,
            "url": url,
            "store_id": store_id,
            "delivery_zip": delivery_zip,
            "user_agent_type": user_agent_type,
            "render": render,
            "callback_url": callback_url,
            **kwargs,
        }
        api_response = self._api_instance.get_response(payload, config)
        return Response(api_response)


class TargetStoreAsync:
    def __init__(self, api_instance: AsyncAPI) -> None:
        """
        Initializes an instance of the TargetStoreAsync class.

        Args:
            api_instance: An instance of the AsyncAPI class used for making requests.
        """
        self._api_instance = api_instance

    async def scrape_search(
        self,
        query: str,
        store_id: Optional[int] = None,
        delivery_zip: Optional[str] = None,
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
        Asynchronously scrapes Target search results for a given query.

        Args:
            query (str): The keyword or phrase to search for.
            store_id (Optional[int]): Set store location.
            delivery_zip (Optional[str]): Set shipping destination.
            fulfillment_type (Optional[str]): Order fulfillment method.
                            Accepted values: "pickup", "shipping", "shop_in_store", "same_day_delivery".
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
            "source": source.TARGET_SEARCH,
            "query": query,
            "store_id": store_id,
            "delivery_zip": delivery_zip,
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
        store_id: Optional[int] = None,
        delivery_zip: Optional[str] = None,
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
        Asynchronously scrapes a Target product page for a given product ID.

        Args:
            product_id (str): Target product ID.
            store_id (Optional[int]): Set store location.
            delivery_zip (Optional[str]): Set shipping destination.
            fulfillment_type (Optional[str]): Order fulfillment method.
                            Accepted values: "pickup", "delivery", "shipping".
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
            "source": source.TARGET_PRODUCT,
            "product_id": product_id,
            "store_id": store_id,
            "delivery_zip": delivery_zip,
            "fulfillment_type": fulfillment_type,
            "user_agent_type": user_agent_type,
            "render": render,
            "callback_url": callback_url,
            "parse": parse,
            **kwargs,
        }
        api_response = await self._api_instance.get_response(payload, config)
        return Response(api_response)

    async def scrape_category(
        self,
        category_id: str,
        store_id: Optional[int] = None,
        delivery_zip: Optional[str] = None,
        fulfillment_type: Optional[str] = None,
        user_agent_type: Optional[str] = None,
        render: Optional[str] = None,
        callback_url: Optional[str] = None,
        request_timeout: Optional[int] = 165,
        job_completion_timeout: Optional[int] = None,
        poll_interval: Optional[int] = None,
        **kwargs
    ) -> Response:
        """
        Asynchronously scrapes a Target category page for a given category ID.

        Args:
            category_id (str): Target taxonomy node ID.
            store_id (Optional[int]): Set store location.
            delivery_zip (Optional[str]): Set shipping destination.
            fulfillment_type (Optional[str]): Order fulfillment method.
                            Accepted values: "pickup", "shipping", "shop_in_store", "same_day_delivery".
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
            "source": source.TARGET_CATEGORY,
            "category_id": category_id,
            "store_id": store_id,
            "delivery_zip": delivery_zip,
            "fulfillment_type": fulfillment_type,
            "user_agent_type": user_agent_type,
            "render": render,
            "callback_url": callback_url,
            **kwargs,
        }
        api_response = await self._api_instance.get_response(payload, config)
        return Response(api_response)

    async def scrape_url(
        self,
        url: str,
        store_id: Optional[int] = None,
        delivery_zip: Optional[str] = None,
        user_agent_type: Optional[str] = None,
        render: Optional[str] = None,
        callback_url: Optional[str] = None,
        request_timeout: Optional[int] = 165,
        job_completion_timeout: Optional[int] = None,
        poll_interval: Optional[int] = None,
        **kwargs
    ) -> Response:
        """
        Asynchronously scrapes content from a Target URL.

        Args:
            url (str): Direct URL to any Target page.
            store_id (Optional[int]): Set store location.
            delivery_zip (Optional[str]): Set shipping destination.
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
            "source": source.TARGET_URL,
            "url": url,
            "store_id": store_id,
            "delivery_zip": delivery_zip,
            "user_agent_type": user_agent_type,
            "render": render,
            "callback_url": callback_url,
            **kwargs,
        }
        api_response = await self._api_instance.get_response(payload, config)
        return Response(api_response)
