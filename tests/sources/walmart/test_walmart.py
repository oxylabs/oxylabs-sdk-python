import unittest
from oxylabs.internal import RealtimeClient


class TestWalmartSearchSync(unittest.TestCase):
    """Tests that scrape_search parameters flow through to the payload."""

    def test_search_source(self):
        client = RealtimeClient('user', 'pass')
        api = client.walmart._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.walmart.scrape_search("laptop")

        self.assertEqual(captured["source"], "walmart_search")
        self.assertEqual(captured["query"], "laptop")

    def test_search_filters(self):
        client = RealtimeClient('user', 'pass')
        api = client.walmart._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.walmart.scrape_search("laptop", min_price=100.0, max_price=500.0, sort_by="price_low")

        self.assertEqual(captured["min_price"], 100.0)
        self.assertEqual(captured["max_price"], 500.0)
        self.assertEqual(captured["sort_by"], "price_low")

    def test_search_fulfillment(self):
        client = RealtimeClient('user', 'pass')
        api = client.walmart._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.walmart.scrape_search("laptop", delivery_zip="10001", fulfillment_speed="2_days")

        self.assertEqual(captured["delivery_zip"], "10001")
        self.assertEqual(captured["fulfillment_speed"], "2_days")


class TestWalmartProductSync(unittest.TestCase):
    """Tests that scrape_product parameters flow through to the payload."""

    def test_product_source(self):
        client = RealtimeClient('user', 'pass')
        api = client.walmart._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.walmart.scrape_product("123456789")

        self.assertEqual(captured["source"], "walmart_product")
        self.assertEqual(captured["product_id"], "123456789")

    def test_product_store(self):
        client = RealtimeClient('user', 'pass')
        api = client.walmart._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.walmart.scrape_product("123456789", store_id="1234")

        self.assertEqual(captured["store_id"], "1234")


class TestWalmartUrlSync(unittest.TestCase):
    """Tests that scrape_url parameters flow through to the payload."""

    def test_url_source(self):
        client = RealtimeClient('user', 'pass')
        api = client.walmart._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.walmart.scrape_url("https://www.walmart.com/ip/123456789")

        self.assertEqual(captured["source"], "walmart")
        self.assertEqual(captured["url"], "https://www.walmart.com/ip/123456789")

    def test_url_parse(self):
        client = RealtimeClient('user', 'pass')
        api = client.walmart._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.walmart.scrape_url("https://www.walmart.com/ip/123456789", parse=True)

        self.assertEqual(captured["parse"], True)
