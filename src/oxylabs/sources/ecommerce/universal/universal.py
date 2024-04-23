from typing import Optional

from src.oxylabs.utils.utils import prepare_config

from .universal_base import UniversalBase


class Universal(UniversalBase):
    def __init__(self, ecommerce_instance) -> None:
        """
        Initializes an instance of the Universal class.

        Args:
            ecommerce_instance: The Ecommerce instance associated with the Universal class.
        """
        self._ecommerce_instance = ecommerce_instance

    def scrape_url(
        self, url: str, opts: Optional[dict] = None, request_timeout: int = None
    ) -> dict:
        """
        Scrapes Universal search results for a given URL.

        Args:
            url (str): The URL to be scraped.
            opts (UniversalUrlOpts, optional): Configuration options for the search. Defaults to:
                {
                    "user_agent_type": desktop,
                    "geo_location": None,
                    "locale": None,
                    "render": None,
                    "content_encoding": "base64",
                    "context": None,
                    "callback_url": None,
                    "parse": None,
                    "parser_type": None,
                    "parsing_instructions": None,
                }
                This parameter allows customization of the search request.
            timeout (int | 50, optional): The interval in seconds for the request to time out if no response is returned. Defaults to 50.

        Returns:
            dict: The response from the server after the job is completed.
        """

        config = prepare_config(request_timeout=request_timeout)
        payload = self._prepare_url_payload(url, opts)
        response = self.client.get_resp(payload, config)
        return response


class UniversalAsync(UniversalBase):
    def __init__(self, ecommerce_async_instance) -> None:
        """
        Initializes an instance of the UniversalAsync class.

        Args:
            ecommerce_async_instance: The EcommerceAsync instance associated with the UniversalAsync class.
        """
        self._ecommerce_async_instance = ecommerce_async_instance

    async def scrape_url(
        self,
        url: str,
        opts: Optional[dict] = None,
        request_timeout: int = None,
        job_completion_timeout: int = None,
        poll_interval: int = None,
    ) -> dict:
        """
        Asynchronously scrapes Universal search results for a given URL.

        Args:
            url (str): The URL to be scraped.
            opts (UniversalUrlOpts, optional): Configuration options for the search. Defaults to:
                {
                    "user_agent_type": desktop,
                    "geo_location": None,
                    "locale": None,
                    "render": None,
                    "content_encoding": "base64",
                    "context": None,
                    "callback_url": None,
                    "parse": None,
                    "parser_type": None,
                    "parsing_instructions": None,
                }
                This parameter allows customization of the search request.
            timeout (int | 50, optional): The interval in seconds for the request to time out if no response is returned. Defaults to 50.
            poll_interval (int | 2, optional): The interval in seconds to poll the server for a response. Defaults to 2.

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
        response = await self._ecommerce_async_instance.get_resp(payload, config)
        return response
