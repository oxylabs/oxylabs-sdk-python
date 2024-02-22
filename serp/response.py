import json
from requests.models import Response


class Resp:
    def __init__(self, parse, parse_instructions, status_code, response_body):
        """
        Initializes a Response object.

        Args:
            parse (bool): Indicates whether the response should be parsed.
            parse_instructions (dict): Instructions for parsing the response.
            status_code (int): The HTTP status code of the response.
            response_body (str): The body of the response.

        Returns:
            None
        """
        self.parse = parse
        self.parse_instructions = parse_instructions
        self.status_code = status_code
        self.response_body = response_body

    @classmethod
    def from_http_resp(cls, http_response, parse, custom_parser_flag):
            """
            Creates a Response object from an HTTP response.

            Args:
                http_response (requests.Response): The HTTP response object.
                parse (bool): Flag indicating whether to parse the response.
                custom_parser_flag (bool): Flag indicating whether to use a custom parser.

            Returns:
                Response: The created Response object.

            Raises:
                Exception: If the status code of the HTTP response is not 200.
                Exception: If failed to parse the JSON object.
            """
            # If status code not 200, raise an exception
            if http_response.status_code != 200:
                raise Exception(f"Error with status code {http_response.status_code}: {http_response.text}")

            # Parse the JSON object
            try:
                response_body = http_response.json()
            except json.JSONDecodeError:
                raise Exception("Failed to parse JSON object")
                        
            # Create a Resp object and return it
            return cls(parse, custom_parser_flag, http_response.status_code, response_body)

