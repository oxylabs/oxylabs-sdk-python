import unittest
from oxylabs.internal import RealtimeClient


class TestFlipkartSearchSync(unittest.TestCase):
    def test_search_source(self):
        client = RealtimeClient('user', 'pass')
        api = client.flipkart._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.flipkart.scrape_search("phone")

        self.assertEqual(captured["source"], "flipkart_search")


class TestFlipkartProductSync(unittest.TestCase):
    def test_product_source(self):
        client = RealtimeClient('user', 'pass')
        api = client.flipkart._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.flipkart.scrape_product("123456")

        self.assertEqual(captured["source"], "flipkart_product")


class TestFlipkartUrlSync(unittest.TestCase):
    def test_url_source(self):
        client = RealtimeClient('user', 'pass')
        api = client.flipkart._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.flipkart.scrape_url("https://www.flipkart.com/")

        self.assertEqual(captured["source"], "flipkart")
