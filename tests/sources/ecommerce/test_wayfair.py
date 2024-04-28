import unittest
from src.oxylabs.sources.ecommerce import Ecommerce, EcommerceAsync
from src.oxylabs.utils.types import user_agent_type

class TestWayfairSearchSync(unittest.TestCase):
    def test_wayfair_search_sync(self):
        ecommerce = Ecommerce('user', 'pass')  # Mock these appropriately.
        query = "furniture"
        opts = {"start_page": 1, "pages": 1, "limit": 24}

        # Mock the _get_resp method to return a controlled response
        ecommerce._get_resp = lambda payload, config: {"mocked_response": "search_results"}
        
        result = ecommerce.wayfair.scrape_search(query, opts)
        self.assertIn("mocked_response", result)
        self.assertEqual(result["mocked_response"], "search_results")


class TestWayfairUrlSync(unittest.TestCase):
    def test_wayfair_url_sync(self):
        ecommerce = Ecommerce('user', 'pass')  # Mock these appropriately.
        url = "https://www.wayfair.com/furniture/sb0/sofas-c413892.html"
        opts = {"user_agent_type": user_agent_type.DESKTOP}

        # Mock the _get_resp method to return a controlled response
        ecommerce._get_resp = lambda payload, config: {"mocked_response": "url_results"}
        
        result = ecommerce.wayfair.scrape_url(url, opts)
        self.assertIn("mocked_response", result)
        self.assertEqual(result["mocked_response"], "url_results")


class TestWayfairSearchAsync(unittest.IsolatedAsyncioTestCase):
    async def test_wayfair_search_async(self):
        ecommerce_async = EcommerceAsync('user', 'pass')  # Mock these appropriately.
        query = "furniture"
        opts = {"start_page": 1, "pages": 1, "limit": 24}
        
        # Mock the _get_resp method to return a controlled response
        async def mock_get_resp(payload, config):
            return {"mocked_response": "async_search_results"}
        
        ecommerce_async._get_resp = mock_get_resp
        
        result = await ecommerce_async.wayfair_async.scrape_search(query, opts)
        self.assertIn("mocked_response", result)
        self.assertEqual(result["mocked_response"], "async_search_results")

class TestWayfairUrlAsync(unittest.IsolatedAsyncioTestCase):
    async def test_wayfair_url_async(self):
        ecommerce_async = EcommerceAsync('user', 'pass')  # Mock these appropriately.
        url = "https://www.wayfair.com/furniture/sb0/sofas-c413892.html"
        opts = {"user_agent_type": user_agent_type.DESKTOP}
        
        # Mock the _get_resp method to return a controlled response
        async def mock_get_resp(payload, config):
            return {"mocked_response": "async_url_results"}
        
        ecommerce_async._get_resp = mock_get_resp
        
        result = await ecommerce_async.wayfair_async.scrape_url(url, opts)
        self.assertIn("mocked_response", result)
        self.assertEqual(result["mocked_response"], "async_url_results")
