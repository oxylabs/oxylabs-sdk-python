import unittest
from oxylabs.internal import RealtimeClient


class TestBestbuySearchSync(unittest.TestCase):
    """Tests that scrape_search parameters flow through to the payload."""

    def test_search_source(self):
        client = RealtimeClient('user', 'pass')
        api = client.bestbuy._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.bestbuy.scrape_search("laptop")

        self.assertEqual(captured["source"], "bestbuy_search")
        self.assertEqual(captured["query"], "laptop")

    def test_search_fulfillment(self):
        client = RealtimeClient('user', 'pass')
        api = client.bestbuy._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.bestbuy.scrape_search("laptop", store_id=123, fulfillment_type="pickup")

        self.assertEqual(captured["store_id"], 123)
        self.assertEqual(captured["fulfillment_type"], "pickup")


class TestBestbuyProductSync(unittest.TestCase):
    """Tests that scrape_product parameters flow through to the payload."""

    def test_product_source(self):
        client = RealtimeClient('user', 'pass')
        api = client.bestbuy._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.bestbuy.scrape_product("6525410")

        self.assertEqual(captured["source"], "bestbuy_product")
        self.assertEqual(captured["product_id"], "6525410")

    def test_product_parse(self):
        client = RealtimeClient('user', 'pass')
        api = client.bestbuy._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.bestbuy.scrape_product("6525410", parse=True)

        self.assertEqual(captured["parse"], True)
