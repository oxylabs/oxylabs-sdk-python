import requests
import json
from bs4 import BeautifulSoup

class Resp:
    def __init__(self, parse, parse_instructions, status_code, status):
        self.parse = parse
        self.parse_instructions = parse_instructions
        self.status_code = status_code
        self.status = status

    @classmethod
    def from_http_resp(cls, http_resp: requests.Response, parse: bool, custom_parser_flag: bool):
        # If status code not 200, raise an exception
        if http_resp.status_code != 200:
            raise Exception(f"Error with status code {http_resp.status_code}: {http_resp.text}")

        # Parse the JSON object
        try:
            resp_body = http_resp.json()

            # Assuming 'results' key contains the HTML content
            html_content = resp_body['results'][0]['content']
            
            print(type(html_content))

            # Create a BeautifulSoup object with the HTML content
            soup = BeautifulSoup(html_content, 'html.parser')
            
            # remove all style tags
            for tag in soup.find_all('style'):
                tag.decompose()

            # Write the prettified HTML to a file
            with open('results.html', 'w', encoding='utf-8') as f:
                f.write(soup.prettify())
            
        except json.JSONDecodeError:
            raise Exception("Failed to parse JSON object")
        

        # soup = BeautifulSoup(http_resp.text, 'html.parser')
        
        # with open('results.txt', 'w', encoding='utf-8') as f:
        #     f.write(soup.prettify())

        # Create a Resp object and return it
        return cls(parse, custom_parser_flag, http_resp.status_code, http_resp.text)
