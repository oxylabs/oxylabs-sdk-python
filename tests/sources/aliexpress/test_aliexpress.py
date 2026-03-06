import unittest
from oxylabs.internal import RealtimeClient


class TestAliexpressSearchSync(unittest.TestCase):
    def test_search_source(self):
        client = RealtimeClient('user', 'pass')
        api = client.aliexpress._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.aliexpress.scrape_search("headphones")

        self.assertEqual(captured["source"], "aliexpress_search")


class TestAliexpressProductSync(unittest.TestCase):
    def test_product_source(self):
        client = RealtimeClient('user', 'pass')
        api = client.aliexpress._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.aliexpress.scrape_product("123456")

        self.assertEqual(captured["source"], "aliexpress_product")


class TestAliexpressUrlSync(unittest.TestCase):
    def test_url_source(self):
        client = RealtimeClient('user', 'pass')
        api = client.aliexpress._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.aliexpress.scrape_url("https://www.aliexpress.com/")

        self.assertEqual(captured["source"], "aliexpress")
