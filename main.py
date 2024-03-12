from oxylabs import Serp, SerpAsync, Ecommerce, EcommerceAsync, Proxy
from oxylabs.serp import Baidu, Google, GoogleAsync, Yandex, Bing, BingAsync
from oxylabs.ecommerce import Amazon, AmazonAsync, GoogleShopping, GoogleShoppingAsync, Wayfair, Wa
from dotenv import load_dotenv
import os
import asyncio

load_dotenv()

async def mainAsync():
    serp_client = SerpAsync(
        os.getenv("OXYLABS_USER_SERP"), os.getenv("OXYLABS_PASSWORD_SERP")
    )
    client = BingAsync(serp_client)
    google = GoogleAsync(serp_client)
    tasks = [
        # google.scrape_google_trends_explore("hello world", timeout=100, poll_interval=20),
        client.scrape_bing_url("https://www.bing.com/search?q=nike",{"parse": True, "parsing_instructions":
            {
            "number_of_results": {
            "_fns": [
                {
                    "_fn": "xpath_one",
                    "_args": [".//span[@class='sb_count']/text()"]
                }
            ]
        }
        }}, timeout=100, poll_interval=10),
        # client.scrape_bing_url("https://www.bing.com/search?q=adidas",{"parse": True}, timeout=100, poll_interval=3),
        # client.scrape_bing_url("https://www.bing.com/search?q=puma",{"parse": True}, timeout=100, poll_interval=6),
    ]
    index = 0
    for future in asyncio.as_completed(tasks):
        result = await future 
        with open(f'{index}.json', 'a', encoding='utf-8') as f:
            f.write(str(result) + "\n")
            
        index += 1


def mainSync():
    serp_client = Serp(os.getenv("OXYLABS_USER_SERP"), os.getenv("OXYLABS_PASSWORD_SERP"))
    bing = Bing(serp_client)

    result = bing.scrape_bing_search(
        "nike",
        {
            "start_page": 1,
            "parse": True,
            'locale': 'fr'
        },
        timeout=15,
    )

    print(result)

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

    # proxy = Proxy(os.getenv("OXYLABS_USER_SERP"), os.getenv("OXYLABS_PASSWORD_SERP"))

    # proxy.add_user_agent_header("mobile_android")
    # proxy.add_geo_location_header("Germany")
    # proxy.add_render_header("html")
    # # proxy.add_parse_header("google")
    # result = proxy.get("https://www.example.com")

    # print(result.text)
    

# Ensure the main coroutine is executed
if __name__ == "__main__":
    # asyncio.run(mainAsync())
    mainSync()
