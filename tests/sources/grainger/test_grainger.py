import unittest
from oxylabs.internal import RealtimeClient


class TestGraingerSearchSync(unittest.TestCase):
    def test_search_source(self):
        client = RealtimeClient('user', 'pass')
        api = client.grainger._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.grainger.scrape_search("screws")

        self.assertEqual(captured["source"], "grainger_search")

    def test_search_domain(self):
        client = RealtimeClient('user', 'pass')
        api = client.grainger._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.grainger.scrape_search("screws", domain="com.mx")

        self.assertEqual(captured["domain"], "com.mx")


class TestGraingerProductSync(unittest.TestCase):
    def test_product_source(self):
        client = RealtimeClient('user', 'pass')
        api = client.grainger._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.grainger.scrape_product("123456")

        self.assertEqual(captured["source"], "grainger_product")


class TestGraingerUrlSync(unittest.TestCase):
    def test_url_source(self):
        client = RealtimeClient('user', 'pass')
        api = client.grainger._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.grainger.scrape_url("https://www.grainger.com/")

        self.assertEqual(captured["source"], "grainger")
