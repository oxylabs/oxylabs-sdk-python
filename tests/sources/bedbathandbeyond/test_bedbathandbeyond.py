import unittest
from oxylabs.internal import RealtimeClient


class TestBedbathandbeyondSearchSync(unittest.TestCase):
    def test_search_source(self):
        client = RealtimeClient('user', 'pass')
        api = client.bedbathandbeyond._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.bedbathandbeyond.scrape_search("table")

        self.assertEqual(captured["source"], "bedbathandbeyond_search")
        self.assertEqual(captured["query"], "table")


class TestBedbathandbeyondProductSync(unittest.TestCase):
    def test_product_source(self):
        client = RealtimeClient('user', 'pass')
        api = client.bedbathandbeyond._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.bedbathandbeyond.scrape_product("12345678")

        self.assertEqual(captured["source"], "bedbathandbeyond_product")
        self.assertEqual(captured["product_id"], "12345678")


class TestBedbathandbeyondUrlSync(unittest.TestCase):
    def test_url_source(self):
        client = RealtimeClient('user', 'pass')
        api = client.bedbathandbeyond._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.bedbathandbeyond.scrape_url("https://www.bedbathandbeyond.com/store/product/123")

        self.assertEqual(captured["source"], "bedbathandbeyond")
        self.assertEqual(captured["url"], "https://www.bedbathandbeyond.com/store/product/123")
