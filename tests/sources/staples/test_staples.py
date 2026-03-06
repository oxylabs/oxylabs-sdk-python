import unittest
from oxylabs.internal import RealtimeClient


class TestStaplesSearchSync(unittest.TestCase):
    """Tests that scrape_search parameters flow through to the payload."""

    def test_search_source(self):
        client = RealtimeClient('user', 'pass')
        api = client.staples._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.staples.scrape_search("chair")

        self.assertEqual(captured["source"], "staples_search")
        self.assertEqual(captured["query"], "chair")

    def test_search_domain(self):
        client = RealtimeClient('user', 'pass')
        api = client.staples._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.staples.scrape_search("chair", domain="ca")

        self.assertEqual(captured["domain"], "ca")

    def test_search_start_page(self):
        client = RealtimeClient('user', 'pass')
        api = client.staples._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.staples.scrape_search("chair", start_page=2)

        self.assertEqual(captured["start_page"], 2)
