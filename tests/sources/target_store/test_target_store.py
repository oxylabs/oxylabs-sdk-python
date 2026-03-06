import unittest
from oxylabs.internal import RealtimeClient


class TestTargetStoreSearchSync(unittest.TestCase):
    def test_search_source(self):
        client = RealtimeClient('user', 'pass')
        api = client.target_store._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.target_store.scrape_search("towels")

        self.assertEqual(captured["source"], "target_search")

    def test_search_fulfillment(self):
        client = RealtimeClient('user', 'pass')
        api = client.target_store._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.target_store.scrape_search("towels", store_id=123, fulfillment_type="pickup")

        self.assertEqual(captured["store_id"], 123)
        self.assertEqual(captured["fulfillment_type"], "pickup")


class TestTargetStoreProductSync(unittest.TestCase):
    def test_product_source(self):
        client = RealtimeClient('user', 'pass')
        api = client.target_store._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.target_store.scrape_product("A-12345678")

        self.assertEqual(captured["source"], "target_product")
        self.assertEqual(captured["product_id"], "A-12345678")


class TestTargetStoreCategorySync(unittest.TestCase):
    def test_category_source(self):
        client = RealtimeClient('user', 'pass')
        api = client.target_store._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.target_store.scrape_category("owq2q")

        self.assertEqual(captured["source"], "target_category")
        self.assertEqual(captured["category_id"], "owq2q")


class TestTargetStoreUrlSync(unittest.TestCase):
    def test_url_source(self):
        client = RealtimeClient('user', 'pass')
        api = client.target_store._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.target_store.scrape_url("https://www.target.com/")

        self.assertEqual(captured["source"], "target")
