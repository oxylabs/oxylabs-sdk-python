import unittest
from oxylabs.internal import AsyncClient, RealtimeClient


class TestYoutubeTranscriptSync(unittest.TestCase):
    """Tests that scrape_transcript parameters flow through to the payload."""

    def test_transcript_source(self):
        client = RealtimeClient('user', 'pass')
        api = client.youtube._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.youtube.scrape_transcript("dQw4w9WgXcQ")

        self.assertEqual(captured["source"], "youtube_transcript")
        self.assertEqual(captured["query"], "dQw4w9WgXcQ")

    def test_transcript_context(self):
        client = RealtimeClient('user', 'pass')
        api = client.youtube._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        ctx = [{"key": "language_code", "value": "en"}]
        client.youtube.scrape_transcript("dQw4w9WgXcQ", context=ctx)

        self.assertEqual(captured["context"], ctx)


class TestYoutubeSearchSync(unittest.TestCase):
    """Tests that scrape_search parameters flow through to the payload."""

    def test_search_source(self):
        client = RealtimeClient('user', 'pass')
        api = client.youtube._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.youtube.scrape_search("python tutorial")

        self.assertEqual(captured["source"], "youtube_search")
        self.assertEqual(captured["query"], "python tutorial")

    def test_search_filters(self):
        client = RealtimeClient('user', 'pass')
        api = client.youtube._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.youtube.scrape_search(
            "python tutorial",
            upload_date="this_week",
            type="video",
            duration="4-20",
            sort_by="view_count",
        )

        self.assertEqual(captured["upload_date"], "this_week")
        self.assertEqual(captured["type"], "video")
        self.assertEqual(captured["duration"], "4-20")
        self.assertEqual(captured["sort_by"], "view_count")

    def test_search_boolean_filters(self):
        client = RealtimeClient('user', 'pass')
        api = client.youtube._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.youtube.scrape_search("python", hd=True, filter_4k=True, live=True)

        self.assertEqual(captured["hd"], True)
        self.assertEqual(captured["4k"], True)
        self.assertEqual(captured["live"], True)

    def test_search_numeric_key_filters(self):
        client = RealtimeClient('user', 'pass')
        api = client.youtube._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.youtube.scrape_search("python", filter_360=True, filter_3d=True)

        self.assertEqual(captured["360"], True)
        self.assertEqual(captured["3d"], True)


class TestYoutubeSearchMaxSync(unittest.TestCase):
    """Tests that scrape_search_max uses the correct source."""

    def test_search_max_source(self):
        client = RealtimeClient('user', 'pass')
        api = client.youtube._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.youtube.scrape_search_max("python tutorial")

        self.assertEqual(captured["source"], "youtube_search_max")


class TestYoutubeMetadataSync(unittest.TestCase):
    """Tests that scrape_metadata parameters flow through to the payload."""

    def test_metadata_source_and_parse(self):
        client = RealtimeClient('user', 'pass')
        api = client.youtube._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.youtube.scrape_metadata("dQw4w9WgXcQ")

        self.assertEqual(captured["source"], "youtube_metadata")
        self.assertEqual(captured["parse"], True)


class TestYoutubeChannelSync(unittest.TestCase):
    """Tests that scrape_channel parameters flow through to the payload."""

    def test_channel_source(self):
        client = RealtimeClient('user', 'pass')
        api = client.youtube._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.youtube.scrape_channel("@Oxylabs")

        self.assertEqual(captured["source"], "youtube_channel")
        self.assertEqual(captured["channel_handle"], "@Oxylabs")

    def test_channel_limit(self):
        client = RealtimeClient('user', 'pass')
        api = client.youtube._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.youtube.scrape_channel("@Oxylabs", limit=50)

        self.assertEqual(captured["limit"], 50)


class TestYoutubeSubtitlesSync(unittest.TestCase):
    """Tests that scrape_subtitles parameters flow through to the payload."""

    def test_subtitles_source(self):
        client = RealtimeClient('user', 'pass')
        api = client.youtube._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        ctx = [{"key": "language_code", "value": "en"}]
        client.youtube.scrape_subtitles("dQw4w9WgXcQ", context=ctx)

        self.assertEqual(captured["source"], "youtube_subtitles")
        self.assertEqual(captured["context"], ctx)


class TestYoutubeVideoTrainabilitySync(unittest.TestCase):
    """Tests that scrape_video_trainability parameters flow through to the payload."""

    def test_trainability_source(self):
        client = RealtimeClient('user', 'pass')
        api = client.youtube._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.youtube.scrape_video_trainability("dQw4w9WgXcQ")

        self.assertEqual(captured["source"], "youtube_video_trainability")
        self.assertEqual(captured["video_id"], "dQw4w9WgXcQ")


class TestYoutubeAutocompleteSync(unittest.TestCase):
    """Tests that scrape_autocomplete parameters flow through to the payload."""

    def test_autocomplete_source(self):
        client = RealtimeClient('user', 'pass')
        api = client.youtube._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.youtube.scrape_autocomplete("python")

        self.assertEqual(captured["source"], "youtube_autocomplete")
        self.assertEqual(captured["query"], "python")

    def test_autocomplete_localization(self):
        client = RealtimeClient('user', 'pass')
        api = client.youtube._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.youtube.scrape_autocomplete("python", location="GB", language="en")

        self.assertEqual(captured["location"], "GB")
        self.assertEqual(captured["language"], "en")


class TestYoutubeDownloadAsync(unittest.IsolatedAsyncioTestCase):
    """Tests that scrape_download is only on async and params flow through."""

    async def test_download_source_and_storage(self):
        client = AsyncClient('user', 'pass')
        api = client.youtube._api_instance
        captured = {}
        async def mock_get_resp(payload, config):
            captured.update(payload)
            return {"mock": True}
        api.get_response = mock_get_resp

        await client.youtube.scrape_download(
            "dQw4w9WgXcQ",
            storage_type="s3",
            storage_url="s3://my-bucket/videos/",
        )

        self.assertEqual(captured["source"], "youtube_download")
        self.assertEqual(captured["query"], "dQw4w9WgXcQ")
        self.assertEqual(captured["storage_type"], "s3")
        self.assertEqual(captured["storage_url"], "s3://my-bucket/videos/")

    async def test_download_context(self):
        client = AsyncClient('user', 'pass')
        api = client.youtube._api_instance
        captured = {}
        async def mock_get_resp(payload, config):
            captured.update(payload)
            return {"mock": True}
        api.get_response = mock_get_resp

        ctx = [
            {"key": "download_type", "value": "video"},
            {"key": "video_quality", "value": "1080"},
        ]
        await client.youtube.scrape_download(
            "dQw4w9WgXcQ",
            storage_type="s3",
            storage_url="s3://my-bucket/videos/",
            context=ctx,
        )

        self.assertEqual(captured["context"], ctx)

    def test_download_not_on_sync(self):
        client = RealtimeClient('user', 'pass')
        self.assertFalse(hasattr(client.youtube, 'scrape_download'))
