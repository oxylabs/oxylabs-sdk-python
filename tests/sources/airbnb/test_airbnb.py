import unittest
from oxylabs.internal import RealtimeClient


class TestAirbnbProductSync(unittest.TestCase):
    def test_product_source(self):
        client = RealtimeClient('user', 'pass')
        api = client.airbnb._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.airbnb.scrape_product("11984394")

        self.assertEqual(captured["source"], "airbnb_product")
        self.assertEqual(captured["product_id"], "11984394")


class TestAirbnbUrlSync(unittest.TestCase):
    def test_url_source(self):
        client = RealtimeClient('user', 'pass')
        api = client.airbnb._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.airbnb.scrape_url("https://www.airbnb.com/rooms/11984394")

        self.assertEqual(captured["source"], "airbnb")
