import unittest
from oxylabs.sources.ecommerce import Ecommerce, EcommerceAsync
from oxylabs.utils.types import user_agent_type

class TestWayfairSearchSync(unittest.TestCase):
    def test_wayfair_search_sync(self):
        """
        Tests synchronous search functionality for Ecommerce Wayfair to ensure 
        it returns expected results.

        This test mocks the _get_resp method to simulate the Ecommerce service 
        processing and checks that the method handles the search query 
        correctly and returns the correct mock response.
        """
        ecommerce = Ecommerce('user', 'pass')
        query = "furniture"
        opts = {"start_page": 1, "pages": 1, "limit": 24}
        ecommerce._get_resp = lambda payload, config: {"mocked_response": "search_results"}
        
        result = ecommerce.wayfair.scrape_search(query, opts)
        self.assertIn("mocked_response", result)
        self.assertEqual(result["mocked_response"], "search_results")

class TestWayfairUrlSync(unittest.TestCase):
    def test_wayfair_url_sync(self):
        """
        Tests the Ecommerce Wayfair URL scraping functionality in a 
        synchronous manner.

        This test mocks the _get_resp method to return controlled responses, 
        ensuring that the method correctly processes the URL and user agent 
        type, returning the expected data.
        """
        ecommerce = Ecommerce('user', 'pass')
        url = "https://www.wayfair.com/furniture/sb0/sofas-c413892.html"
        opts = {"user_agent_type": user_agent_type.DESKTOP}
        ecommerce._get_resp = lambda payload, config: {"mocked_response": "url_results"}
        
        result = ecommerce.wayfair.scrape_url(url, opts)
        self.assertIn("mocked_response", result)
        self.assertEqual(result["mocked_response"], "url_results")

class TestWayfairSearchAsync(unittest.IsolatedAsyncioTestCase):
    async def test_wayfair_search_async(self):
        """
        Asynchronously tests Ecommerce Wayfair search to validate the async 
        API handling.

        Uses a mocked asynchronous response to verify that the search query 
        processing is handled correctly and that the async functionality 
        returns expected results.
        """
        ecommerce_async = EcommerceAsync('user', 'pass')
        query = "furniture"
        opts = {"start_page": 1, "pages": 1, "limit": 24}
        async def mock_get_resp(payload, config):
            return {"mocked_response": "async_search_results"}
        ecommerce_async._get_resp = mock_get_resp
        
        result = await ecommerce_async.wayfair_async.scrape_search(query, opts)
        self.assertIn("mocked_response", result)
        self.assertEqual(result["mocked_response"], "async_search_results")

class TestWayfairUrlAsync(unittest.IsolatedAsyncioTestCase):
    async def test_wayfair_url_async(self):
        """
        Asynchronously tests Ecommerce Wayfair URL scraping functionality.

        This test mocks the _get_resp method to provide controlled async 
        responses, verifying that the URL and user agent options are processed 
        correctly and yield expected outcomes.
        """
        ecommerce_async = EcommerceAsync('user', 'pass')
        url = "https://www.wayfair.com/furniture/sb0/sofas-c413892.html"
        opts = {"user_agent_type": user_agent_type.DESKTOP}
        async def mock_get_resp(payload, config):
            return {"mocked_response": "async_url_results"}
        ecommerce_async._get_resp = mock_get_resp
        
        result = await ecommerce_async.wayfair_async.scrape_url(url, opts)
        self.assertIn("mocked_response", result)
        self.assertEqual(result["mocked_response"], "async_url_results")
