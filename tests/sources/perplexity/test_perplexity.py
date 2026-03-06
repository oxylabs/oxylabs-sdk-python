import unittest
from oxylabs.internal import RealtimeClient


class TestPerplexitySync(unittest.TestCase):
    """Tests that scrape parameters flow through to the payload."""

    def test_scrape_source(self):
        client = RealtimeClient('user', 'pass')
        api = client.perplexity._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.perplexity.scrape("top 3 smartphones in 2025")

        self.assertEqual(captured["source"], "perplexity")
        self.assertEqual(captured["prompt"], "top 3 smartphones in 2025")

    def test_scrape_geo_location(self):
        client = RealtimeClient('user', 'pass')
        api = client.perplexity._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.perplexity.scrape("smartphones", geo_location="United States")

        self.assertEqual(captured["geo_location"], "United States")

    def test_scrape_parse(self):
        client = RealtimeClient('user', 'pass')
        api = client.perplexity._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.perplexity.scrape("smartphones", parse=True)

        self.assertEqual(captured["parse"], True)
