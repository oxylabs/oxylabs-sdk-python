import unittest
from oxylabs.internal import RealtimeClient


class TestAvnetSearchSync(unittest.TestCase):
    """Tests that scrape_search parameters flow through to the payload."""

    def test_search_source(self):
        client = RealtimeClient('user', 'pass')
        api = client.avnet._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.avnet.scrape_search("case")

        self.assertEqual(captured["source"], "avnet_search")
        self.assertEqual(captured["query"], "case")

    def test_search_start_page(self):
        client = RealtimeClient('user', 'pass')
        api = client.avnet._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.avnet.scrape_search("case", start_page=3)

        self.assertEqual(captured["start_page"], 3)
