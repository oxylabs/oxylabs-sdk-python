from serp.serp import SerpClient, SerpClientAsync
from serp.bing import Bing, BingSearchOpts
import json


# Initialize the clients
serp_client = SerpClient('hamdan', 'gzR4pHW9eiEM#Ky')


browser = Bing(serp_client)

# # results = browser.scrape_bing_search('apple')
results = browser.scrape_bing_search('ford', {
    'parse': True,
})


# results = browser.scrape_bing_search('apple', {
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
with open('results.json', 'w') as f:
    json.dump(results, f, indent=4)