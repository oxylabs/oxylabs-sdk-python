import unittest
from oxylabs.internal import RealtimeClient


class TestCostcoSearchSync(unittest.TestCase):
    def test_search_source(self):
        client = RealtimeClient('user', 'pass')
        api = client.costco._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.costco.scrape_search("milk")

        self.assertEqual(captured["source"], "costco_search")

    def test_search_domain(self):
        client = RealtimeClient('user', 'pass')
        api = client.costco._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.costco.scrape_search("milk", domain="ca")

        self.assertEqual(captured["domain"], "ca")


class TestCostcoProductSync(unittest.TestCase):
    def test_product_source(self):
        client = RealtimeClient('user', 'pass')
        api = client.costco._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.costco.scrape_product("123456")

        self.assertEqual(captured["source"], "costco_product")


class TestCostcoUrlSync(unittest.TestCase):
    def test_url_source(self):
        client = RealtimeClient('user', 'pass')
        api = client.costco._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.costco.scrape_url("https://www.costco.com/")

        self.assertEqual(captured["source"], "costco")
