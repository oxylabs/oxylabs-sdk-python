import unittest
from oxylabs.internal import RealtimeClient


class TestAmazonSearchParams(unittest.TestCase):
    """Tests that new parameters flow through to the payload for scrape_search."""

    def test_search_locale(self):
        client = RealtimeClient('user', 'pass')
        api = client.amazon._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.amazon.scrape_search("laptop", locale="en-us")

        self.assertEqual(captured["locale"], "en-us")

    def test_search_sort_by(self):
        client = RealtimeClient('user', 'pass')
        api = client.amazon._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.amazon.scrape_search("laptop", sort_by="price-asc-rank")

        self.assertEqual(captured["sort_by"], "price-asc-rank")

    def test_search_refinements(self):
        client = RealtimeClient('user', 'pass')
        api = client.amazon._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.amazon.scrape_search("laptop", refinements="p_n_condition-type:New")

        self.assertEqual(captured["refinements"], "p_n_condition-type:New")


class TestAmazonUrlParams(unittest.TestCase):
    """Tests that new parameters flow through to the payload for scrape_url."""

    def test_url_geo_location(self):
        client = RealtimeClient('user', 'pass')
        api = client.amazon._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.amazon.scrape_url("https://www.amazon.com/dp/B09V3KXJPB", geo_location="United States")

        self.assertEqual(captured["geo_location"], "United States")

    def test_url_locale(self):
        client = RealtimeClient('user', 'pass')
        api = client.amazon._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.amazon.scrape_url("https://www.amazon.com/dp/B09V3KXJPB", locale="en-us")

        self.assertEqual(captured["locale"], "en-us")

    def test_url_context(self):
        client = RealtimeClient('user', 'pass')
        api = client.amazon._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        ctx = [{"key": "currency", "value": "USD"}]
        client.amazon.scrape_url("https://www.amazon.com/dp/B09V3KXJPB", context=ctx)

        self.assertEqual(captured["context"], ctx)


class TestAmazonProductParams(unittest.TestCase):
    """Tests that new parameters flow through to the payload for scrape_product."""

    def test_product_locale(self):
        client = RealtimeClient('user', 'pass')
        api = client.amazon._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.amazon.scrape_product("B09V3KXJPB", locale="en-us")

        self.assertEqual(captured["locale"], "en-us")


class TestAmazonPricingParams(unittest.TestCase):
    """Tests that new parameters flow through to the payload for scrape_pricing."""

    def test_pricing_locale(self):
        client = RealtimeClient('user', 'pass')
        api = client.amazon._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.amazon.scrape_pricing("B09V3KXJPB", locale="en-us")

        self.assertEqual(captured["locale"], "en-us")

    def test_pricing_context(self):
        client = RealtimeClient('user', 'pass')
        api = client.amazon._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        ctx = [{"key": "currency", "value": "USD"}]
        client.amazon.scrape_pricing("B09V3KXJPB", context=ctx)

        self.assertEqual(captured["context"], ctx)


class TestAmazonBestsellersParams(unittest.TestCase):
    """Tests that new parameters flow through to the payload for scrape_bestsellers."""

    def test_bestsellers_locale(self):
        client = RealtimeClient('user', 'pass')
        api = client.amazon._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.amazon.scrape_bestsellers("11091801", locale="en-us")

        self.assertEqual(captured["locale"], "en-us")

    def test_bestsellers_context(self):
        client = RealtimeClient('user', 'pass')
        api = client.amazon._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        ctx = [{"key": "currency", "value": "USD"}]
        client.amazon.scrape_bestsellers("11091801", context=ctx)

        self.assertEqual(captured["context"], ctx)


class TestAmazonSellersParams(unittest.TestCase):
    """Tests that new parameters flow through to the payload for scrape_sellers."""

    def test_sellers_locale(self):
        client = RealtimeClient('user', 'pass')
        api = client.amazon._api_instance
        captured = {}
        api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

        client.amazon.scrape_sellers("ATVPDKIKX0DER", locale="en-us")

        self.assertEqual(captured["locale"], "en-us")
