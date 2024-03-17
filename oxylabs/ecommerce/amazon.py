from .amazon_base import AmazonBase
from typing import Optional, Dict, Any
from .ecommerce import InitEcommerce, InitEcommerceAsync
from oxylabs.utils.utils import prepare_config


class Amazon(AmazonBase):
    def __init__(self, client: InitEcommerce) -> None:
        """
        Initializes an Amazon instance.

        Args:
            client (Ecommerce): An instance of the Ecommerce class.

        Raises:
            TypeError: If the client parameter is not an instance of Ecommerce.
        """
        if not isinstance(client, InitEcommerce):
            raise TypeError("Amazon requires an Ecommerce instance")
        self.client = client

    def scrape_amazon_search(
        self,
        query: str,
        opts: Optional[Dict[str, Any]] = None,
        timeout: Optional[int] = None,
    ) -> Dict[str, Any]:
        """
        Scrapes Amazon search results for a given query.

        Args:
            query (str): The search query.
            opts (dict, optional): Configuration options for the search. Defaults to:
                {
                    "domain": com,
                    "start_page": 1,
                    "pages": 1,
                    "locale": None,
                    "results_language": None,
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
        payload = self._prepare_amazon_search_payload(query, opts)
        response = self.client.get_resp(payload, config)
        return response

    def scrape_amazon_url(
        self,
        url: str,
        opts: Optional[Dict[str, Any]] = None,
        timeout: Optional[int] = None,
    ) -> Dict[str, Any]:
        """
        Scrapes Amazon search results for a given URL.

        Args:
            url (str): The URL to scrape.
            opts (dict, optional): Configuration options for the search. Defaults to:
                {
                    "domain": com,
                    "locale": None,
                    "results_language": None,
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
        payload = self._prepare_amazon_url_payload(url, opts)
        response = self.client.get_resp(payload, config)
        return response

    def scrape_amazon_product(
        self,
        query: str,
        opts: Optional[Dict[str, Any]] = None,
        timeout: Optional[int] = None,
    ) -> Dict[str, Any]:
        """
        Scrapes Amazon product details for a given query.

        Args:
            query (str): 10-symbol ASIN code.
            opts (dict, optional): Configuration options for the search. Defaults to:
                {
                    "domain": com,
                    "locale": None,
                    "results_language": None,
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
        payload = self._prepare_amazon_product_payload(query, opts)
        response = self.client.get_resp(payload, config)
        return response

    def scrape_amazon_pricing(
        self,
        query: str,
        opts: Optional[Dict[str, Any]] = None,
        timeout: Optional[int] = None,
    ) -> Dict[str, Any]:
        """
        Scrapes Amazon pricing details for a given query.

        Args:
            query (str): 10-symbol ASIN code.
            opts (dict, optional): Configuration options for the search. Defaults to:
                {
                    "domain": com,
                    "locale": None,
                    "results_language": None,
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
        payload = self._prepare_amazon_pricing_payload(query, opts)
        response = self.client.get_resp(payload, config)
        return response

    def scrape_amazon_reviews(
        self,
        query: str,
        opts: Optional[Dict[str, Any]] = None,
        timeout: Optional[int] = None,
    ) -> Dict[str, Any]:
        """
        Scrapes Amazon reviews for a given query.

        Args:
            query (str): 10-symbol ASIN code.
            opts (dict, optional): Configuration options for the search. Defaults to:
                {
                    "domain": com,
                    "start_page": 1,
                    "pages": 1,
                    "locale": None,
                    "results_language": None,
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
        payload = self._prepare_amazon_reviews_payload(query, opts)
        response = self.client.get_resp(payload, config)
        return response

    def scrape_amazon_questions(
        self,
        query: str,
        opts: Optional[Dict[str, Any]] = None,
        timeout: Optional[int] = None,
    ) -> Dict[str, Any]:
        """
        Scrapes Amazon questions for a given query.

        Args:
            query (str): 10-symbol ASIN code.
            opts (dict, optional): Configuration options for the search. Defaults to:
                {
                    "domain": com,
                    "start_page": 1,
                    "pages": 1,
                    "locale": None,
                    "results_language": None,
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
        payload = self._prepare_amazon_questions_payload(query, opts)
        response = self.client.get_resp(payload, config)
        return response

    def scrape_amazon_bestsellers(
        self,
        query: str,
        opts: Optional[Dict[str, Any]] = None,
        timeout: Optional[int] = None,
    ) -> Dict[str, Any]:
        """
        Scrapes Amazon bestsellers.

        Args:
            query (str): Browse node ID.
            opts (dict, optional): Configuration options for the search. Defaults to:
                {
                    "domain": com,
                    "start_page": 1,
                    "pages": 1,
                    "locale": None,
                    "results_language": None,
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
        payload = self._prepare_amazon_bestseller_payload(query, opts)
        response = self.client.get_resp(payload, config)
        return response

    def scrape_amazon_sellers(
        self,
        query: str,
        opts: Optional[Dict[str, Any]] = None,
        timeout: Optional[int] = None,
    ) -> Dict[str, Any]:
        """
        Scrapes Amazon sellers for a given query.

        Args:
            query (str): 13-character seller ID.
            opts (dict, optional): Configuration options for the search. Defaults to:
                {
                    "domain": com,
                    "start_page": 1,
                    "pages": 1,
                    "locale": None,
                    "results_language": None,
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
        payload = self._prepare_amazon_seller_payload(query, opts)
        response = self.client.get_resp(payload, config)
        return response


class AmazonAsync(AmazonBase):
    def __init__(self, client: InitEcommerceAsync) -> None:
        """
        Initializes an instance of AmazonAsync.

        Args:
            client (EcommerceAsync): An instance of EcommerceAsync.

        Raises:
            TypeError: If the client parameter is not an instance of EcommerceAsync.
        """
        if not isinstance(client, InitEcommerceAsync):
            raise TypeError("AmazonAsync requires an EcommerceAsync instance")
        self.client = client

    async def scrape_amazon_search(
        self,
        query: str,
        opts: Optional[Dict[str, Any]] = None,
        timeout: Optional[int] = None,
        poll_interval: Optional[int] = None,
    ) -> Dict[str, Any]:
        """
        Scrapes Amazon search results for a given query.

        Args:
            query (str): The search query.
            opts (dict, optional): Configuration options for the search. Defaults to:
                {
                    "domain": com,
                    "start_page": 1,
                    "pages": 1,
                    "locale": None,
                    "results_language": None,
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
        payload = self._prepare_amazon_search_payload(query, opts)
        response = await self.client.get_resp(payload, config)
        return response

    async def scrape_amazon_url(
        self,
        url: str,
        opts: Optional[Dict[str, Any]] = None,
        timeout: Optional[int] = None,
        poll_interval: Optional[int] = None,
    ) -> Dict[str, Any]:
        """
        Scrapes Amazon search results for a given URL.

        Args:
            url (str): The URL to scrape.
            opts (dict, optional): Configuration options for the search. Defaults to:
                {
                    "domain": com,
                    "locale": None,
                    "results_language": None,
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
        payload = self._prepare_amazon_url_payload(url, opts)
        response = await self.client.get_resp(payload, config)
        return response

    async def scrape_amazon_product(
        self,
        query: str,
        opts: Optional[Dict[str, Any]] = None,
        timeout: Optional[int] = None,
        poll_interval: Optional[int] = None,
    ) -> Dict[str, Any]:
        """
        Scrapes Amazon product details for a given query.

        Args:
            query (str): 10-symbol ASIN code.
            opts (dict, optional): Configuration options for the search. Defaults to:
                {
                    "domain": com,
                    "locale": None,
                    "results_language": None,
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
        payload = self._prepare_amazon_product_payload(query, opts)
        response = await self.client.get_resp(payload, config)
        return response

    async def scrape_amazon_pricing(
        self,
        query: str,
        opts: Optional[Dict[str, Any]] = None,
        timeout: Optional[int] = None,
        poll_interval: Optional[int] = None,
    ) -> Dict[str, Any]:
        """
        Scrapes Amazon pricing details for a given query.

        Args:
            query (str): 10-symbol ASIN code.
            opts (dict, optional): Configuration options for the search. Defaults to:
                {
                    "domain": com,
                    "locale": None,
                    "results_language": None,
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
        payload = self._prepare_amazon_pricing_payload(query, opts)
        response = await self.client.get_resp(payload, config)
        return response

    async def scrape_amazon_reviews(
        self,
        query: str,
        opts: Optional[Dict[str, Any]] = None,
        timeout: Optional[int] = None,
        poll_interval: Optional[int] = None,
    ) -> Dict[str, Any]:
        """
        Scrapes Amazon reviews for a given query.

        Args:
            query (str): 10-symbol ASIN code.
            opts (dict, optional): Configuration options for the search. Defaults to:
                {
                    "domain": com,
                    "start_page": 1,
                    "pages": 1,
                    "locale": None,
                    "results_language": None,
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
        payload = self._prepare_amazon_reviews_payload(query, opts)
        response = await self.client.get_resp(payload, config)
        return response

    async def scrape_amazon_questions(
        self,
        query: str,
        opts: Optional[Dict[str, Any]] = None,
        timeout: Optional[int] = None,
        poll_interval: Optional[int] = None,
    ) -> Dict[str, Any]:
        """
        Scrapes Amazon questions for a given query.

        Args:
            query (str): 10-symbol ASIN code.
            opts (dict, optional): Configuration options for the search. Defaults to:
                {
                    "domain": com,
                    "start_page": 1,
                    "pages": 1,
                    "locale": None,
                    "results_language": None,
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
        payload = self._prepare_amazon_questions_payload(query, opts)
        response = await self.client.get_resp(payload, config)
        return response

    async def scrape_amazon_bestsellers(
        self,
        query,
        opts: Optional[Dict[str, Any]] = None,
        timeout: Optional[int] = None,
        poll_interval: Optional[int] = None,
    ) -> Dict[str, Any]:
        """
        Scrapes Amazon bestsellers.

        Args:
            query (str): Browse node ID.
            opts (dict, optional): Configuration options for the search. Defaults to:
                {
                    "domain": com,
                    "start_page": 1,
                    "pages": 1,
                    "locale": None,
                    "results_language": None,
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
        payload = self._prepare_amazon_bestseller_payload(query, opts)
        response = await self.client.get_resp(payload, config)
        return response

    async def scrape_amazon_sellers(
        self,
        query: str,
        opts: Optional[Dict[str, Any]] = None,
        timeout: Optional[int] = None,
        poll_interval: Optional[int] = None,
    ) -> Dict[str, Any]:
        """
        Scrapes Amazon sellers for a given query.

        Args:
            query (str): 13-character seller ID.
            opts (dict, optional): Configuration options for the search. Defaults to:
                {
                    "domain": com,
                    "start_page": 1,
                    "pages": 1,
                    "locale": None,
                    "results_language": None,
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
        payload = self._prepare_amazon_seller_payload(query, opts)
        response = await self.client.get_resp(payload, config)
        return response
