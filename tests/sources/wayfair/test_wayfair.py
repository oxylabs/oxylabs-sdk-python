import unittest
from oxylabs.internal.api import RealtimeAPI, AsyncAPI, APICredentials
from oxylabs.sources.wayfair import Wayfair, WayfairAsync
from oxylabs.utils.types import user_agent_type

class TestWayfairSearchSync(unittest.TestCase):
    def test_wayfair_search_sync(self):
        """
        Tests synchronous search functionality for Wayfair to ensure
        it returns expected results.

        This test mocks the get_response method to simulate the API responses
        and checks that the method handles the search query
        correctly and returns the correct mock response.
        """
        api = RealtimeAPI(APICredentials('user', 'pass'))
        api.get_response = lambda payload, config: {"mocked_response": "search_results"}
        wayfair = Wayfair(api)
        query = "furniture"
        opts = {"start_page": 1, "pages": 1, "limit": 24}
        
        result = wayfair.scrape_search(query, opts)
        self.assertIn("mocked_response", result.raw)
        self.assertEqual(result.raw["mocked_response"], "search_results")

class TestWayfairUrlSync(unittest.TestCase):
    def test_wayfair_url_sync(self):
        """
        Tests the Wayfair URL scraping functionality in a
        synchronous manner.

        This test mocks the get_response method to return controlled responses,
        ensuring that the method correctly processes the URL and user agent 
        type, returning the expected data.
        """
        api = RealtimeAPI(APICredentials('user', 'pass'))
        api.get_response = lambda payload, config: {"mocked_response": "url_results"}
        wayfair = Wayfair(api)
        url = "https://www.wayfair.com/furniture/sb0/sofas-c413892.html"
        opts = {"user_agent_type": user_agent_type.DESKTOP}
        
        result = wayfair.scrape_url(url, opts)
        self.assertIn("mocked_response", result.raw)
        self.assertEqual(result.raw["mocked_response"], "url_results")

class TestWayfairSearchAsync(unittest.IsolatedAsyncioTestCase):
    async def test_wayfair_search_async(self):
        """
        Asynchronously tests Wayfair search to validate the async
        API handling.

        Uses a mocked asynchronous response to verify that the search query 
        processing is handled correctly and that the async functionality 
        returns expected results.
        """
        api = AsyncAPI(APICredentials('user', 'pass'))
        async def mock_get_resp(payload, config):
            return {"mocked_response": "async_search_results"}
        api.get_response = mock_get_resp
        wayfair = WayfairAsync(api)
        query = "furniture"
        opts = {"start_page": 1, "pages": 1, "limit": 24}
        
        result = await wayfair.scrape_search(query, opts)
        self.assertIn("mocked_response", result.raw)
        self.assertEqual(result.raw["mocked_response"], "async_search_results")

class TestWayfairUrlAsync(unittest.IsolatedAsyncioTestCase):
    async def test_wayfair_url_async(self):
        """
        Asynchronously tests Wayfair URL scraping functionality.

        This test mocks the get_response method to provide controlled async
        responses, verifying that the URL and user agent options are processed 
        correctly and yield expected outcomes.
        """
        api = AsyncAPI(APICredentials('user', 'pass'))
        async def mock_get_resp(payload, config):
            return {"mocked_response": "async_url_results"}
        api.get_response = mock_get_resp
        wayfair = WayfairAsync(api)
        url = "https://www.wayfair.com/furniture/sb0/sofas-c413892.html"
        opts = {"user_agent_type": user_agent_type.DESKTOP}
        
        result = await wayfair.scrape_url(url, opts)
        self.assertIn("mocked_response", result.raw)
        self.assertEqual(result.raw["mocked_response"], "async_url_results")
