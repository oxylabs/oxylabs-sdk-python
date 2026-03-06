import unittest
from oxylabs.internal import RealtimeClient


class TestRakutenSearchSync(unittest.TestCase):
    def test_search_source(self):
        client = RealtimeClient('user', 'pass')
        api = client.rakuten._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.rakuten.scrape_search("shoes")

        self.assertEqual(captured["source"], "rakuten_search")


class TestRakutenUrlSync(unittest.TestCase):
    def test_url_source(self):
        client = RealtimeClient('user', 'pass')
        api = client.rakuten._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.rakuten.scrape_url("https://www.rakuten.com.tw/")

        self.assertEqual(captured["source"], "rakuten")
