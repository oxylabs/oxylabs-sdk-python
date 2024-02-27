from serp.serp import SerpClient, SerpClientAsync
from serp.bing import Bing
from serp.bing_async import BingAsync
import json
from dotenv import load_dotenv
import os
import asyncio

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
        poll_interval=3
    )

    # Now that you have awaited the results, you can dump it into a file
    with open('results.json', 'w') as f:
        json.dump(results, f, indent=4)

# Ensure the main coroutine is executed
if __name__ == "__main__":
    asyncio.run(main())
