from serp.serp import Serp, SerpAsync
from serp.baidu import Baidu
from serp.google import Google
from serp.yandex import Yandex
from serp.bing import BingAsync, Bing
from proxy.proxy import Proxy
from dotenv import load_dotenv
import os
import asyncio

load_dotenv()


async def mainAsync():
    serp_client = SerpAsync(
        os.getenv("OXYLABS_USER"), os.getenv("OXYLABS_PASSWORD")
    )
    client = BingAsync(serp_client)

    results = await asyncio.gather(
        # client.scrape_bing_search(
        #     "nike", {"start_page": 1, "parse": True}, poll_interval=4, timeout=15
        # ),
        # client.scrape_bing_search("adidas", {"start_page": 1, "parse": True}),
        client.scrape_bing_url("https://www.bing.com/search?q=nike",{"parse": True}, timeout=45, poll_interval=3
    )
    )

    print(results)


def mainSync():
    serp_client = Serp(os.getenv("OXYLABS_USER"), os.getenv("OXYLABS_PASSWORD"))
    # bing = Bing(serp_client)

    # result = bing.scrape_bing_search(
    #     "nike",
    #     {
    #         "start_page": 1,
    #         "parse": True,
    #         'locale': 'fr'
    #     },
    #     timeout=15,
    # )

    # result = bing.scrape_bing_url(
    #     "https://www.bing.com/search?q=nike",
    #     {
    #         "parse": True,
    #     },
    #     timeout=45,
    # )
    
    # baidu = Baidu(serp_client)
    
    # result = baidu.scrape_baidu_search(
    #     "nike",
    #     {
    #         "start_page": 1,
    #         'user_agent_type': 'desktop',
    #         'parse': True,
    #     },
    #     timeout=15,
    # )
    
    # baidu.scrape_baidu_url(
    #     "https://www.baidu.com/s?wd=nike",
    #     {
    #         "parse": True,
    #     },
    #     timeout=45,
    # )
    
    
    # yandex = Yandex(serp_client)
    
    # yandex.scrape_yandex_search(
    #     "nike",
    #     {
    #         "start_page": 1,
    #         'limit': 3,
    #     },
    #     timeout=15,
    # )
    
    
    # yandex.scrape_yandex_url(
    #     "https://yandex.ru/search/?text=nike",
    #     timeout=45,
    # )
    
    
    # google = Google(serp_client)
    
    # google.scrape_google_search(
    #     "nike",
    #     {
    #         "start_page": 1,
    #         "parse": True,
    #     },
    #     timeout=15,
    # )
    
    
    # google.scrape_google_url(
    #     "https://www.google.com/search?q=nike",
    #     {
    #         "parse": True,
    #     },
    #     timeout=45,
    # )

    proxy = Proxy(os.getenv("OXYLABS_USER"), os.getenv("OXYLABS_PASSWORD"))

    proxy.add_user_agent_header("mobile_android")
    proxy.add_geo_location_header("Germany")
    proxy.add_render_header("html")
    # proxy.add_parse_header("google")
    result = proxy.get("https://www.example.com")

    print(result.text)
    

# Ensure the main coroutine is executed
if __name__ == "__main__":
    # asyncio.run(mainAsync())
    mainSync()
