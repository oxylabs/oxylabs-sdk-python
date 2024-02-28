from serp.serp import SerpClient, SerpClientAsync
from serp.bing import Bing
from serp.bing_async import BingAsync
import json
from dotenv import load_dotenv
import os
import asyncio

load_dotenv()

async def mainAsync():
    serp_client = SerpClientAsync(os.getenv('OXYLABS_USER'), os.getenv('OXYLABS_PASSWORD'))
    client = BingAsync(serp_client)

    await asyncio.gather(
    client.scrape_bing_search("nike", {'start_page': 1, 'parse': True}, poll_interval=4, timeout=15),
    client.scrape_bing_search("adidas", {'start_page': 1, 'parse': True}),
    client.scrape_bing_search("puma", {'start_page': 1, 'parse': True}, poll_interval=5, timeout=35)
    )


    # Await the async method and get the results
    # results = await client.scrape_bing_search(
    #     "nike",
    #     {
    #         'start_page': 1,
    #         'parse': True,
    #     },
    #     poll_interval=4,
    #     timeout=15
    # )

    # await client.scrape_bing_search(
    #     "adidas",
    #     {
    #         'start_page': 1,
    #         'parse': True,
    #     }
    # )

    # await client.scrape_bing_search(
    #     "adidas",
    #     {
    #         'start_page': 1,
    #         'parse': True,
    #     },
    #     poll_interval=5,
    #     timeout=35
    # )

    # with open('results.json', 'w') as f:
    #     json.dump(results, f, indent=4)

def mainSync():
        serp_client = SerpClient(os.getenv('OXYLABS_USER'), os.getenv('OXYLABS_PASSWORD'))
        client = Bing(serp_client)

        results = client.scrape_bing_search(
        "nike",
        {
            'start_page': 1,
            'parse': True,
        },
        timeout=15
        )

        results2 = client.scrape_bing_url(
        "https://www.bing.com/search?q=nike",
        {
            'parse': True,
        },
        timeout=45
        )

        results3 = client.scrape_bing_url(
        "https://www.bing.com/search?q=nike",
        {
            'parse': True,
        },
        timeout=35
        )
            
        # with open('results.json', 'w') as f:
        #     json.dump(results, f, indent=4)


# Ensure the main coroutine is executed
if __name__ == "__main__":
    asyncio.run(mainAsync())
    #  mainSync()
