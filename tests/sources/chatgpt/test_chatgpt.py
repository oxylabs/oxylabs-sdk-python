import unittest
from oxylabs.internal import RealtimeClient


class TestChatgptSync(unittest.TestCase):
    """Tests that scrape parameters flow through to the payload."""

    def test_scrape_source(self):
        client = RealtimeClient('user', 'pass')
        api = client.chatgpt._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.chatgpt.scrape("best supplements for better sleep")

        self.assertEqual(captured["source"], "chatgpt")
        self.assertEqual(captured["prompt"], "best supplements for better sleep")

    def test_scrape_search(self):
        client = RealtimeClient('user', 'pass')
        api = client.chatgpt._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.chatgpt.scrape("best supplements", search=True)

        self.assertEqual(captured["search"], True)

    def test_scrape_geo_location(self):
        client = RealtimeClient('user', 'pass')
        api = client.chatgpt._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.chatgpt.scrape("best supplements", geo_location="United States")

        self.assertEqual(captured["geo_location"], "United States")

    def test_scrape_parse(self):
        client = RealtimeClient('user', 'pass')
        api = client.chatgpt._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.chatgpt.scrape("best supplements", parse=True)

        self.assertEqual(captured["parse"], True)
