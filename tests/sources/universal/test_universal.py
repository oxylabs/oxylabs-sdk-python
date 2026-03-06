import unittest                                                                                                                                                                                                                  
from oxylabs.internal import RealtimeClient                                                                                                                                                                                      
                                                                                                                                                                                                                                

class TestUniversalUrlSync(unittest.TestCase):                                                                                                                                                                                   
    def test_url_source(self):                                                                                                                                                                                                   
        client = RealtimeClient('user', 'pass')
        api = client.universal._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.universal.scrape_url("https://www.example.com")

        self.assertEqual(captured["source"], "universal_ecommerce")
        self.assertEqual(captured["url"], "https://www.example.com")

    def test_url_render(self):
        client = RealtimeClient('user', 'pass')
        api = client.universal._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.universal.scrape_url("https://www.example.com", render="html")

        self.assertEqual(captured["render"], "html")

    def test_url_parse(self):
        client = RealtimeClient('user', 'pass')
        api = client.universal._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.universal.scrape_url("https://www.example.com", parse=True)

        self.assertEqual(captured["parse"], True)

    def test_url_browser_instructions(self):
        client = RealtimeClient('user', 'pass')
        api = client.universal._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        instructions = [{"type": "click", "selector": ".btn"}]
        client.universal.scrape_url("https://www.example.com", render="html", browser_instructions=instructions)

        self.assertEqual(captured["browser_instructions"], instructions)

    def test_url_context(self):
        client = RealtimeClient('user', 'pass')
        api = client.universal._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        ctx = [{"key": "http_method", "value": "post"}]
        client.universal.scrape_url("https://www.example.com", context=ctx)

        self.assertEqual(captured["context"], ctx)