import unittest
from oxylabs.internal import RealtimeClient


class TestKrogerSearchSync(unittest.TestCase):
    """Tests that scrape_search parameters flow through to the payload."""

    def test_search_source(self):
        client = RealtimeClient('user', 'pass')
        api = client.kroger._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.kroger.scrape_search("milk")

        self.assertEqual(captured["source"], "kroger_search")
        self.assertEqual(captured["query"], "milk")

    def test_search_store_id(self):
        client = RealtimeClient('user', 'pass')
        api = client.kroger._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.kroger.scrape_search("milk", store_id=70100456)

        self.assertEqual(captured["store_id"], 70100456)

    def test_search_context(self):
        client = RealtimeClient('user', 'pass')
        api = client.kroger._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        ctx = [{"key": "price_range", "value": "1.00-5.00"}]
        client.kroger.scrape_search("milk", context=ctx)

        self.assertEqual(captured["context"], ctx)


class TestKrogerProductSync(unittest.TestCase):
    """Tests that scrape_product parameters flow through to the payload."""

    def test_product_source(self):
        client = RealtimeClient('user', 'pass')
        api = client.kroger._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.kroger.scrape_product("0001111041700")

        self.assertEqual(captured["source"], "kroger_product")
        self.assertEqual(captured["product_id"], "0001111041700")


class TestKrogerUrlSync(unittest.TestCase):
    """Tests that scrape_url parameters flow through to the payload."""

    def test_url_source(self):
        client = RealtimeClient('user', 'pass')
        api = client.kroger._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.kroger.scrape_url("https://www.kroger.com/p/milk/0001111041700")

        self.assertEqual(captured["source"], "kroger")
        self.assertEqual(captured["url"], "https://www.kroger.com/p/milk/0001111041700")
