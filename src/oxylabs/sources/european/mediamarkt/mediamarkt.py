from typing import Optional

from oxylabs.internal.api import RealtimeAPI, AsyncAPI
from oxylabs.sources.response import Response
from oxylabs.utils.types import source
from oxylabs.utils.utils import prepare_config


class Mediamarkt:
    def __init__(self, api_instance: RealtimeAPI) -> None:
        """
        Initializes an instance of the Mediamarkt class.

        Args:
            api_instance: An instance of the RealtimeAPI class used for making requests.
        """
        self._api_instance = api_instance

    def scrape_search(
        self,
        query: str,
        domain: Optional[str] = None,
        start_page: Optional[int] = None,
        user_agent_type: Optional[str] = None,
        render: Optional[str] = None,
        callback_url: Optional[str] = None,
        request_timeout: Optional[int] = 165,
        **kwargs
    ) -> Response:
        """
        Scrapes MediaMarkt search results for a given query.

        Args:
            query (str): The keyword or phrase to search for.
            domain (Optional[str]): Domain localization. Accepted values:
                            "de", "es", "pl", "nl", "hu", "ch", "at", "com.tr".
            start_page (Optional[int]): The starting page number.
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
            "source": source.MEDIAMARKT_SEARCH,
            "query": query,
            "domain": domain,
            "start_page": start_page,
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
        domain: Optional[str] = None,
        user_agent_type: Optional[str] = None,
        render: Optional[str] = None,
        callback_url: Optional[str] = None,
        request_timeout: Optional[int] = 165,
        **kwargs
    ) -> Response:
        """
        Scrapes a MediaMarkt product page for a given product ID.

        Args:
            product_id (str): MediaMarkt product ID.
            domain (Optional[str]): Domain localization. Accepted values:
                            "de", "es", "pl", "nl", "hu", "ch", "at", "com.tr".
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
            "source": source.MEDIAMARKT_PRODUCT,
            "product_id": product_id,
            "domain": domain,
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
        user_agent_type: Optional[str] = None,
        render: Optional[str] = None,
        callback_url: Optional[str] = None,
        request_timeout: Optional[int] = 165,
        **kwargs
    ) -> Response:
        """
        Scrapes content from a MediaMarkt URL.

        Args:
            url (str): Direct URL to any MediaMarkt page.
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
            "source": source.MEDIAMARKT_URL,
            "url": url,
            "user_agent_type": user_agent_type,
            "render": render,
            "callback_url": callback_url,
            **kwargs,
        }
        api_response = self._api_instance.get_response(payload, config)
        return Response(api_response)


class MediamarktAsync:
    def __init__(self, api_instance: AsyncAPI) -> None:
        """
        Initializes an instance of the MediamarktAsync class.

        Args:
            api_instance: An instance of the AsyncAPI class used for making requests.
        """
        self._api_instance = api_instance

    async def scrape_search(
        self,
        query: str,
        domain: Optional[str] = None,
        start_page: Optional[int] = None,
        user_agent_type: Optional[str] = None,
        render: Optional[str] = None,
        callback_url: Optional[str] = None,
        request_timeout: Optional[int] = 165,
        job_completion_timeout: Optional[int] = None,
        poll_interval: Optional[int] = None,
        **kwargs
    ) -> Response:
        """
        Asynchronously scrapes MediaMarkt search results for a given query.

        Args:
            query (str): The keyword or phrase to search for.
            domain (Optional[str]): Domain localization. Accepted values:
                            "de", "es", "pl", "nl", "hu", "ch", "at", "com.tr".
            start_page (Optional[int]): The starting page number.
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
            "source": source.MEDIAMARKT_SEARCH,
            "query": query,
            "domain": domain,
            "start_page": start_page,
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
        domain: Optional[str] = None,
        user_agent_type: Optional[str] = None,
        render: Optional[str] = None,
        callback_url: Optional[str] = None,
        request_timeout: Optional[int] = 165,
        job_completion_timeout: Optional[int] = None,
        poll_interval: Optional[int] = None,
        **kwargs
    ) -> Response:
        """
        Asynchronously scrapes a MediaMarkt product page for a given product ID.

        Args:
            product_id (str): MediaMarkt product ID.
            domain (Optional[str]): Domain localization. Accepted values:
                            "de", "es", "pl", "nl", "hu", "ch", "at", "com.tr".
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
            "source": source.MEDIAMARKT_PRODUCT,
            "product_id": product_id,
            "domain": domain,
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
        user_agent_type: Optional[str] = None,
        render: Optional[str] = None,
        callback_url: Optional[str] = None,
        request_timeout: Optional[int] = 165,
        job_completion_timeout: Optional[int] = None,
        poll_interval: Optional[int] = None,
        **kwargs
    ) -> Response:
        """
        Asynchronously scrapes content from a MediaMarkt URL.

        Args:
            url (str): Direct URL to any MediaMarkt page.
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
            "source": source.MEDIAMARKT_URL,
            "url": url,
            "user_agent_type": user_agent_type,
            "render": render,
            "callback_url": callback_url,
            **kwargs,
        }
        api_response = await self._api_instance.get_response(payload, config)
        return Response(api_response)
