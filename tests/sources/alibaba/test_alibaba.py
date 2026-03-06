import unittest
from oxylabs.internal import RealtimeClient


class TestAlibabaSearchSync(unittest.TestCase):
    def test_search_source(self):
        client = RealtimeClient('user', 'pass')
        api = client.alibaba._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.alibaba.scrape_search("electronics")

        self.assertEqual(captured["source"], "alibaba_search")

    def test_search_start_page(self):
        client = RealtimeClient('user', 'pass')
        api = client.alibaba._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.alibaba.scrape_search("electronics", start_page=2)

        self.assertEqual(captured["start_page"], 2)


class TestAlibabaProductSync(unittest.TestCase):
    def test_product_source(self):
        client = RealtimeClient('user', 'pass')
        api = client.alibaba._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.alibaba.scrape_product("1234567890123")

        self.assertEqual(captured["source"], "alibaba_product")


class TestAlibabaUrlSync(unittest.TestCase):
    def test_url_source(self):
        client = RealtimeClient('user', 'pass')
        api = client.alibaba._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.alibaba.scrape_url("https://www.alibaba.com/")

        self.assertEqual(captured["source"], "alibaba")
