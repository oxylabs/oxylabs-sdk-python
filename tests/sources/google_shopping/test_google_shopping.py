import unittest
from oxylabs.internal import RealtimeClient


class TestGoogleShoppingSearchSync(unittest.TestCase):
    """Tests that scrape_shopping_search parameters flow through to the payload."""

    def test_shopping_search_source(self):
        client = RealtimeClient('user', 'pass')
        api = client.google_shopping._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.google_shopping.scrape_shopping_search("laptop")

        self.assertEqual(captured["source"], "google_shopping_search")
        self.assertEqual(captured["query"], "laptop")

    def test_shopping_search_pagination(self):
        client = RealtimeClient('user', 'pass')
        api = client.google_shopping._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.google_shopping.scrape_shopping_search("laptop", start_page=2, pages=3)

        self.assertEqual(captured["start_page"], 2)
        self.assertEqual(captured["pages"], 3)

    def test_shopping_search_locale(self):
        client = RealtimeClient('user', 'pass')
        api = client.google_shopping._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.google_shopping.scrape_shopping_search("laptop", locale="en")

        self.assertEqual(captured["locale"], "en")


class TestGoogleShoppingUrlSync(unittest.TestCase):
    """Tests that scrape_shopping_url parameters flow through to the payload."""

    def test_shopping_url_source(self):
        client = RealtimeClient('user', 'pass')
        api = client.google_shopping._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.google_shopping.scrape_shopping_url("https://shopping.google.com/search?q=laptop")

        self.assertEqual(captured["source"], "google_shopping")
        self.assertEqual(captured["url"], "https://shopping.google.com/search?q=laptop")

    def test_shopping_url_render(self):
        client = RealtimeClient('user', 'pass')
        api = client.google_shopping._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.google_shopping.scrape_shopping_url("https://shopping.google.com/search?q=laptop", render="html")

        self.assertEqual(captured["render"], "html")


class TestGoogleShoppingProductsSync(unittest.TestCase):
    """Tests that scrape_shopping_products parameters flow through to the payload."""

    def test_shopping_products_source(self):
        client = RealtimeClient('user', 'pass')
        api = client.google_shopping._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.google_shopping.scrape_shopping_products("product_token_123")

        self.assertEqual(captured["source"], "google_shopping_product")
        self.assertEqual(captured["query"], "product_token_123")

    def test_shopping_products_locale(self):
        client = RealtimeClient('user', 'pass')
        api = client.google_shopping._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.google_shopping.scrape_shopping_products("product_token_123", locale="de")

        self.assertEqual(captured["locale"], "de")


class TestGoogleShoppingPricingRemoved(unittest.TestCase):
    """Tests that scrape_product_pricing has been removed (deprecated Oct 2025)."""

    def test_product_pricing_removed(self):
        client = RealtimeClient('user', 'pass')
        self.assertFalse(hasattr(client.google_shopping, 'scrape_product_pricing'))
