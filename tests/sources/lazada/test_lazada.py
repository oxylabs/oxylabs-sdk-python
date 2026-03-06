import unittest
from oxylabs.internal import RealtimeClient


class TestLazadaSearchSync(unittest.TestCase):
    def test_search_source(self):
        client = RealtimeClient('user', 'pass')
        api = client.lazada._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.lazada.scrape_search("dress")

        self.assertEqual(captured["source"], "lazada_search")


class TestLazadaProductSync(unittest.TestCase):
    def test_product_source(self):
        client = RealtimeClient('user', 'pass')
        api = client.lazada._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.lazada.scrape_product("123456")

        self.assertEqual(captured["source"], "lazada_product")


class TestLazadaUrlSync(unittest.TestCase):
    def test_url_source(self):
        client = RealtimeClient('user', 'pass')
        api = client.lazada._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.lazada.scrape_url("https://www.lazada.com/")

        self.assertEqual(captured["source"], "lazada")
