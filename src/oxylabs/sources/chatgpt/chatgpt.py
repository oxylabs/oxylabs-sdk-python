from typing import Optional

from oxylabs.internal.api import RealtimeAPI, AsyncAPI
from oxylabs.sources.response import Response
from oxylabs.utils.types import source
from oxylabs.utils.utils import prepare_config


class Chatgpt:
    def __init__(self, api_instance: RealtimeAPI) -> None:
        """
        Initializes an instance of the Chatgpt class.

        Args:
            api_instance: An instance of the RealtimeAPI class used for making requests.
        """
        self._api_instance = api_instance

    def scrape(
        self,
        prompt: str,
        search: Optional[bool] = None,
        geo_location: Optional[str] = None,
        render: Optional[str] = None,
        parse: Optional[bool] = None,
        callback_url: Optional[str] = None,
        request_timeout: Optional[int] = 165,
        **kwargs
    ) -> Response:
        """
        Scrapes ChatGPT conversational responses for a given prompt.

        Args:
            prompt (str): The prompt or question to submit to ChatGPT.
                            Must be less than 4000 symbols.
            search (Optional[bool]): Triggers ChatGPT to perform a Web Search
                            for the prompt. Defaults to true.
            geo_location (Optional[str]): Specify a country to send the prompt from.
            render (Optional[str]): JavaScript rendering is enforced by default for chatgpt.
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
            "source": source.CHATGPT,
            "prompt": prompt,
            "search": search,
            "geo_location": geo_location,
            "render": render,
            "parse": parse,
            "callback_url": callback_url,
            **kwargs,
        }
        api_response = self._api_instance.get_response(payload, config)
        return Response(api_response)


class ChatgptAsync:
    def __init__(self, api_instance: AsyncAPI) -> None:
        """
        Initializes an instance of the ChatgptAsync class.

        Args:
            api_instance: An instance of the AsyncAPI class used for making requests.
        """
        self._api_instance = api_instance

    async def scrape(
        self,
        prompt: str,
        search: Optional[bool] = None,
        geo_location: Optional[str] = None,
        render: Optional[str] = None,
        parse: Optional[bool] = None,
        callback_url: Optional[str] = None,
        request_timeout: Optional[int] = 165,
        job_completion_timeout: Optional[int] = None,
        poll_interval: Optional[int] = None,
        **kwargs
    ) -> Response:
        """
        Asynchronously scrapes ChatGPT conversational responses for a given prompt.

        Args:
            prompt (str): The prompt or question to submit to ChatGPT.
                            Must be less than 4000 symbols.
            search (Optional[bool]): Triggers ChatGPT to perform a Web Search
                            for the prompt. Defaults to true.
            geo_location (Optional[str]): Specify a country to send the prompt from.
            render (Optional[str]): JavaScript rendering is enforced by default for chatgpt.
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
            "source": source.CHATGPT,
            "prompt": prompt,
            "search": search,
            "geo_location": geo_location,
            "render": render,
            "parse": parse,
            "callback_url": callback_url,
            **kwargs,
        }
        api_response = await self._api_instance.get_response(payload, config)
        return Response(api_response)
