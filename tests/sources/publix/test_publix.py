import unittest
from oxylabs.internal import RealtimeClient


class TestPublixSearchSync(unittest.TestCase):
    def test_search_source(self):
        client = RealtimeClient('user', 'pass')
        api = client.publix._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.publix.scrape_search("bread")

        self.assertEqual(captured["source"], "publix_search")

    def test_search_store(self):
        client = RealtimeClient('user', 'pass')
        api = client.publix._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.publix.scrape_search("bread", store_id=123)

        self.assertEqual(captured["store_id"], 123)


class TestPublixProductSync(unittest.TestCase):
    def test_product_source(self):
        client = RealtimeClient('user', 'pass')
        api = client.publix._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.publix.scrape_product("12345")

        self.assertEqual(captured["source"], "publix_product")


class TestPublixUrlSync(unittest.TestCase):
    def test_url_source(self):
        client = RealtimeClient('user', 'pass')
        api = client.publix._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.publix.scrape_url("https://www.publix.com/")

        self.assertEqual(captured["source"], "publix")
