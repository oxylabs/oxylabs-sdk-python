import unittest
from oxylabs.internal import RealtimeClient


class TestMercadolibreSearchSync(unittest.TestCase):
    def test_search_source(self):
        client = RealtimeClient('user', 'pass')
        api = client.mercadolibre._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.mercadolibre.scrape_search("iphone")

        self.assertEqual(captured["source"], "mercadolibre_search")


class TestMercadolibreProductSync(unittest.TestCase):
    def test_product_source(self):
        client = RealtimeClient('user', 'pass')
        api = client.mercadolibre._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.mercadolibre.scrape_product("MLA123456")

        self.assertEqual(captured["source"], "mercadolibre_product")


class TestMercadolibreUrlSync(unittest.TestCase):
    def test_url_source(self):
        client = RealtimeClient('user', 'pass')
        api = client.mercadolibre._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.mercadolibre.scrape_url("https://www.mercadolibre.com/")

        self.assertEqual(captured["source"], "mercadolibre")
