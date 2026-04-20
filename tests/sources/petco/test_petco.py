import unittest
from oxylabs.internal import RealtimeClient


class TestPetcoSearchSync(unittest.TestCase):
    def test_search_source(self):
        client = RealtimeClient('user', 'pass')
        api = client.petco._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.petco.scrape_search("dog food")

        self.assertEqual(captured["source"], "petco_search")


class TestPetcoUrlSync(unittest.TestCase):
    def test_url_source(self):
        client = RealtimeClient('user', 'pass')
        api = client.petco._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.petco.scrape_url("https://www.petco.com/")

        self.assertEqual(captured["source"], "petco")

