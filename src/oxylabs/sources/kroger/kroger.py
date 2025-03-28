from typing import Optional

from oxylabs.internal.api import RealtimeAPI, AsyncAPI
from oxylabs.sources.response import Response
from oxylabs.utils.types import source
from oxylabs.utils.utils import prepare_config


class Kroger:
    def __init__(self, api_instance:RealtimeAPI) -> None:
        """
        Initializes an instance of the Kroger class.

        Args:
            api_instance: An instance of the RealtimeAPI class used for making requests.
        """
        self._api_instance = api_instance

    def scrape_product(
        self,
        product_id: str,
        render: Optional[str] = None,
        callback_url: Optional[str] = None,
        user_agent_type: Optional[str] = None,
        store_id: Optional[int] = None,
        delivery_zip: Optional[str] = None,
        fulfillment_type: Optional[str] = None,
        request_timeout: Optional[int] = 165,
        **kwargs
    ) -> Response:
        """
        Scrapes Kroger product page for a given query and product ID.

        Args:
            product_id (str): The product ID.
            render (Optional[str]): Enables JavaScript rendering.
            callback_url (Optional[str]): URL to your callback endpoint.
            user_agent_type (Optional[str]): Device type and browser.
            store_id (Optional[int]): The store ID.
            delivery_zip (Optional[str]): The delivery location ZIP code.
            fulfillment_type (Optional[str]): The Fulfillment method.
            request_timeout (int | 165, optional): The interval in seconds for
                            the request to time out if no response is returned.
                            Defaults to 165.

        Returns:
            Response: The response from the server after the job is completed.
        """

        config = prepare_config(request_timeout=request_timeout)
        payload = {
            "source": source.KROGER_PRODUCT,
            "product_id": product_id,
            "render": render,
            "callback_url": callback_url,
            "user_agent_type": user_agent_type,
            "store_id": store_id,
            "delivery_zip": delivery_zip,
            "fulfillment_type": fulfillment_type,
            **kwargs,
        }
        api_response = self._api_instance.get_response(payload, config)
        return Response(api_response)

    def scrape_search(
        self,
        query: str,
        render: Optional[str] = None,
        callback_url: Optional[str] = None,
        user_agent_type: Optional[str] = None,
        store_id: Optional[int] = None,
        delivery_zip: Optional[str] = None,
        fulfillment_type: Optional[str] = None,
        request_timeout: Optional[int] = 165,
        **kwargs
    ) -> Response:
        """
        Scrapes Kroger search page for a given query.

        Args:
            query (str): The search query.
            render (Optional[str]): Enables JavaScript rendering.
            callback_url (Optional[str]): URL to your callback endpoint.
            user_agent_type (Optional[str]): Device type and browser.
            store_id (Optional[int]): The store ID.
            delivery_zip (Optional[str]): The delivery location ZIP code.
            fulfillment_type (Optional[str]): The Fulfillment method.
            request_timeout (int | 165, optional): The interval in seconds for
                            the request to time out if no response is returned.
                            Defaults to 165.

        Returns:
            Response: The response from the server after the job is completed.
        """

        config = prepare_config(request_timeout=request_timeout)
        payload = {
            "source": source.KROGER_SEARCH,
            "query": query,
            "render": render,
            "callback_url": callback_url,
            "user_agent_type": user_agent_type,
            "store_id": store_id,
            "delivery_zip": delivery_zip,
            "fulfillment_type": fulfillment_type,
            **kwargs,
        }
        api_response = self._api_instance.get_response(payload, config)
        return Response(api_response)

    def scrape_url(
        self,
        url: str,
        render: Optional[str] = None,
        callback_url: Optional[str] = None,
        user_agent_type: Optional[str] = None,
        store_id: Optional[int] = None,
        delivery_zip: Optional[str] = None,
        fulfillment_type: Optional[str] = None,
        request_timeout: Optional[int] = 165,
        **kwargs
    ) -> Response:
        """
        Scrapes Kroger page for a given URL.

        Args:
            url (str): Direct URL (link) to Kroger page.
            render (Optional[str]): Enables JavaScript rendering.
            callback_url (Optional[str]): URL to your callback endpoint.
            user_agent_type (Optional[str]): Device type and browser.
            store_id (Optional[int]): The store ID.
            delivery_zip (Optional[str]): The delivery location ZIP code.
            fulfillment_type (Optional[str]): The Fulfillment method.
            request_timeout (int | 165, optional): The interval in seconds for
                            the request to time out if no response is returned.
                            Defaults to 165.

        Returns:
            Response: The response from the server after the job is completed.
        """

        config = prepare_config(request_timeout=request_timeout)
        payload = {
            "source": source.KROGER,
            "url": url,
            "render": render,
            "callback_url": callback_url,
            "user_agent_type": user_agent_type,
            "store_id": store_id,
            "delivery_zip": delivery_zip,
            "fulfillment_type": fulfillment_type,
            **kwargs,
        }
        api_response = self._api_instance.get_response(payload, config)
        return Response(api_response)


