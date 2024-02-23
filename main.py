from serp.serp import SerpClient
from serp.bing import Bing
import json
from utils import constants


# Initialize the clients
serp_client = SerpClient("hamdan", "gzR4pHW9eiEM#Ky")


browser = Bing(serp_client)

results = browser.scrape_bing_search(
    "iphone",
    {
        'start_page': 1,
        'parse': True,
    },
    
)


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
with open("results.json", "w") as f:
    json.dump(results, f, indent=4)
    