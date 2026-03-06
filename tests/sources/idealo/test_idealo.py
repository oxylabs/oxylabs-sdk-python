import unittest
from oxylabs.internal import RealtimeClient


class TestIdealoSearchSync(unittest.TestCase):
    def test_search_source(self):
        client = RealtimeClient('user', 'pass')
        api = client.idealo._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.idealo.scrape_search("iphone")

        self.assertEqual(captured["source"], "idealo_search")
        self.assertEqual(captured["query"], "iphone")
