import unittest
from oxylabs.internal import RealtimeClient


class TestSheinSearchSync(unittest.TestCase):
    """Tests that scrape_search parameters flow through to the payload."""

    def test_search_source(self):
        client = RealtimeClient('user', 'pass')
        api = client.shein._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.shein.scrape_search("dress")

        self.assertEqual(captured["source"], "shein_search")
        self.assertEqual(captured["query"], "dress")

    def test_search_domain(self):
        client = RealtimeClient('user', 'pass')
        api = client.shein._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.shein.scrape_search("dress", domain="com.mx")

        self.assertEqual(captured["domain"], "com.mx")
