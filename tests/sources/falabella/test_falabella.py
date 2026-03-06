import unittest
from oxylabs.internal import RealtimeClient


class TestFalabellaSearchSync(unittest.TestCase):
    def test_search_source(self):
        client = RealtimeClient('user', 'pass')
        api = client.falabella._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.falabella.scrape_search("zapatos")

        self.assertEqual(captured["source"], "falabella_search")


class TestFalabellaProductSync(unittest.TestCase):
    def test_product_source(self):
        client = RealtimeClient('user', 'pass')
        api = client.falabella._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.falabella.scrape_product("123456")

        self.assertEqual(captured["source"], "falabella_product")


class TestFalabellaUrlSync(unittest.TestCase):
    def test_url_source(self):
        client = RealtimeClient('user', 'pass')
        api = client.falabella._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.falabella.scrape_url("https://www.falabella.com/")

        self.assertEqual(captured["source"], "falabella")
