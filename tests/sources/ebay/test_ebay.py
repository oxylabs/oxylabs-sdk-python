import unittest
from oxylabs.internal import RealtimeClient


class TestEbaySearchSync(unittest.TestCase):
    """Tests that scrape_search parameters flow through to the payload."""

    def test_search_source(self):
        client = RealtimeClient('user', 'pass')
        api = client.ebay._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.ebay.scrape_search("laptop")

        self.assertEqual(captured["source"], "ebay_search")
        self.assertEqual(captured["query"], "laptop")

    def test_search_domain(self):
        client = RealtimeClient('user', 'pass')
        api = client.ebay._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.ebay.scrape_search("laptop", domain="co.uk")

        self.assertEqual(captured["domain"], "co.uk")

    def test_search_start_page(self):
        client = RealtimeClient('user', 'pass')
        api = client.ebay._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.ebay.scrape_search("laptop", start_page=3)

        self.assertEqual(captured["start_page"], 3)


class TestEbayProductSync(unittest.TestCase):
    """Tests that scrape_product parameters flow through to the payload."""

    def test_product_source(self):
        client = RealtimeClient('user', 'pass')
        api = client.ebay._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.ebay.scrape_product("123456789")

        self.assertEqual(captured["source"], "ebay_product")
        self.assertEqual(captured["product_id"], "123456789")

    def test_product_domain(self):
        client = RealtimeClient('user', 'pass')
        api = client.ebay._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.ebay.scrape_product("123456789", domain="de")

        self.assertEqual(captured["domain"], "de")


class TestEbayUrlSync(unittest.TestCase):
    """Tests that scrape_url parameters flow through to the payload."""

    def test_url_source(self):
        client = RealtimeClient('user', 'pass')
        api = client.ebay._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.ebay.scrape_url("https://www.ebay.com/itm/123456789")

        self.assertEqual(captured["source"], "ebay")
        self.assertEqual(captured["url"], "https://www.ebay.com/itm/123456789")

    def test_url_render(self):
        client = RealtimeClient('user', 'pass')
        api = client.ebay._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.ebay.scrape_url("https://www.ebay.com/itm/123456789", render="html")

        self.assertEqual(captured["render"], "html")
