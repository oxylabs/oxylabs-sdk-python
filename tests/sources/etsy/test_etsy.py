import unittest
from oxylabs.internal import RealtimeClient


class TestEtsySearchSync(unittest.TestCase):
    """Tests that scrape_search parameters flow through to the payload."""

    def test_search_source(self):
        client = RealtimeClient('user', 'pass')
        api = client.etsy._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.etsy.scrape_search("handmade jewelry")

        self.assertEqual(captured["source"], "etsy_search")
        self.assertEqual(captured["query"], "handmade jewelry")

    def test_search_store_id(self):
        client = RealtimeClient('user', 'pass')
        api = client.etsy._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.etsy.scrape_search("jewelry", store_id=12345)

        self.assertEqual(captured["store_id"], 12345)


class TestEtsyProductSync(unittest.TestCase):
    """Tests that scrape_product parameters flow through to the payload."""

    def test_product_source(self):
        client = RealtimeClient('user', 'pass')
        api = client.etsy._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.etsy.scrape_product("1234567890")

        self.assertEqual(captured["source"], "etsy_product")
        self.assertEqual(captured["product_id"], "1234567890")

    def test_product_parse(self):
        client = RealtimeClient('user', 'pass')
        api = client.etsy._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.etsy.scrape_product("1234567890", parse=True)

        self.assertEqual(captured["parse"], True)


class TestEtsyUrlSync(unittest.TestCase):
    """Tests that scrape_url parameters flow through to the payload."""

    def test_url_source(self):
        client = RealtimeClient('user', 'pass')
        api = client.etsy._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.etsy.scrape_url("https://www.etsy.com/listing/123456")

        self.assertEqual(captured["source"], "etsy")
        self.assertEqual(captured["url"], "https://www.etsy.com/listing/123456")
