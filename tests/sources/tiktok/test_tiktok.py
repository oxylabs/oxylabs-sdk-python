import unittest
from oxylabs.internal import RealtimeClient


class TestTiktokShopSearchSync(unittest.TestCase):
    """Tests that scrape_shop_search parameters flow through to the payload."""

    def test_shop_search_source(self):
        client = RealtimeClient('user', 'pass')
        api = client.tiktok._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.tiktok.scrape_shop_search("phone case")

        self.assertEqual(captured["source"], "tiktok_shop_search")
        self.assertEqual(captured["query"], "phone case")

    def test_shop_search_render(self):
        client = RealtimeClient('user', 'pass')
        api = client.tiktok._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.tiktok.scrape_shop_search("phone case", render="html")

        self.assertEqual(captured["render"], "html")


class TestTiktokShopProductSync(unittest.TestCase):
    """Tests that scrape_shop_product parameters flow through to the payload."""

    def test_shop_product_source(self):
        client = RealtimeClient('user', 'pass')
        api = client.tiktok._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.tiktok.scrape_shop_product("1729553810632530")

        self.assertEqual(captured["source"], "tiktok_shop_product")
        self.assertEqual(captured["product_id"], "1729553810632530")

    def test_shop_product_domain(self):
        client = RealtimeClient('user', 'pass')
        api = client.tiktok._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.tiktok.scrape_shop_product("1729553810632530", domain="com")

        self.assertEqual(captured["domain"], "com")


class TestTiktokShopUrlSync(unittest.TestCase):
    """Tests that scrape_shop_url parameters flow through to the payload."""

    def test_shop_url_source(self):
        client = RealtimeClient('user', 'pass')
        api = client.tiktok._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.tiktok.scrape_shop_url("https://www.tiktok.com/@shop/product/123")

        self.assertEqual(captured["source"], "tiktok")
        self.assertEqual(captured["url"], "https://www.tiktok.com/@shop/product/123")

    def test_shop_url_user_agent(self):
        client = RealtimeClient('user', 'pass')
        api = client.tiktok._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.tiktok.scrape_shop_url("https://www.tiktok.com/@shop/product/123", user_agent_type="mobile")

        self.assertEqual(captured["user_agent_type"], "mobile")
