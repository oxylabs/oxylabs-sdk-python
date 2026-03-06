import unittest
from oxylabs.internal import RealtimeClient


class TestInstacartSearchSync(unittest.TestCase):
    def test_search_source(self):
        client = RealtimeClient('user', 'pass')
        api = client.instacart._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.instacart.scrape_search("milk")

        self.assertEqual(captured["source"], "instacart_search")


class TestInstacartProductSync(unittest.TestCase):
    def test_product_source(self):
        client = RealtimeClient('user', 'pass')
        api = client.instacart._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.instacart.scrape_product("123")

        self.assertEqual(captured["source"], "instacart_product")


class TestInstacartUrlSync(unittest.TestCase):
    def test_url_source(self):
        client = RealtimeClient('user', 'pass')
        api = client.instacart._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.instacart.scrape_url("https://www.instacart.com/")

        self.assertEqual(captured["source"], "instacart")
