from .universal_base import UniversalBase
from typing import Optional, Dict, Any
from .ecommerce import InitEcommerce, InitEcommerceAsync
from oxylabs.utils.utils import prepare_config


class Universal(UniversalBase):
    def __init__(self, client):
        if not isinstance(client, InitEcommerce):
            raise TypeError("Universal requires an Ecommerce instance")
        self.client = client

    def scrape_universal_url(
        self, url: str, opts: Optional[dict] = None, timeout: int = None
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

        config = prepare_config(timeout=timeout)
        payload = self._prepare_universal_url_payload(url, opts)
        response = self.client.get_resp(payload, config)
        return response


class UniversalAsync(UniversalBase):
    def __init__(self, client):
        if not isinstance(client, InitEcommerceAsync):
            raise TypeError(
                "UniversalAsync requires an EcommerceAsync instance"
            )
        self.client = client

    async def scrape_universal_url(
        self,
        url: str,
        opts: Optional[dict] = None,
        timeout: int = None,
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

        config = prepare_config(timeout=timeout, poll_interval=poll_interval)
        payload = self._prepare_universal_url_payload(url, opts)
        response = await self.client.get_resp(payload, config)
        return response
