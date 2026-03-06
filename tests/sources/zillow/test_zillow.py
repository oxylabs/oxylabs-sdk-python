import unittest
from oxylabs.internal import RealtimeClient


class TestZillowUrlSync(unittest.TestCase):
    def test_url_source(self):
        client = RealtimeClient('user', 'pass')
        api = client.zillow._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.zillow.scrape_url("https://www.zillow.com/homes/for_sale/")

        self.assertEqual(captured["source"], "zillow")
        self.assertEqual(captured["url"], "https://www.zillow.com/homes/for_sale/")
