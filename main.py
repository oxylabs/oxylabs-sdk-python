from serp.serp import SerpClient, SerpClientAsync, SerpProxyClient          
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

# proxy_client = SerpProxyClient(username, password)
# proxy_client.add_user_agent_header(UserAgent.UA_DESKTOP.value)

# results = proxy_client.get("https://www.bing.com/search?q=nike")


# # Save returned HTML to result.html file
# with open('result.html', 'w', encoding='utf-8') as f:
#     f.write(results.text)


# bing = Bing(serp_client)
# baidu = Baidu(serp_client)
# yandex = Yandex(serp_client)
google = Google(serp_client)

results = google.scrape_google_images("https://www.google.com/url?sa=i&url=https%3A%2F%2Ftelanganatoday.com%2Fgoogle-multisearch-tool-to-help-users-search-with-photos&psig=AOvVaw3QjWyl5T8zQksFYrLiamF6&ust=1709201835847000&source=images&cd=vfe&opi=89978449&ved=0CBMQjRxqFwoTCLjhl5TnzYQDFQAAAAAdAAAAABAP", {
    'parse': True,
    "context": [{
        "key": "tbm",
        "value": "isch"
    }]
})

# results = google.scrape_google_travel_hotels("nike")

# results = bing.scrape_bing_search("nike",
#     {
#         'parse': True,
#         'limit': 5,   
#         'geo_location': 'Harrisburg,Arkansas,United States',
#     })
# results = baidu.scrape_baidu_search("nike",{'pages': 1})
# results = yandex.scrape_yandex_search("nike",{'pages': 1})

# results = bing.scrape_bing_url("https://www.bing.com/search?q=nike",
# {
#     'parse': True,
#     'geo_location': 'Harrisburg,Arkansas,United States',
# })
# results = baidu.scrape_baidu_url("https://www.baidu.com/s?wd=nike")
# results = yandex.scrape_yandex_url("https://yandex.com/search/?text=nike&lr=10616&search_source=yacom_desktop_common")


with open("results.json", "w") as f:
    json.dump(results, f, indent=4)


