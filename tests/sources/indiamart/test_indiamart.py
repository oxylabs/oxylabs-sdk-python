import unittest
from oxylabs.internal import RealtimeClient


class TestIndiamartSearchSync(unittest.TestCase):
    def test_search_source(self):
        client = RealtimeClient('user', 'pass')
        api = client.indiamart._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.indiamart.scrape_search("machinery")

        self.assertEqual(captured["source"], "indiamart_search")


class TestIndiamartProductSync(unittest.TestCase):
    def test_product_source(self):
        client = RealtimeClient('user', 'pass')
        api = client.indiamart._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.indiamart.scrape_product("123456")

        self.assertEqual(captured["source"], "indiamart_product")


class TestIndiamartUrlSync(unittest.TestCase):
    def test_url_source(self):
        client = RealtimeClient('user', 'pass')
        api = client.indiamart._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.indiamart.scrape_url("https://www.indiamart.com/")

        self.assertEqual(captured["source"], "indiamart")
