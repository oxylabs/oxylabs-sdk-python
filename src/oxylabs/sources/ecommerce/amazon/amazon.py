from .amazon_base import AmazonBase
from typing import Optional
from src.oxylabs.utils.utils import prepare_config


class Amazon(AmazonBase):
    def __init__(self, ecommerce_instance) -> None:
        """
        Initializes an instance of the Amazon class.

        Args:
            ecommerce_instance: The Ecommerce instance associated with the Amazon class.
        """
        self._ecommerce_instance = ecommerce_instance

    def scrape_search(
        self,
        query: str,
        opts: Optional[dict] = None,
        timeout: Optional[int] = None,
    ) -> dict:
        """
        Scrapes Amazon search results for a given query.

        Args:
            query (str): The search query.
            opts (dict, optional): Configuration options for the search. Defaults to:
                {
                    "domain": com,
                    "start_page": 1,
                    "pages": 1,
                    "geo_location": None,
                    "user_agent_type": desktop,
                    "callback_url": None,
                    "render": None,
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
        response = self._ecommerce_instance.get_resp(payload, config)
        return response

    def scrape_url(
        self,
        url: str,
        opts: Optional[dict] = None,
        timeout: Optional[int] = None,
    ) -> dict:
        """
        Scrapes Amazon search results for a given URL.

        Args:
            url (str): The URL to scrape.
            opts (dict, optional): Configuration options for the search. Defaults to:
                {
                    "domain": com,
                    "user_agent_type": desktop,
                    "callback_url": None,
                    "render": None,
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
        response = self._ecommerce_instance.get_resp(payload, config)
        return response

    def scrape_product(
        self,
        query: str,
        opts: Optional[dict] = None,
        timeout: Optional[int] = None,
    ) -> dict:
        """
        Scrapes Amazon product details for a given query.

        Args:
            query (str): 10-symbol ASIN code.
            opts (dict, optional): Configuration options for the search. Defaults to:
                {
                    "domain": com,
                    "geo_location": None,
                    "user_agent_type": desktop,
                    "callback_url": None,
                    "render": None,
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
        payload = self._prepare_product_payload(query, opts)
        response = self._ecommerce_instance.get_resp(payload, config)
        return response

    def scrape_pricing(
        self,
        query: str,
        opts: Optional[dict] = None,
        timeout: Optional[int] = None,
    ) -> dict:
        """
        Scrapes Amazon pricing details for a given query.

        Args:
            query (str): 10-symbol ASIN code.
            opts (dict, optional): Configuration options for the search. Defaults to:
                {
                    "domain": com,
                    "start_page": 1,
                    "pages": 1,
                    "geo_location": None,
                    "user_agent_type": desktop,
                    "callback_url": None,
                    "render": None,
                    "parse": None,
                    "parsing_instructions": None,
                }
                This parameter allows customization of the search request.
            timeout (int | 50, optional): The interval in seconds for the request to time out if no response is returned. Defaults to 50.

        Returns:
            dict: The response from the server after the job is completed.
        """

        config = prepare_config(timeout=timeout)
        payload = self._prepare_pricing_payload(query, opts)
        response = self._ecommerce_instance.get_resp(payload, config)
        return response

    def scrape_reviews(
        self,
        query: str,
        opts: Optional[dict] = None,
        timeout: Optional[int] = None,
    ) -> dict:
        """
        Scrapes Amazon reviews for a given query.

        Args:
            query (str): 10-symbol ASIN code.
            opts (dict, optional): Configuration options for the search. Defaults to:
                {
                    "domain": com,
                    "start_page": 1,
                    "pages": 1,
                    "geo_location": None,
                    "user_agent_type": desktop,
                    "callback_url": None,
                    "render": None,
                    "parse": None,
                    "parsing_instructions": None,
                }
                This parameter allows customization of the search request.
            timeout (int | 50, optional): The interval in seconds for the request to time out if no response is returned. Defaults to 50.

        Returns:
            dict: The response from the server after the job is completed.
        """

        config = prepare_config(timeout=timeout)
        payload = self._prepare_reviews_payload(query, opts)
        response = self._ecommerce_instance.get_resp(payload, config)
        return response

    def scrape_questions(
        self,
        query: str,
        opts: Optional[dict] = None,
        timeout: Optional[int] = None,
    ) -> dict:
        """
        Scrapes Amazon questions for a given query.

        Args:
            query (str): 10-symbol ASIN code.
            opts (dict, optional): Configuration options for the search. Defaults to:
                {
                    "domain": com,
                    "geo_location": None,
                    "user_agent_type": desktop,
                    "callback_url": None,
                    "render": None,
                    "parse": None,
                    "parsing_instructions": None,
                }
                This parameter allows customization of the search request.
            timeout (int | 50, optional): The interval in seconds for the request to time out if no response is returned. Defaults to 50.

        Returns:
            dict: The response from the server after the job is completed.
        """

        config = prepare_config(timeout=timeout)
        payload = self._prepare_questions_payload(query, opts)
        response = self._ecommerce_instance.get_resp(payload, config)
        return response

    def scrape_bestsellers(
        self,
        query: str,
        opts: Optional[dict] = None,
        timeout: Optional[int] = None,
    ) -> dict:
        """
        Scrapes Amazon bestsellers.

        Args:
            query (str): Browse node ID.
            opts (dict, optional): Configuration options for the search. Defaults to:
                {
                    "domain": com,
                    "start_page": 1,
                    "pages": 1,
                    "geo_location": None,
                    "user_agent_type": desktop,
                    "callback_url": None,
                    "render": None,
                    "parse": None,
                    "parsing_instructions": None,
                }
                This parameter allows customization of the search request.
            timeout (int | 50, optional): The interval in seconds for the request to time out if no response is returned. Defaults to 50.

        Returns:
            dict: The response from the server after the job is completed.
        """

        config = prepare_config(timeout=timeout)
        payload = self._prepare_bestseller_payload(query, opts)
        response = self._ecommerce_instance.get_resp(payload, config)
        return response

    def scrape_sellers(
        self,
        query: str,
        opts: Optional[dict] = None,
        timeout: Optional[int] = None,
    ) -> dict:
        """
        Scrapes Amazon sellers for a given query.

        Args:
            query (str): 13-character seller ID.
            opts (dict, optional): Configuration options for the search. Defaults to:
                {
                    "domain": com,
                    "geo_location": None,
                    "user_agent_type": desktop,
                    "callback_url": None,
                    "render": None,
                    "parse": None,
                    "parsing_instructions": None,
                }
                This parameter allows customization of the search request.
            timeout (int | 50, optional): The interval in seconds for the request to time out if no response is returned. Defaults to 50.

        Returns:
            dict: The response from the server after the job is completed.
        """

        config = prepare_config(timeout=timeout)
        payload = self._prepare_seller_payload(query, opts)
        response = self._ecommerce_instance.get_resp(payload, config)
        return response


class AmazonAsync(AmazonBase):
    def __init__(self, ecommerce_async_instance) -> None:
        """
        Initializes an instance of the AmazonAsync class.

        Args:
            ecommerce_async_instance: The EcommerceAsync instance associated with the AmazonAsync class.
        """
        self._ecommerce_async_instance = ecommerce_async_instance

    async def scrape_search(
        self,
        query: str,
        opts: Optional[dict] = None,
        timeout: Optional[int] = None,
        poll_interval: Optional[int] = None,
    ) -> dict:
        """
        Scrapes Amazon search results for a given query.

        Args:
            query (str): The search query.
            opts (dict, optional): Configuration options for the search. Defaults to:
                {
                    "domain": com,
                    "start_page": 1,
                    "pages": 1,
                    "geo_location": None,
                    "user_agent_type": desktop,
                    "callback_url": None,
                    "render": None,
                    "parse": None,
                    "context": None,
                    "parsing_instructions": None,
                }
                This parameter allows customization of the search request.
            timeout (int | 50, optional): The interval in seconds for the request to time out if no response is returned. Defaults to 50.
            poll_interval (int | 2, optional): The interval in seconds to poll the server for a response. Defaults to 2

        Returns:
            dict: The response from the server after the job is completed.
        """

        config = prepare_config(timeout=timeout, poll_interval=poll_interval)
        payload = self._prepare_search_payload(query, opts)
        response = await self._ecommerce_async_instance.get_resp(payload, config)
        return response

    async def scrape_url(
        self,
        url: str,
        opts: Optional[dict] = None,
        timeout: Optional[int] = None,
        poll_interval: Optional[int] = None,
    ) -> dict:
        """
        Scrapes Amazon search results for a given URL.

        Args:
            url (str): The URL to scrape.
            opts (dict, optional): Configuration options for the search. Defaults to:
                {
                    "domain": com,
                    "user_agent_type": desktop,
                    "callback_url": None,
                    "render": None,
                    "parse": None,
                    "parsing_instructions": None,
                }
                This parameter allows customization of the search request.
            timeout (int | 50, optional): The interval in seconds for the request to time out if no response is returned. Defaults to 50.
            poll_interval (int | 2, optional): The interval in seconds to poll the server for a response. Defaults to 2

        Returns:
            dict: The response from the server after the job is completed.
        """

        config = prepare_config(timeout=timeout, poll_interval=poll_interval)
        payload = self._prepare_url_payload(url, opts)
        response = await self._ecommerce_async_instance.get_resp(payload, config)
        return response

    async def scrape_product(
        self,
        query: str,
        opts: Optional[dict] = None,
        timeout: Optional[int] = None,
        poll_interval: Optional[int] = None,
    ) -> dict:
        """
        Scrapes Amazon product details for a given query.

        Args:
            query (str): 10-symbol ASIN code.
            opts (dict, optional): Configuration options for the search. Defaults to:
                {
                    "domain": com,
                    "geo_location": None,
                    "user_agent_type": desktop,
                    "callback_url": None,
                    "render": None,
                    "parse": None,
                    "context": None,
                    "parsing_instructions": None,
                }
                This parameter allows customization of the search request.
            timeout (int | 50, optional): The interval in seconds for the request to time out if no response is returned. Defaults to 50.
            poll_interval (int | 2, optional): The interval in seconds to poll the server for a response. Defaults to 2

        Returns:
            dict: The response from the server after the job is completed.
        """

        config = prepare_config(timeout=timeout, poll_interval=poll_interval)
        payload = self._prepare_product_payload(query, opts)
        response = await self._ecommerce_async_instance.get_resp(payload, config)
        return response

    async def scrape_pricing(
        self,
        query: str,
        opts: Optional[dict] = None,
        timeout: Optional[int] = None,
        poll_interval: Optional[int] = None,
    ) -> dict:
        """
        Scrapes Amazon pricing details for a given query.

        Args:
            query (str): 10-symbol ASIN code.
            opts (dict, optional): Configuration options for the search. Defaults to:
                {
                    "domain": com,
                    "start_page": 1,
                    "pages": 1,
                    "geo_location": None,
                    "user_agent_type": desktop,
                    "callback_url": None,
                    "render": None,
                    "parse": None,
                    "parsing_instructions": None,
                }
                This parameter allows customization of the search request.
            timeout (int | 50, optional): The interval in seconds for the request to time out if no response is returned. Defaults to 50.
            poll_interval (int | 2, optional): The interval in seconds to poll the server for a response. Defaults to 2

        Returns:
            dict: The response from the server after the job is completed.
        """

        config = prepare_config(timeout=timeout, poll_interval=poll_interval)
        payload = self._prepare_pricing_payload(query, opts)
        response = await self._ecommerce_async_instance.get_resp(payload, config)
        return response

    async def scrape_reviews(
        self,
        query: str,
        opts: Optional[dict] = None,
        timeout: Optional[int] = None,
        poll_interval: Optional[int] = None,
    ) -> dict:
        """
        Scrapes Amazon reviews for a given query.

        Args:
            query (str): 10-symbol ASIN code.
            opts (dict, optional): Configuration options for the search. Defaults to:
                {
                    "domain": com,
                    "start_page": 1,
                    "pages": 1,
                    "geo_location": None,
                    "user_agent_type": desktop,
                    "callback_url": None,
                    "render": None,
                    "parse": None,
                    "parsing_instructions": None,
                }
                This parameter allows customization of the search request.
            timeout (int | 50, optional): The interval in seconds for the request to time out if no response is returned. Defaults to 50.
            poll_interval (int | 2, optional): The interval in seconds to poll the server for a response. Defaults to 2

        Returns:
            dict: The response from the server after the job is completed.
        """

        config = prepare_config(timeout=timeout, poll_interval=poll_interval)
        payload = self._prepare_reviews_payload(query, opts)
        response = await self._ecommerce_async_instance.get_resp(payload, config)
        return response

    async def scrape_questions(
        self,
        query: str,
        opts: Optional[dict] = None,
        timeout: Optional[int] = None,
        poll_interval: Optional[int] = None,
    ) -> dict:
        """
        Scrapes Amazon questions for a given query.

        Args:
            query (str): 10-symbol ASIN code.
            opts (dict, optional): Configuration options for the search. Defaults to:
                {
                    "domain": com,
                    "geo_location": None,
                    "user_agent_type": desktop,
                    "callback_url": None,
                    "render": None,
                    "parse": None,
                    "parsing_instructions": None,
                }
                This parameter allows customization of the search request.
            timeout (int | 50, optional): The interval in seconds for the request to time out if no response is returned. Defaults to 50.
            poll_interval (int | 2, optional): The interval in seconds to poll the server for a response. Defaults to 2

        Returns:
            dict: The response from the server after the job is completed.
        """

        config = prepare_config(timeout=timeout, poll_interval=poll_interval)
        payload = self._prepare_questions_payload(query, opts)
        response = await self._ecommerce_async_instance.get_resp(payload, config)
        return response

    async def scrape_bestsellers(
        self,
        query,
        opts: Optional[dict] = None,
        timeout: Optional[int] = None,
        poll_interval: Optional[int] = None,
    ) -> dict:
        """
        Scrapes Amazon bestsellers.

        Args:
            query (str): Browse node ID.
            opts (dict, optional): Configuration options for the search. Defaults to:
                {
                    "domain": com,
                    "start_page": 1,
                    "pages": 1,
                    "geo_location": None,
                    "user_agent_type": desktop,
                    "callback_url": None,
                    "render": None,
                    "parse": None,
                    "parsing_instructions": None,
                }
                This parameter allows customization of the search request.
            timeout (int | 50, optional): The interval in seconds for the request to time out if no response is returned. Defaults to 50.
            poll_interval (int | 2, optional): The interval in seconds to poll the server for a response. Defaults to 2

        Returns:
            dict: The response from the server after the job is completed.
        """

        config = prepare_config(timeout=timeout, poll_interval=poll_interval)
        payload = self._prepare_bestseller_payload(query, opts)
        response = await self._ecommerce_async_instance.get_resp(payload, config)
        return response

    async def scrape_sellers(
        self,
        query: str,
        opts: Optional[dict] = None,
        timeout: Optional[int] = None,
        poll_interval: Optional[int] = None,
    ) -> dict:
        """
        Scrapes Amazon sellers for a given query.

        Args:
            query (str): 13-character seller ID.
            opts (dict, optional): Configuration options for the search. Defaults to:
                {
                    "domain": com,
                    "geo_location": None,
                    "user_agent_type": desktop,
                    "callback_url": None,
                    "render": None,
                    "parse": None,
                    "parsing_instructions": None,
                }
                This parameter allows customization of the search request.
            timeout (int | 50, optional): The interval in seconds for the request to time out if no response is returned. Defaults to 50.
            poll_interval (int | 2, optional): The interval in seconds to poll the server for a response. Defaults to 2

        Returns:
            dict: The response from the server after the job is completed.
        """

        config = prepare_config(timeout=timeout, poll_interval=poll_interval)
        payload = self._prepare_seller_payload(query, opts)
        response = await self._ecommerce_async_instance.get_resp(payload, config)
        return response
