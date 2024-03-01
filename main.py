from serp.serp import SerpClient, SerpClientAsync
from serp.bing import Bing
from serp.baidu import Baidu
from serp.google import Google
from serp.yandex import Yandex
from serp.bing_async import BingAsync
from dotenv import load_dotenv
import os
import asyncio

load_dotenv()


async def mainAsync():
    serp_client = SerpClientAsync(
        os.getenv("OXYLABS_USER"), os.getenv("OXYLABS_PASSWORD")
    )
    client = BingAsync(serp_client)

    result = await asyncio.gather(
        client.scrape_bing_search(
            "nike", {"start_page": 1, "parse": True}, poll_interval=4, timeout=15
        ),
        client.scrape_bing_search("adidas", {"start_page": 1, "parse": True}),
        client.scrape_bing_search(
            "puma", {"start_page": 1, "parse": True}, poll_interval=5, timeout=35
        ),
    )


def mainSync():
    serp_client = SerpClient(os.getenv("OXYLABS_USER"), os.getenv("OXYLABS_PASSWORD"))
    bing = Bing(serp_client)

    bing.scrape_bing_search(
        "nike",
        {
            "start_page": 1,
            "parse": True,
            'locale': 'fr'
        },
        timeout=15,
    )

    bing.scrape_bing_url(
        "https://www.bing.com/search?q=nike",
        {
            "parse": True,
        },
        timeout=45,
    )
    
    baidu = Baidu(serp_client)
    
    baidu.scrape_baidu_search(
        "nike",
        {
            "start_page": 1,
            'user_agent_type': 'desktop',
        },
        timeout=15,
    )
    
    baidu.scrape_baidu_url(
        "https://www.baidu.com/s?wd=nike",
        {
            "parse": True,
        },
        timeout=45,
    )
    
    
    yandex = Yandex(serp_client)
    
    yandex.scrape_yandex_search(
        "nike",
        {
            "start_page": 1,
            'limit': 3,
        },
        timeout=15,
    )
    
    
    yandex.scrape_yandex_url(
        "https://yandex.ru/search/?text=nike",
        timeout=45,
    )
    
    
    google = Google(serp_client)
    
    google.scrape_google_search(
        "nike",
        {
            "start_page": 1,
            "parse": True,
        },
        timeout=15,
    )
    
    
    google.scrape_google_url(
        "https://www.google.com/search?q=nike",
        {
            "parse": True,
        },
        timeout=45,
    )
    
    print("Done")
    

# Ensure the main coroutine is executed
if __name__ == "__main__":
    asyncio.run(mainAsync())
    # mainSync()
