import unittest
from unittest.mock import patch, Mock
from src.oxylabs.proxy import Proxy

class TestProxyGet(unittest.TestCase):
    @patch('requests.Session')
    def test_proxy_get_with_timeout(self, MockSession):
        """
        Tests the Proxy.get method for correct timeout handling and header 
        setup.
        
        This test uses a mocked requests.Session to simulate HTTP responses and 
        validate
        the interaction, ensuring the Proxy class constructs requests with the 
        correct headers and timeout.

        Args:
            MockSession (MagicMock): A mock of the requests.Session to verify 
            request execution.

        Steps:
        1. Set up a mock response to simulate an HTTP response.
        2. Configure Proxy instance with headers.
        3. Make a request using Proxy.get with a timeout and verify the method 
           call and response.

        Assertions:
        - Verify correct URL and timeout parameters are passed to the session's 
          get method.
        - Check the response text matches expected content.
        """
        
        # Setup the mock response object with desired properties (like .text)
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.text = "Mock response content"

        # Setup the mock session to return the mock response on .get
        session_instance = MockSession.return_value
        session_instance.get.return_value = mock_response

        # Initialize the Proxy with credentials
        proxy = Proxy("wsapiuman", "A1705pdVe9hil")

        # Customize headers (optional)
        proxy.add_user_agent_header("desktop_chrome")
        proxy.add_geo_location_header("Germany")
        proxy.add_render_header("html")

        # Make the request using the proxy to the test URL
        result = proxy.get("https://www.example.com", request_timeout=10)

        # Assertions to ensure the request was made correctly
        session_instance.get.assert_called_with(
            "https://www.example.com", timeout=10
        )
        self.assertEqual(result.text, "Mock response content")