class KrogerAsync:
    def __init__(self, api_instance:AsyncAPI) -> None:
        """
        Initializes an instance of the Kroger class.

        Args:
            api_instance: An instance of the AsyncAPI class used for making requests.
        """
        self._api_instance = api_instance

    async def scrape_product(
        self,
        product_id: str,
        render: Optional[str] = None,
        callback_url: Optional[str] = None,
        user_agent_type: Optional[str] = None,
        store_id: Optional[int] = None,
        delivery_zip: Optional[str] = None,
        fulfillment_type: Optional[str] = None,
        request_timeout: Optional[int] = 165,
        job_completion_timeout: Optional[int] = None,
        poll_interval: Optional[int] = None,
        **kwargs
    ) -> Response:
        """
        Asynchronously scrapes Kroger product page for a given query and product ID.

        Args:
            product_id (str): The product ID.
            render (Optional[str]): Enables JavaScript rendering.
            callback_url (Optional[str]): URL to your callback endpoint.
            user_agent_type (Optional[str]): Device type and browser.
            store_id (Optional[int]): The store ID.
            delivery_zip (Optional[str]): The delivery location ZIP code.
            fulfillment_type (Optional[str]): The Fulfillment method.
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
            "source": source.KROGER_PRODUCT,
            "product_id": product_id,
            "render": render,
            "callback_url": callback_url,
            "user_agent_type": user_agent_type,
            "store_id": store_id,
            "delivery_zip": delivery_zip,
            "fulfillment_type": fulfillment_type,
            **kwargs,
        }
        api_response = await self._api_instance.get_response(payload, config)
        return Response(api_response)

    async def scrape_search(
        self,
        query: str,
        render: Optional[str] = None,
        callback_url: Optional[str] = None,
        user_agent_type: Optional[str] = None,
        store_id: Optional[int] = None,
        delivery_zip: Optional[str] = None,
        fulfillment_type: Optional[str] = None,
        request_timeout: Optional[int] = 165,
        job_completion_timeout: Optional[int] = None,
        poll_interval: Optional[int] = None,
        **kwargs
    ) -> Response:
        """
        Asynchronously scrapes Kroger search page for a given query.

        Args:
            query (str): The search query.
            render (Optional[str]): Enables JavaScript rendering.
            callback_url (Optional[str]): URL to your callback endpoint.
            user_agent_type (Optional[str]): Device type and browser.
            store_id (Optional[int]): The store ID.
            delivery_zip (Optional[str]): The delivery location ZIP code.
            fulfillment_type (Optional[str]): The Fulfillment method.
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
            "source": source.KROGER_SEARCH,
            "query": query,
            "render": render,
            "callback_url": callback_url,
            "user_agent_type": user_agent_type,
            "store_id": store_id,
            "delivery_zip": delivery_zip,
            "fulfillment_type": fulfillment_type,
            **kwargs,
        }
        api_response = await self._api_instance.get_response(payload, config)
        return Response(api_response)

    async def scrape_url(
        self,
        url: str,
        render: Optional[str] = None,
        callback_url: Optional[str] = None,
        user_agent_type: Optional[str] = None,
        store_id: Optional[int] = None,
        delivery_zip: Optional[str] = None,
        fulfillment_type: Optional[str] = None,
        request_timeout: Optional[int] = 165,
        job_completion_timeout: Optional[int] = None,
        poll_interval: Optional[int] = None,
        **kwargs
    ) -> Response:
        """
        Asynchronously scrapes Kroger page for a given URL.

        Args:
            url (str): Direct URL (link) to Kroger page.
            render (Optional[str]): Enables JavaScript rendering.
            callback_url (Optional[str]): URL to your callback endpoint.
            user_agent_type (Optional[str]): Device type and browser.
            store_id (Optional[int]): The store ID.
            delivery_zip (Optional[str]): The delivery location ZIP code.
            fulfillment_type (Optional[str]): The Fulfillment method.
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
            "source": source.KROGER,
            "url": url,
            "render": render,
            "callback_url": callback_url,
            "user_agent_type": user_agent_type,
            "store_id": store_id,
            "delivery_zip": delivery_zip,
            "fulfillment_type": fulfillment_type,
            **kwargs,
        }
        api_response = await self._api_instance.get_response(payload, config)
        return Response(api_response)
