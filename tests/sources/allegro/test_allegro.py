import unittest
from oxylabs.internal import RealtimeClient


class TestAllegroSearchSync(unittest.TestCase):
    def test_search_source(self):
        client = RealtimeClient('user', 'pass')
        api = client.allegro._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.allegro.scrape_search("laptop")

        self.assertEqual(captured["source"], "allegro_search")

    def test_search_localization(self):
        client = RealtimeClient('user', 'pass')
        api = client.allegro._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.allegro.scrape_search("laptop", delivery_time="one_day", shipping_from="poland")

        self.assertEqual(captured["delivery_time"], "one_day")
        self.assertEqual(captured["shipping_from"], "poland")


class TestAllegroProductSync(unittest.TestCase):
    def test_product_source(self):
        client = RealtimeClient('user', 'pass')
        api = client.allegro._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.allegro.scrape_product("12345678901")

        self.assertEqual(captured["source"], "allegro_product")
