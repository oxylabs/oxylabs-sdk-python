import unittest
from oxylabs.internal import RealtimeClient


class TestMercadolivreSearchSync(unittest.TestCase):
    def test_search_source(self):
        client = RealtimeClient('user', 'pass')
        api = client.mercadolivre._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.mercadolivre.scrape_search("celular")

        self.assertEqual(captured["source"], "mercadolivre_search")


class TestMercadolivreProductSync(unittest.TestCase):
    def test_product_source(self):
        client = RealtimeClient('user', 'pass')
        api = client.mercadolivre._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.mercadolivre.scrape_product("MLB123456")

        self.assertEqual(captured["source"], "mercadolivre_product")
