import unittest
from oxylabs.internal import RealtimeClient


class TestGoogleAiModeSync(unittest.TestCase):
    """Tests that scrape_ai_mode parameters flow through to the payload."""

    def test_ai_mode_default_render(self):
        client = RealtimeClient('user', 'pass')
        api = client.google._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.google.scrape_ai_mode("what is python")

        self.assertEqual(captured["source"], "google_ai_mode")
        self.assertEqual(captured["query"], "what is python")
        self.assertEqual(captured["render"], "html")

    def test_ai_mode_parse(self):
        client = RealtimeClient('user', 'pass')
        api = client.google._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.google.scrape_ai_mode("what is python", parse=True)

        self.assertEqual(captured["parse"], True)

    def test_ai_mode_geo_location(self):
        client = RealtimeClient('user', 'pass')
        api = client.google._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.google.scrape_ai_mode("what is python", geo_location="United States")

        self.assertEqual(captured["geo_location"], "United States")


class TestGoogleNewsSync(unittest.TestCase):
    """Tests that scrape_news parameters flow through to the payload."""

    def test_news_injects_tbm(self):
        client = RealtimeClient('user', 'pass')
        api = client.google._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.google.scrape_news("breaking news")

        self.assertEqual(captured["source"], "google_search")
        self.assertEqual(captured["query"], "breaking news")
        tbm_found = False
        for item in captured["context"]:
            if item.get("key") == "tbm":
                self.assertEqual(item["value"], "nws")
                tbm_found = True
        self.assertTrue(tbm_found, "tbm=nws not found in context")

    def test_news_preserves_existing_context(self):
        client = RealtimeClient('user', 'pass')
        api = client.google._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        ctx = [{"key": "safe_search", "value": "true"}]
        client.google.scrape_news("breaking news", context=ctx)

        keys = [item["key"] for item in captured["context"]]
        self.assertIn("safe_search", keys)
        self.assertIn("tbm", keys)

    def test_news_does_not_override_tbm(self):
        client = RealtimeClient('user', 'pass')
        api = client.google._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        ctx = [{"key": "tbm", "value": "nws"}]
        client.google.scrape_news("breaking news", context=ctx)

        tbm_count = sum(1 for item in captured["context"] if item.get("key") == "tbm")
        self.assertEqual(tbm_count, 1)

    def test_news_domain(self):
        client = RealtimeClient('user', 'pass')
        api = client.google._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.google.scrape_news("breaking news", domain="co.uk")

        self.assertEqual(captured["domain"], "co.uk")

    def test_news_pagination(self):
        client = RealtimeClient('user', 'pass')
        api = client.google._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.google.scrape_news("breaking news", start_page=2, pages=3, limit=5)

        self.assertEqual(captured["start_page"], 2)
        self.assertEqual(captured["pages"], 3)
        self.assertEqual(captured["limit"], 5)
