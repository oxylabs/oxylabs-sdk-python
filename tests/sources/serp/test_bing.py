import unittest
from oxylabs.utils.types import user_agent_type
from oxylabs.internal import AsyncClient, RealtimeClient

class TestBingSearchSync(unittest.TestCase):
    """
    Test case for synchronous Bing search.

    This test case tests the functionality of the synchronous Bing search
    in the RealtimeClient class. It uses a mock response to simulate the
    behavior of the Bing search.
    """

    def test_bing_search_sync(self):
        """
        Test the synchronous Bing search.

        This test creates a RealtimeClient and sets its _get_resp method to a
        lambda function that returns a mock response. It then calls the
        scrape_search method with a query and checks that the returned result
        contains the mock response.
        """
        client = RealtimeClient('user', 'pass')
        query = "nike"
        client._get_resp = lambda payload, config: {"mocked_response": "search_results"}
        
        result = client.serp.bing.scrape_search(query, domain="com", limit=10)
        self.assertIn("mocked_response", result)
        self.assertEqual(result["mocked_response"], "search_results")

class TestBingUrlSync(unittest.TestCase):
    """
    Test case for synchronous Bing URL scraping.

    This test case tests the functionality of the synchronous Bing URL scraping
    in the RealtimeClient class. It uses a mock response to simulate the
    behavior of the Bing URL scraping.
    """

    def test_bing_url_sync(self):
        """
        Test the synchronous Bing URL scraping.

        This test creates a RealtimeClient and sets its _get_resp method to a
        lambda function that returns a mock response. It then calls the
        scrape_url method with a URL and checks that the returned result
        contains the mock response.
        """

        client = RealtimeClient('user', 'pass')
        url = "https://www.bing.com/search?q=nike"
        opts = {"user_agent_type": user_agent_type.DESKTOP}
        client._get_resp = lambda payload, config: {"mocked_response": "url_results"}
        
        result = client.serp.bing.scrape_url(url, opts)
        self.assertIn("mocked_response", result)
        self.assertEqual(result["mocked_response"], "url_results")


class TestBingSearchAsync(unittest.IsolatedAsyncioTestCase):
    """
    Test case for asynchronous Bing search.

    This test case tests the functionality of the asynchronous Bing search
    in the AsyncClient class. It uses a mock response to simulate the
    behavior of the Bing search.
    """

    async def test_bing_search_async(self):
        """
        Test the asynchronous Bing search.

        This test creates an AsyncClient and sets its _get_resp method to a
        mock function that returns a mock response. It then calls the
        scrape_search method with a query and checks that the returned result
        contains the mock response.
        """
        client = AsyncClient('user', 'pass')
        query = "nike"
        opts = {"domain": "com", "limit": 10}
        async def mock_get_resp(payload, config):
            return {"mocked_response": "async_search_results"}
        client._get_resp = mock_get_resp
        
        result = await client.serp.bing.scrape_search(query, opts)
        self.assertIn("mocked_response", result)
        self.assertEqual(result["mocked_response"], "async_search_results")

class TestBingUrlAsync(unittest.IsolatedAsyncioTestCase):
    """
    Test case for asynchronous Bing URL scraping.

    This test case tests the functionality of the asynchronous Bing URL scraping
    in the AsyncClient class. It uses a mock response to simulate the
    behavior of the Bing URL scraping.
    """

    async def test_bing_url_async(self):
        """
        Test the asynchronous Bing URL scraping.

        This test creates an AsyncClient and sets its _get_resp method to a
        mock function that returns a mock response. It then calls the
        scrape_url method with a URL and checks that the returned result
        contains the mock response.
        """
        client = AsyncClient('user', 'pass')
        url = "https://www.bing.com/search?q=nike"
        opts = {"user_agent_type": user_agent_type.DESKTOP}
        async def mock_get_resp(payload, config):
            return {"mocked_response": "async_url_results"}
        client._get_resp = mock_get_resp
        
        result = await client.serp.bing.scrape_url(url, opts)
        self.assertIn("mocked_response", result)
        self.assertEqual(result["mocked_response"], "async_url_results")
