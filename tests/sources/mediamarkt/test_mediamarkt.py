import unittest
from oxylabs.internal import RealtimeClient


class TestMediamarktSearchSync(unittest.TestCase):
    def test_search_source(self):
        client = RealtimeClient('user', 'pass')
        api = client.mediamarkt._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.mediamarkt.scrape_search("headphones")

        self.assertEqual(captured["source"], "mediamarkt_search")

    def test_search_domain(self):
        client = RealtimeClient('user', 'pass')
        api = client.mediamarkt._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.mediamarkt.scrape_search("headphones", domain="es")

        self.assertEqual(captured["domain"], "es")


class TestMediamarktProductSync(unittest.TestCase):
    def test_product_source(self):
        client = RealtimeClient('user', 'pass')
        api = client.mediamarkt._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.mediamarkt.scrape_product("123456")

        self.assertEqual(captured["source"], "mediamarkt_product")


class TestMediamarktUrlSync(unittest.TestCase):
    def test_url_source(self):
        client = RealtimeClient('user', 'pass')
        api = client.mediamarkt._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.mediamarkt.scrape_url("https://www.mediamarkt.de/")

        self.assertEqual(captured["source"], "mediamarkt")
