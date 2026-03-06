from typing import Optional

from oxylabs.internal.api import RealtimeAPI, AsyncAPI
from oxylabs.sources.response import Response
from oxylabs.utils.types import source
from oxylabs.utils.utils import prepare_config


class Youtube:
    def __init__(self, api_instance: RealtimeAPI) -> None:
        """
        Initializes an instance of the Youtube class.

        Args:
            api_instance: An instance of the RealtimeAPI class used for making requests.
        """
        self._api_instance = api_instance

    def scrape_transcript(
        self,
        query: str,
        context: Optional[list] = None,
        callback_url: Optional[str] = None,
        request_timeout: Optional[int] = 165,
        **kwargs
    ) -> Response:
        """
        Scrapes a YouTube video transcript for a given query.

        Args:
            query (str): A YouTube video ID.
            context (Optional[list]): Context parameters (language_code, transcript_origin).
            callback_url (Optional[str]): URL to your callback endpoint.
            request_timeout (int | 165, optional): The interval in seconds for
                            the request to time out if no response is returned.
                            Defaults to 165.

        Returns:
            Response: The response from the server after the job is completed.
        """

        config = prepare_config(request_timeout=request_timeout)
        payload = {
            "source": source.YOUTUBE_TRANSCRIPT,
            "query": query,
            "context": context,
            "callback_url": callback_url,
            **kwargs,
        }
        api_response = self._api_instance.get_response(payload, config)
        return Response(api_response)

    def scrape_search(
        self,
        query: str,
        upload_date: Optional[str] = None,
        type: Optional[str] = None,
        duration: Optional[str] = None,
        sort_by: Optional[str] = None,
        filter_360: Optional[bool] = None,
        filter_3d: Optional[bool] = None,
        filter_4k: Optional[bool] = None,
        creative_commons: Optional[bool] = None,
        hd: Optional[bool] = None,
        hdr: Optional[bool] = None,
        live: Optional[bool] = None,
        location: Optional[bool] = None,
        purchased: Optional[bool] = None,
        subtitles: Optional[bool] = None,
        vr180: Optional[bool] = None,
        callback_url: Optional[str] = None,
        request_timeout: Optional[int] = 165,
        **kwargs
    ) -> Response:
        """
        Scrapes YouTube search results for a given query. Returns up to 20 results.

        Args:
            query (str): The search term.
            upload_date (Optional[str]): Filter by upload date. Accepted values:
                            "today", "last_hour", "this_week", "this_month", "this_year".
            type (Optional[str]): Filter by type. Accepted values:
                            "video", "channel", "playlist", "movie".
            duration (Optional[str]): Filter by duration. Accepted values:
                            "<4", "4-20", ">20".
            sort_by (Optional[str]): Sort results. Accepted values:
                            "rating", "relevance", "view_count", "upload_date".
            filter_360 (Optional[bool]): Returns 360-degree videos.
            filter_3d (Optional[bool]): Returns 3D videos.
            filter_4k (Optional[bool]): Returns 4K videos.
            creative_commons (Optional[bool]): Only Creative Commons licensed videos.
            hd (Optional[bool]): Returns HD videos.
            hdr (Optional[bool]): Returns HDR videos.
            live (Optional[bool]): Returns live streams.
            location (Optional[bool]): Returns videos with location info.
            purchased (Optional[bool]): Returns purchased content.
            subtitles (Optional[bool]): Returns videos with subtitles/CC.
            vr180 (Optional[bool]): Returns VR180 videos.
            callback_url (Optional[str]): URL to your callback endpoint.
            request_timeout (int | 165, optional): The interval in seconds for
                            the request to time out if no response is returned.
                            Defaults to 165.

        Returns:
            Response: The response from the server after the job is completed.
        """

        config = prepare_config(request_timeout=request_timeout)
        payload = {
            "source": source.YOUTUBE_SEARCH,
            "query": query,
            "upload_date": upload_date,
            "type": type,
            "duration": duration,
            "sort_by": sort_by,
            "360": filter_360,
            "3d": filter_3d,
            "4k": filter_4k,
            "creative_commons": creative_commons,
            "hd": hd,
            "hdr": hdr,
            "live": live,
            "location": location,
            "purchased": purchased,
            "subtitles": subtitles,
            "vr180": vr180,
            "callback_url": callback_url,
            **kwargs,
        }
        api_response = self._api_instance.get_response(payload, config)
        return Response(api_response)

    def scrape_search_max(
        self,
        query: str,
        upload_date: Optional[str] = None,
        type: Optional[str] = None,
        duration: Optional[str] = None,
        sort_by: Optional[str] = None,
        filter_360: Optional[bool] = None,
        filter_3d: Optional[bool] = None,
        filter_4k: Optional[bool] = None,
        creative_commons: Optional[bool] = None,
        hd: Optional[bool] = None,
        hdr: Optional[bool] = None,
        live: Optional[bool] = None,
        location: Optional[bool] = None,
        purchased: Optional[bool] = None,
        subtitles: Optional[bool] = None,
        vr180: Optional[bool] = None,
        callback_url: Optional[str] = None,
        request_timeout: Optional[int] = 165,
        **kwargs
    ) -> Response:
        """
        Scrapes YouTube search results for a given query. Returns up to 700 results.

        Args:
            query (str): The search term.
            upload_date (Optional[str]): Filter by upload date. Accepted values:
                            "today", "last_hour", "this_week", "this_month", "this_year".
            type (Optional[str]): Filter by type. Accepted values:
                            "video", "channel", "playlist", "movie".
            duration (Optional[str]): Filter by duration. Accepted values:
                            "<4", "4-20", ">20".
            sort_by (Optional[str]): Sort results. Accepted values:
                            "rating", "relevance", "view_count", "upload_date".
            filter_360 (Optional[bool]): Returns 360-degree videos.
            filter_3d (Optional[bool]): Returns 3D videos.
            filter_4k (Optional[bool]): Returns 4K videos.
            creative_commons (Optional[bool]): Only Creative Commons licensed videos.
            hd (Optional[bool]): Returns HD videos.
            hdr (Optional[bool]): Returns HDR videos.
            live (Optional[bool]): Returns live streams.
            location (Optional[bool]): Returns videos with location info.
            purchased (Optional[bool]): Returns purchased content.
            subtitles (Optional[bool]): Returns videos with subtitles/CC.
            vr180 (Optional[bool]): Returns VR180 videos.
            callback_url (Optional[str]): URL to your callback endpoint.
            request_timeout (int | 165, optional): The interval in seconds for
                            the request to time out if no response is returned.
                            Defaults to 165.

        Returns:
            Response: The response from the server after the job is completed.
        """

        config = prepare_config(request_timeout=request_timeout)
        payload = {
            "source": source.YOUTUBE_SEARCH_MAX,
            "query": query,
            "upload_date": upload_date,
            "type": type,
            "duration": duration,
            "sort_by": sort_by,
            "360": filter_360,
            "3d": filter_3d,
            "4k": filter_4k,
            "creative_commons": creative_commons,
            "hd": hd,
            "hdr": hdr,
            "live": live,
            "location": location,
            "purchased": purchased,
            "subtitles": subtitles,
            "vr180": vr180,
            "callback_url": callback_url,
            **kwargs,
        }
        api_response = self._api_instance.get_response(payload, config)
        return Response(api_response)

    def scrape_metadata(
        self,
        query: str,
        parse: Optional[bool] = True,
        callback_url: Optional[str] = None,
        request_timeout: Optional[int] = 165,
        **kwargs
    ) -> Response:
        """
        Scrapes YouTube video metadata for a given video ID.

        Args:
            query (str): A YouTube video ID.
            parse (Optional[bool]): Returns parsed data. Required for this source,
                            defaults to True.
            callback_url (Optional[str]): URL to your callback endpoint.
            request_timeout (int | 165, optional): The interval in seconds for
                            the request to time out if no response is returned.
                            Defaults to 165.

        Returns:
            Response: The response from the server after the job is completed.
        """

        config = prepare_config(request_timeout=request_timeout)
        payload = {
            "source": source.YOUTUBE_METADATA,
            "query": query,
            "parse": parse,
            "callback_url": callback_url,
            **kwargs,
        }
        api_response = self._api_instance.get_response(payload, config)
        return Response(api_response)

    def scrape_channel(
        self,
        channel_handle: str,
        parse: Optional[bool] = True,
        limit: Optional[int] = None,
        callback_url: Optional[str] = None,
        request_timeout: Optional[int] = 165,
        **kwargs
    ) -> Response:
        """
        Scrapes YouTube channel information for a given channel handle.

        Args:
            channel_handle (str): YouTube channel handle (e.g. "@Oxylabs").
            parse (Optional[bool]): Returns parsed data. Defaults to True.
            limit (Optional[int]): Limits number of videos in the videos array.
                            Defaults to 20.
            callback_url (Optional[str]): URL to your callback endpoint.
            request_timeout (int | 165, optional): The interval in seconds for
                            the request to time out if no response is returned.
                            Defaults to 165.

        Returns:
            Response: The response from the server after the job is completed.
        """

        config = prepare_config(request_timeout=request_timeout)
        payload = {
            "source": source.YOUTUBE_CHANNEL,
            "channel_handle": channel_handle,
            "parse": parse,
            "limit": limit,
            "callback_url": callback_url,
            **kwargs,
        }
        api_response = self._api_instance.get_response(payload, config)
        return Response(api_response)

    def scrape_subtitles(
        self,
        query: str,
        context: Optional[list] = None,
        callback_url: Optional[str] = None,
        request_timeout: Optional[int] = 165,
        **kwargs
    ) -> Response:
        """
        Scrapes YouTube video subtitles for a given video ID.

        Args:
            query (str): A YouTube video ID.
            context (Optional[list]): Context parameters (language_code, subtitle_origin).
            callback_url (Optional[str]): URL to your callback endpoint.
            request_timeout (int | 165, optional): The interval in seconds for
                            the request to time out if no response is returned.
                            Defaults to 165.

        Returns:
            Response: The response from the server after the job is completed.
        """

        config = prepare_config(request_timeout=request_timeout)
        payload = {
            "source": source.YOUTUBE_SUBTITLES,
            "query": query,
            "context": context,
            "callback_url": callback_url,
            **kwargs,
        }
        api_response = self._api_instance.get_response(payload, config)
        return Response(api_response)

    def scrape_video_trainability(
        self,
        video_id: str,
        callback_url: Optional[str] = None,
        request_timeout: Optional[int] = 165,
        **kwargs
    ) -> Response:
        """
        Checks AI training eligibility for a YouTube video.

        Args:
            video_id (str): A YouTube video ID.
            callback_url (Optional[str]): URL to your callback endpoint.
            request_timeout (int | 165, optional): The interval in seconds for
                            the request to time out if no response is returned.
                            Defaults to 165.

        Returns:
            Response: The response from the server after the job is completed.
        """

        config = prepare_config(request_timeout=request_timeout)
        payload = {
            "source": source.YOUTUBE_VIDEO_TRAINABILITY,
            "video_id": video_id,
            "callback_url": callback_url,
            **kwargs,
        }
        api_response = self._api_instance.get_response(payload, config)
        return Response(api_response)

    def scrape_autocomplete(
        self,
        query: str,
        location: Optional[str] = None,
        language: Optional[str] = None,
        callback_url: Optional[str] = None,
        request_timeout: Optional[int] = 165,
        **kwargs
    ) -> Response:
        """
        Scrapes YouTube autocomplete suggestions for a given query.

        Args:
            query (str): The search term for keyword suggestions.
            location (Optional[str]): 2-letter country code. Defaults to "US".
            language (Optional[str]): Language code. Defaults to "en".
            callback_url (Optional[str]): URL to your callback endpoint.
            request_timeout (int | 165, optional): The interval in seconds for
                            the request to time out if no response is returned.
                            Defaults to 165.

        Returns:
            Response: The response from the server after the job is completed.
        """

        config = prepare_config(request_timeout=request_timeout)
        payload = {
            "source": source.YOUTUBE_AUTOCOMPLETE,
            "query": query,
            "location": location,
            "language": language,
            "callback_url": callback_url,
            **kwargs,
        }
        api_response = self._api_instance.get_response(payload, config)
        return Response(api_response)


