from serp.serp import SerpClient
from serp.bing import Bing
from serp.baidu import Baidu
from serp.yandex import Yandex
from serp.google import Google
import json
from utils.constants import Render, Domain, UserAgent, Locale
import random
import time
import os
from dotenv import load_dotenv


# Load environment variables from .env file
load_dotenv()
username = os.getenv("SERP_USERNAME")
password = os.getenv("SERP_PASSWORD")
# Initialize the clients
serp_client = SerpClient(username, password)

bing = Bing(serp_client)
baidu = Baidu(serp_client)
yandex = Yandex(serp_client)
google = Google(serp_client)

# results = google.scrape_google_search("nike", {
#     'parse': True,
#     "context": [{
#         "key": "limit_per_page",
#         "value": [
#         {"page": 1, "limit": 10},
#         ]
#     }]
# })

results = google.scrape_google_travel_hotels("nike")

results = bing.scrape_bing_search("nike")
results = baidu.scrape_baidu_search("nike",{'pages': 1})
results = yandex.scrape_yandex_search("nike",{'pages': 0})

# results = bing.scrape_bing_url("https://www.bing.com/search?q=nike")
# results = baidu.scrape_baidu_url("https://www.baidu.com/s?wd=nike")
# results = yandex.scrape_yandex_url("https://yandex.com/search/?text=nike&lr=10616&search_source=yacom_desktop_common")


with open("results.json", "w") as f:
    json.dump(results, f, indent=4)


