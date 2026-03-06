import unittest
from oxylabs.internal import RealtimeClient


class TestDcardSearchSync(unittest.TestCase):
    """Tests that scrape_search parameters flow through to the payload."""

    def test_search_source(self):
        client = RealtimeClient('user', 'pass')
        api = client.dcard._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.dcard.scrape_search("tv")

        self.assertEqual(captured["source"], "dcard_search")
        self.assertEqual(captured["query"], "tv")

    def test_search_render(self):
        client = RealtimeClient('user', 'pass')
        api = client.dcard._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.dcard.scrape_search("tv", render="html")

        self.assertEqual(captured["render"], "html")
