import unittest
from oxylabs.internal import RealtimeClient


class TestMagazineluizaSearchSync(unittest.TestCase):
    def test_search_source(self):
        client = RealtimeClient('user', 'pass')
        api = client.magazineluiza._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.magazineluiza.scrape_search("telefone")

        self.assertEqual(captured["source"], "magazineluiza_search")


class TestMagazineluizaProductSync(unittest.TestCase):
    def test_product_source(self):
        client = RealtimeClient('user', 'pass')
        api = client.magazineluiza._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.magazineluiza.scrape_product("123456")

        self.assertEqual(captured["source"], "magazineluiza_product")


class TestMagazineluizaUrlSync(unittest.TestCase):
    def test_url_source(self):
        client = RealtimeClient('user', 'pass')
        api = client.magazineluiza._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.magazineluiza.scrape_url("https://www.magazineluiza.com.br/")

        self.assertEqual(captured["source"], "magazineluiza")
