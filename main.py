from serp.serp import SerpClient, SerpClientAsync
from serp.bing import Bing
from serp.bing_async import BingAsync
import json
from dotenv import load_dotenv
import os
import asyncio


# Initialize the clients
# serp_client = SerpClient("hamdan", "gzR4pHW9eiEM#Ky")


# browser = Bing(serp_client)

# results = browser.scrape_bing_search(
#     "iphone",
#     {
#         'start_page': 1,
#         'parse': True,
#     },
    
# )

# Load the environment variables from .env file
load_dotenv()

async def main():
    serp_client = SerpClientAsync(os.getenv('OXYLABS_USER'), os.getenv('OXYLABS_PASSWORD'))
    client = BingAsync(serp_client)

    # Await the async method and get the results
    results = await client.scrape_bing_search(
        "nike",
        {
            'start_page': 1,
            'parse': True,
        },
    )

    # Now that you have awaited the results, you can dump it into a file
    with open('results.json', 'w') as f:
        json.dump(results, f, indent=4)

# Ensure the main coroutine is executed
if __name__ == "__main__":
    asyncio.run(main())


# results = browser.scrape_bing_url('https://www.bing.com/search?form=MY0291&OCID=MY0291&q=Bing+AI&showconv=1',{
#     'user_agent_type': constants.UserAgent.UA_DESKTOP_CHROME.value,
#     'geo_location': 'Lahore, Punjab, Pakistan',
#     'parse': True,
# },3)

# results = browser.scrape_bing_search('pakistan', {
#     'parse': True,
#         "parse_instructions": {
#         "bing_search_results": {
#             "title": {
#                 "_fns": [
#                     {
#                         "_fn": "xpath",
#                         "_args": [
#                             "//li[@class='b_algo']/h2/a/text()"
#                         ]
#                     }
#                 ]
#             },
#             "description": {
#                 "_fns": [
#                     {
#                         "_fn": "xpath",
#                         "_args": [
#                             "//li[@class='b_algo']/div[@class='b_caption']/p/text()"
#                         ]
#                     }
#                 ]
#             },
#             "url": {
#                 "_fns": [
#                     {
#                         "_fn": "xpath",
#                         "_args": [
#                             "//li[@class='b_algo']/h2/a/@href"
#                         ]
#                     }
#                 ]
#             }
#         }
#     }
# })



# print(type(results)) results is dict now write to file as json