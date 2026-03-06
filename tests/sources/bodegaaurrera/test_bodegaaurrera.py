import unittest
from oxylabs.internal import RealtimeClient


class TestBodegaaurrerapSearchSync(unittest.TestCase):
    def test_search_source(self):
        client = RealtimeClient('user', 'pass')
        api = client.bodegaaurrera._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.bodegaaurrera.scrape_search("arroz")

        self.assertEqual(captured["source"], "bodegaaurrera_search")
        self.assertEqual(captured["query"], "arroz")

    def test_search_subdomain(self):
        client = RealtimeClient('user', 'pass')
        api = client.bodegaaurrera._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.bodegaaurrera.scrape_search("arroz", subdomain="despensa")

        self.assertEqual(captured["subdomain"], "despensa")


class TestBodegaaurreraProductSync(unittest.TestCase):
    def test_product_source(self):
        client = RealtimeClient('user', 'pass')
        api = client.bodegaaurrera._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.bodegaaurrera.scrape_product("123456")

        self.assertEqual(captured["source"], "bodegaaurrera_product")


class TestBodegaaurreraUrlSync(unittest.TestCase):
    def test_url_source(self):
        client = RealtimeClient('user', 'pass')
        api = client.bodegaaurrera._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.bodegaaurrera.scrape_url("https://www.bodegaaurrera.com.mx/")

        self.assertEqual(captured["source"], "bodegaaurrera")
