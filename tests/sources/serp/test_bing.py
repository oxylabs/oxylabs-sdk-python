import unittest
from src.oxylabs.sources.serp import SERP, SERPAsync
from src.oxylabs.utils.types import user_agent_type

class TestBingSearchSync(unittest.TestCase):
    def test_bing_search_sync(self):
        """
        Tests synchronous SERP's Bing search functionality to ensure it returns expected results.

        Mocks the response from the _get_resp method to simulate SERP processing and validates
        that the method handles the search query correctly and returns the correct mock response.
        """
        serp = SERP('user', 'pass')
        query = "nike"
        opts = {"domain": "com", "limit": 10}
        serp._get_resp = lambda payload, config: {"mocked_response": "search_results"}
        
        result = serp.bing.scrape_search(query, opts)
        self.assertIn("mocked_response", result)
        self.assertEqual(result["mocked_response"], "search_results")

class TestBingUrlSync(unittest.TestCase):
    def test_bing_url_sync(self):
        """
        Tests the SERP's Bing URL scraping functionality in a synchronous manner.

        Mocks the _get_resp method to return controlled responses, ensuring that the method
        correctly processes the URL and user agent type, returning the expected data.
        """
        serp = SERP('user', 'pass')
        url = "https://www.bing.com/search?q=nike"
        opts = {"user_agent_type": user_agent_type.DESKTOP}
        serp._get_resp = lambda payload, config: {"mocked_response": "url_results"}
        
        result = serp.bing.scrape_url(url, opts)
        self.assertIn("mocked_response", result)
        self.assertEqual(result["mocked_response"], "url_results")

class TestBingSearchAsync(unittest.IsolatedAsyncioTestCase):
    async def test_bing_search_async(self):
        """
        Asynchronously tests SERP's Bing search to validate the async API handling.

        Uses a mocked asynchronous response to verify that the search query processing
        is handled correctly and that the async functionality returns expected results.
        """
        serp_async = SERPAsync('user', 'pass')
        query = "nike"
        opts = {"domain": "com", "limit": 10}
        async def mock_get_resp(payload, config):
            return {"mocked_response": "async_search_results"}
        serp_async._get_resp = mock_get_resp
        
        result = await serp_async.bing_async.scrape_search(query, opts)
        self.assertIn("mocked_response", result)
        self.assertEqual(result["mocked_response"], "async_search_results")

class TestBingUrlAsync(unittest.IsolatedAsyncioTestCase):
    async def test_bing_url_async(self):
        """
        Asynchronously tests SERP's Bing URL scraping functionality.

        Mocks the _get_resp method to provide controlled async responses, verifying that
        the URL and user agent options are processed correctly and yield expected outcomes.
        """
        serp_async = SERPAsync('user', 'pass')
        url = "https://www.bing.com/search?q=nike"
        opts = {"user_agent_type": user_agent_type.DESKTOP}
        async def mock_get_resp(payload, config):
            return {"mocked_response": "async_url_results"}
        serp_async._get_resp = mock_get_resp
        
        result = await serp_async.bing_async.scrape_url(url, opts)
        self.assertIn("mocked_response", result)
        self.assertEqual(result["mocked_response"], "async_url_results")