class YoutubeAsync:
    def __init__(self, api_instance: AsyncAPI) -> None:
        """
        Initializes an instance of the YoutubeAsync class.

        Args:
            api_instance: An instance of the AsyncAPI class used for making requests.
        """
        self._api_instance = api_instance

    async def scrape_transcript(
        self,
        query: str,
        context: Optional[list] = None,
        callback_url: Optional[str] = None,
        request_timeout: Optional[int] = 165,
        job_completion_timeout: Optional[int] = None,
        poll_interval: Optional[int] = None,
        **kwargs
    ) -> Response:
        """
        Asynchronously scrapes a YouTube video transcript for a given query.

        Args:
            query (str): A YouTube video ID.
            context (Optional[list]): Context parameters (language_code, transcript_origin).
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
            "source": source.YOUTUBE_TRANSCRIPT,
            "query": query,
            "context": context,
            "callback_url": callback_url,
            **kwargs,
        }
        api_response = await self._api_instance.get_response(payload, config)
        return Response(api_response)

    async def scrape_search(
        self,
        query: str,
        upload_date: Optional[str] = None,
        type: Optional[str] = None,
        duration: Optional[str] = None,
        sort_by: Optional[str] = None,
        filter_360: Optional[bool] = None,
        filter_3d: Optional[bool] = None,
        filter_4k: Optional[bool] = None,
        creative_commons: Optional[bool] = None,
        hd: Optional[bool] = None,
        hdr: Optional[bool] = None,
        live: Optional[bool] = None,
        location: Optional[bool] = None,
        purchased: Optional[bool] = None,
        subtitles: Optional[bool] = None,
        vr180: Optional[bool] = None,
        callback_url: Optional[str] = None,
        request_timeout: Optional[int] = 165,
        job_completion_timeout: Optional[int] = None,
        poll_interval: Optional[int] = None,
        **kwargs
    ) -> Response:
        """
        Asynchronously scrapes YouTube search results for a given query.
        Returns up to 20 results.

        Args:
            query (str): The search term.
            upload_date (Optional[str]): Filter by upload date. Accepted values:
                            "today", "last_hour", "this_week", "this_month", "this_year".
            type (Optional[str]): Filter by type. Accepted values:
                            "video", "channel", "playlist", "movie".
            duration (Optional[str]): Filter by duration. Accepted values:
                            "<4", "4-20", ">20".
            sort_by (Optional[str]): Sort results. Accepted values:
                            "rating", "relevance", "view_count", "upload_date".
            filter_360 (Optional[bool]): Returns 360-degree videos.
            filter_3d (Optional[bool]): Returns 3D videos.
            filter_4k (Optional[bool]): Returns 4K videos.
            creative_commons (Optional[bool]): Only Creative Commons licensed videos.
            hd (Optional[bool]): Returns HD videos.
            hdr (Optional[bool]): Returns HDR videos.
            live (Optional[bool]): Returns live streams.
            location (Optional[bool]): Returns videos with location info.
            purchased (Optional[bool]): Returns purchased content.
            subtitles (Optional[bool]): Returns videos with subtitles/CC.
            vr180 (Optional[bool]): Returns VR180 videos.
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
            "source": source.YOUTUBE_SEARCH,
            "query": query,
            "upload_date": upload_date,
            "type": type,
            "duration": duration,
            "sort_by": sort_by,
            "360": filter_360,
            "3d": filter_3d,
            "4k": filter_4k,
            "creative_commons": creative_commons,
            "hd": hd,
            "hdr": hdr,
            "live": live,
            "location": location,
            "purchased": purchased,
            "subtitles": subtitles,
            "vr180": vr180,
            "callback_url": callback_url,
            **kwargs,
        }
        api_response = await self._api_instance.get_response(payload, config)
        return Response(api_response)

    async def scrape_search_max(
        self,
        query: str,
        upload_date: Optional[str] = None,
        type: Optional[str] = None,
        duration: Optional[str] = None,
        sort_by: Optional[str] = None,
        filter_360: Optional[bool] = None,
        filter_3d: Optional[bool] = None,
        filter_4k: Optional[bool] = None,
        creative_commons: Optional[bool] = None,
        hd: Optional[bool] = None,
        hdr: Optional[bool] = None,
        live: Optional[bool] = None,
        location: Optional[bool] = None,
        purchased: Optional[bool] = None,
        subtitles: Optional[bool] = None,
        vr180: Optional[bool] = None,
        callback_url: Optional[str] = None,
        request_timeout: Optional[int] = 165,
        job_completion_timeout: Optional[int] = None,
        poll_interval: Optional[int] = None,
        **kwargs
    ) -> Response:
        """
        Asynchronously scrapes YouTube search results for a given query.
        Returns up to 700 results.

        Args:
            query (str): The search term.
            upload_date (Optional[str]): Filter by upload date. Accepted values:
                            "today", "last_hour", "this_week", "this_month", "this_year".
            type (Optional[str]): Filter by type. Accepted values:
                            "video", "channel", "playlist", "movie".
            duration (Optional[str]): Filter by duration. Accepted values:
                            "<4", "4-20", ">20".
            sort_by (Optional[str]): Sort results. Accepted values:
                            "rating", "relevance", "view_count", "upload_date".
            filter_360 (Optional[bool]): Returns 360-degree videos.
            filter_3d (Optional[bool]): Returns 3D videos.
            filter_4k (Optional[bool]): Returns 4K videos.
            creative_commons (Optional[bool]): Only Creative Commons licensed videos.
            hd (Optional[bool]): Returns HD videos.
            hdr (Optional[bool]): Returns HDR videos.
            live (Optional[bool]): Returns live streams.
            location (Optional[bool]): Returns videos with location info.
            purchased (Optional[bool]): Returns purchased content.
            subtitles (Optional[bool]): Returns videos with subtitles/CC.
            vr180 (Optional[bool]): Returns VR180 videos.
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
            "source": source.YOUTUBE_SEARCH_MAX,
            "query": query,
            "upload_date": upload_date,
            "type": type,
            "duration": duration,
            "sort_by": sort_by,
            "360": filter_360,
            "3d": filter_3d,
            "4k": filter_4k,
            "creative_commons": creative_commons,
            "hd": hd,
            "hdr": hdr,
            "live": live,
            "location": location,
            "purchased": purchased,
            "subtitles": subtitles,
            "vr180": vr180,
            "callback_url": callback_url,
            **kwargs,
        }
        api_response = await self._api_instance.get_response(payload, config)
        return Response(api_response)

    async def scrape_metadata(
        self,
        query: str,
        parse: Optional[bool] = True,
        callback_url: Optional[str] = None,
        request_timeout: Optional[int] = 165,
        job_completion_timeout: Optional[int] = None,
        poll_interval: Optional[int] = None,
        **kwargs
    ) -> Response:
        """
        Asynchronously scrapes YouTube video metadata for a given video ID.

        Args:
            query (str): A YouTube video ID.
            parse (Optional[bool]): Returns parsed data. Required for this source,
                            defaults to True.
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
            "source": source.YOUTUBE_METADATA,
            "query": query,
            "parse": parse,
            "callback_url": callback_url,
            **kwargs,
        }
        api_response = await self._api_instance.get_response(payload, config)
        return Response(api_response)

    async def scrape_channel(
        self,
        channel_handle: str,
        parse: Optional[bool] = True,
        limit: Optional[int] = None,
        callback_url: Optional[str] = None,
        request_timeout: Optional[int] = 165,
        job_completion_timeout: Optional[int] = None,
        poll_interval: Optional[int] = None,
        **kwargs
    ) -> Response:
        """
        Asynchronously scrapes YouTube channel information for a given channel handle.

        Args:
            channel_handle (str): YouTube channel handle (e.g. "@Oxylabs").
            parse (Optional[bool]): Returns parsed data. Defaults to True.
            limit (Optional[int]): Limits number of videos in the videos array.
                            Defaults to 20.
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
            "source": source.YOUTUBE_CHANNEL,
            "channel_handle": channel_handle,
            "parse": parse,
            "limit": limit,
            "callback_url": callback_url,
            **kwargs,
        }
        api_response = await self._api_instance.get_response(payload, config)
        return Response(api_response)

    async def scrape_subtitles(
        self,
        query: str,
        context: Optional[list] = None,
        callback_url: Optional[str] = None,
        request_timeout: Optional[int] = 165,
        job_completion_timeout: Optional[int] = None,
        poll_interval: Optional[int] = None,
        **kwargs
    ) -> Response:
        """
        Asynchronously scrapes YouTube video subtitles for a given video ID.

        Args:
            query (str): A YouTube video ID.
            context (Optional[list]): Context parameters (language_code, subtitle_origin).
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
            "source": source.YOUTUBE_SUBTITLES,
            "query": query,
            "context": context,
            "callback_url": callback_url,
            **kwargs,
        }
        api_response = await self._api_instance.get_response(payload, config)
        return Response(api_response)

    async def scrape_video_trainability(
        self,
        video_id: str,
        callback_url: Optional[str] = None,
        request_timeout: Optional[int] = 165,
        job_completion_timeout: Optional[int] = None,
        poll_interval: Optional[int] = None,
        **kwargs
    ) -> Response:
        """
        Asynchronously checks AI training eligibility for a YouTube video.

        Args:
            video_id (str): A YouTube video ID.
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
            "source": source.YOUTUBE_VIDEO_TRAINABILITY,
            "video_id": video_id,
            "callback_url": callback_url,
            **kwargs,
        }
        api_response = await self._api_instance.get_response(payload, config)
        return Response(api_response)

    async def scrape_download(
        self,
        query: str,
        storage_type: str,
        storage_url: str,
        context: Optional[list] = None,
        callback_url: Optional[str] = None,
        request_timeout: Optional[int] = 165,
        job_completion_timeout: Optional[int] = None,
        poll_interval: Optional[int] = None,
        **kwargs
    ) -> Response:
        """
        Asynchronously downloads YouTube video/audio content to cloud storage.

        This method is only available via Push-Pull (async) integration.

        Args:
            query (str): A YouTube video ID.
            storage_type (str): Cloud storage type. Accepted values:
                            "gcs", "s3", "s3_compatible".
            storage_url (str): Bucket name (AWS S3) or URL (other S3-compatible storage).
            context (Optional[list]): Context parameters (download_type, video_quality).
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
            "source": source.YOUTUBE_DOWNLOAD,
            "query": query,
            "storage_type": storage_type,
            "storage_url": storage_url,
            "context": context,
            "callback_url": callback_url,
            **kwargs,
        }
        api_response = await self._api_instance.get_response(payload, config)
        return Response(api_response)

    async def scrape_autocomplete(
        self,
        query: str,
        location: Optional[str] = None,
        language: Optional[str] = None,
        callback_url: Optional[str] = None,
        request_timeout: Optional[int] = 165,
        job_completion_timeout: Optional[int] = None,
        poll_interval: Optional[int] = None,
        **kwargs
    ) -> Response:
        """
        Asynchronously scrapes YouTube autocomplete suggestions for a given query.

        Args:
            query (str): The search term for keyword suggestions.
            location (Optional[str]): 2-letter country code. Defaults to "US".
            language (Optional[str]): Language code. Defaults to "en".
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
            "source": source.YOUTUBE_AUTOCOMPLETE,
            "query": query,
            "location": location,
            "language": language,
            "callback_url": callback_url,
            **kwargs,
        }
        api_response = await self._api_instance.get_response(payload, config)
        return Response(api_response)
