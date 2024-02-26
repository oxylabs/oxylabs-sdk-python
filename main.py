from serp.serp import SerpClient
from serp.bing import Bing
from serp.baidu import Baidu
from serp.yandex import Yandex
import json
from utils.constants import Render, Domain, UserAgent, Locale
import random
import time

# Initialize the clients
serp_client = SerpClient("serpuman", "Alpha#Beta#123")

bing = Bing(serp_client)
baidu = Baidu(serp_client)
yandex = Yandex(serp_client)

results = bing.scrape_bing_search("nike",{'parse': True},4)
results = baidu.scrape_baidu_search("nike",{'parse': True,'domain':'cn'},1)
results = yandex.scrape_yandex_search("nike")

# results = bing.scrape_bing_url("https://www.bing.com/search?q=nike")
# results = baidu.scrape_baidu_url("https://www.baidu.com/s?wd=nike")
# results = yandex.scrape_yandex_url("https://yandex.com/search/?text=nike&lr=10616&search_source=yacom_desktop_common")



# print(type(results)) results is dict now write to file as json
# with open("results.json", "w") as f:
#     json.dump(results, f, indent=4)


