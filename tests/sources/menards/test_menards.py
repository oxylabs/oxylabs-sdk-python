import unittest
from oxylabs.internal import RealtimeClient


class TestMenardsSearchSync(unittest.TestCase):
    def test_search_source(self):
        client = RealtimeClient('user', 'pass')
        api = client.menards._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.menards.scrape_search("lumber")

        self.assertEqual(captured["source"], "menards_search")

    def test_search_filters(self):
        client = RealtimeClient('user', 'pass')
        api = client.menards._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.menards.scrape_search("lumber", in_stock_today=True, pickup_at_store_eligible=True)

        self.assertEqual(captured["in_stock_today"], True)
        self.assertEqual(captured["pickup_at_store_eligible"], True)


class TestMenardsProductSync(unittest.TestCase):
    def test_product_source(self):
        client = RealtimeClient('user', 'pass')
        api = client.menards._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.menards.scrape_product("123", store_id="456")

        self.assertEqual(captured["source"], "menards_product")
        self.assertEqual(captured["store_id"], "456")


class TestMenardsUrlSync(unittest.TestCase):
    def test_url_source(self):
        client = RealtimeClient('user', 'pass')
        api = client.menards._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.menards.scrape_url("https://www.menards.com/")

        self.assertEqual(captured["source"], "menards")
