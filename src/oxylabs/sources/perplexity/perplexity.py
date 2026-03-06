from typing import Optional

from oxylabs.internal.api import RealtimeAPI, AsyncAPI
from oxylabs.sources.response import Response
from oxylabs.utils.types import source
from oxylabs.utils.utils import prepare_config


class Perplexity:
    def __init__(self, api_instance: RealtimeAPI) -> None:
        """
        Initializes an instance of the Perplexity class.

        Args:
            api_instance: An instance of the RealtimeAPI class used for making requests.
        """
        self._api_instance = api_instance

    def scrape(
        self,
        prompt: str,
        geo_location: Optional[str] = None,
        parse: Optional[bool] = None,
        callback_url: Optional[str] = None,
        request_timeout: Optional[int] = 165,
        **kwargs
    ) -> Response:
        """
        Scrapes Perplexity responses for a given prompt.

        Args:
            prompt (str): The prompt or question to submit to Perplexity.
            geo_location (Optional[str]): Specify a country to send the prompt from.
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
            "source": source.PERPLEXITY,
            "prompt": prompt,
            "geo_location": geo_location,
            "parse": parse,
            "callback_url": callback_url,
            **kwargs,
        }
        api_response = self._api_instance.get_response(payload, config)
        return Response(api_response)


class PerplexityAsync:
    def __init__(self, api_instance: AsyncAPI) -> None:
        """
        Initializes an instance of the PerplexityAsync class.

        Args:
            api_instance: An instance of the AsyncAPI class used for making requests.
        """
        self._api_instance = api_instance

    async def scrape(
        self,
        prompt: str,
        geo_location: Optional[str] = None,
        parse: Optional[bool] = None,
        callback_url: Optional[str] = None,
        request_timeout: Optional[int] = 165,
        job_completion_timeout: Optional[int] = None,
        poll_interval: Optional[int] = None,
        **kwargs
    ) -> Response:
        """
        Asynchronously scrapes Perplexity responses for a given prompt.

        Args:
            prompt (str): The prompt or question to submit to Perplexity.
            geo_location (Optional[str]): Specify a country to send the prompt from.
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
            "source": source.PERPLEXITY,
            "prompt": prompt,
            "geo_location": geo_location,
            "parse": parse,
            "callback_url": callback_url,
            **kwargs,
        }
        api_response = await self._api_instance.get_response(payload, config)
        return Response(api_response)
