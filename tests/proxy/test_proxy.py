import unittest
from unittest.mock import patch, Mock
from src.oxylabs.proxy import Proxy

class TestProxyGet(unittest.TestCase):
    @patch('requests.Session')
    def test_proxy_get_with_timeout(self, MockSession):
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
