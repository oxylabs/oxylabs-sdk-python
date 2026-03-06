import unittest
from oxylabs.internal import RealtimeClient


class TestCdiscountSearchSync(unittest.TestCase):
    def test_search_source(self):
        client = RealtimeClient('user', 'pass')
        api = client.cdiscount._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.cdiscount.scrape_search("tv")

        self.assertEqual(captured["source"], "cdiscount_search")


class TestCdiscountProductSync(unittest.TestCase):
    def test_product_source(self):
        client = RealtimeClient('user', 'pass')
        api = client.cdiscount._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.cdiscount.scrape_product("123456")

        self.assertEqual(captured["source"], "cdiscount_product")


class TestCdiscountUrlSync(unittest.TestCase):
    def test_url_source(self):
        client = RealtimeClient('user', 'pass')
        api = client.cdiscount._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.cdiscount.scrape_url("https://www.cdiscount.com/")

        self.assertEqual(captured["source"], "cdiscount")
