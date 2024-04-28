import unittest
from src.oxylabs.sources.serp import SERP, SERPAsync
from src.oxylabs.utils.types import user_agent_type

class TestBingSearchSync(unittest.TestCase):
    def test_bing_search_sync(self):
        serp = SERP('user', 'pass')  # Mock these appropriately.
        query = "nike"
        opts = {"domain": "com", "limit": 10}
        # Mock the _get_resp method to return a controlled response
        serp._get_resp = lambda payload, config: {"mocked_response": "search_results"}
        
        result = serp.bing.scrape_search(query, opts)
        print("result",result)
        self.assertIn("mocked_response", result)
        self.assertEqual(result["mocked_response"], "search_results")

class TestBingUrlSync(unittest.TestCase):
    def test_bing_url_sync(self):
        serp = SERP('user', 'pass')  # Mock these appropriately.
        url = "https://www.bing.com/search?q=nike"
        opts = {"user_agent_type": user_agent_type.DESKTOP}
        # Mock the _get_resp method to return a controlled response
        serp._get_resp = lambda payload, config: {"mocked_response": "url_results"}
        
        result = serp.bing.scrape_url(url, opts)
        self.assertIn("mocked_response", result)
        self.assertEqual(result["mocked_response"], "url_results")

class TestBingSearchAsync(unittest.IsolatedAsyncioTestCase):
    async def test_bing_search_async(self):
        serp_async = SERPAsync('user', 'pass')  # Mock these appropriately.
        query = "nike"
        opts = {"domain": "com", "limit": 10}
        
        # Mock the _get_resp method to return a controlled response
        async def mock_get_resp(payload, config):
            return {"mocked_response": "async_search_results"}
        
        serp_async._get_resp = mock_get_resp
        
        result = await serp_async.bing_async.scrape_search(query, opts)
        self.assertIn("mocked_response", result)
        self.assertEqual(result["mocked_response"], "async_search_results")

class TestBingUrlAsync(unittest.IsolatedAsyncioTestCase):
    async def test_bing_url_async(self):
        serp_async = SERPAsync('user', 'pass')  # Mock these appropriately.
        url = "https://www.bing.com/search?q=nike"
        opts = {"user_agent_type": user_agent_type.DESKTOP}
        
        # Mock the _get_resp method to return a controlled response
        async def mock_get_resp(payload, config):
            return {"mocked_response": "async_url_results"}
        
        serp_async._get_resp = mock_get_resp
        
        result = await serp_async.bing_async.scrape_url(url, opts)
        self.assertIn("mocked_response", result)
        self.assertEqual(result["mocked_response"], "async_url_results")
