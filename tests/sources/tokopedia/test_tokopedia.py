import unittest
from oxylabs.internal import RealtimeClient


class TestTokopediaSearchSync(unittest.TestCase):
    def test_search_source(self):
        client = RealtimeClient('user', 'pass')
        api = client.tokopedia._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.tokopedia.scrape_search("shampoo")

        self.assertEqual(captured["source"], "tokopedia_search")


class TestTokopediaUrlSync(unittest.TestCase):
    def test_url_source(self):
        client = RealtimeClient('user', 'pass')
        api = client.tokopedia._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.tokopedia.scrape_url("https://www.tokopedia.com/")

        self.assertEqual(captured["source"], "tokopedia")
