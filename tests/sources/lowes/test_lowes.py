import unittest
from oxylabs.internal import RealtimeClient


class TestLowesSearchSync(unittest.TestCase):
    def test_search_source(self):
        client = RealtimeClient('user', 'pass')
        api = client.lowes._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.lowes.scrape_search("hammer")

        self.assertEqual(captured["source"], "lowes_search")

    def test_search_filters(self):
        client = RealtimeClient('user', 'pass')
        api = client.lowes._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.lowes.scrape_search("hammer", store_id=123, free_delivery=True, pickup_today=True)

        self.assertEqual(captured["store_id"], 123)
        self.assertEqual(captured["free_delivery"], True)
        self.assertEqual(captured["pickup_today"], True)


class TestLowesProductSync(unittest.TestCase):
    def test_product_source(self):
        client = RealtimeClient('user', 'pass')
        api = client.lowes._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.lowes.scrape_product("123")

        self.assertEqual(captured["source"], "lowes_product")


class TestLowesUrlSync(unittest.TestCase):
    def test_url_source(self):
        client = RealtimeClient('user', 'pass')
        api = client.lowes._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.lowes.scrape_url("https://www.lowes.com/")

        self.assertEqual(captured["source"], "lowes")
