# Oxylabs Python SDK

[![Oxylabs promo code](https://raw.githubusercontent.com/oxylabs/product-integrations/refs/heads/master/Affiliate-Universal-1090x275.png)](https://oxylabs.io/pages/gitoxy?utm_source=877&utm_medium=affiliate&groupid=877&utm_content=oxylabs-sdk-python-github&transaction_id=102f49063ab94276ae8f116d224b67)

[![](https://dcbadge.vercel.app/api/server/eWsVUJrnG5)](https://discord.gg/Pds3gBmKMH)

This is a Python SDK for the [Oxylabs](https://oxylabs.io)
[Scraper APIs](https://developers.oxylabs.io/scraper-apis/web-scraper-api#getting-started).

This SDK helps integrate with Oxylabs’ all-in-one Web Scraper API. 
It can help you retrieve data from e-commerce websites, search engines (SERP), 
real estate platforms, and more.

The Python SDK provides you with several benefits over using the raw APIs
directly:

- **Simplified Interface**: abstracts away complexities, offering a
straightforward user interface for interacting with the Oxylabs API.
- **Automated Request Management**: streamlines the handling of API requests and
 responses for enhanced efficiency and reliability.
- **Error Handling**: provides meaningful error messages and handles common API
errors, simplifying troubleshooting.
- **Result Parsing**: streamlines the process of extracting relevant data from HTML results, 
allowing developers to focus on application logic.

## Requirements

- Python 3.5 or above.

You can check your Python version by running the following command in your
preferred terminal:

```sh
python --version
```

Or, for systems with multiple Python versions installed:

```sh
python3 --version
```

If you need to install or update python you can do so by following the steps
mentioned [here](https://www.python.org/downloads/).

## Authentication

You will need an Oxylabs API username and password which you can get by signing
up at https://oxylabs.io. You can check things out with a free trial at
https://oxylabs.io/products/scraper-api.

## Installation

```bash
pip install oxylabs
```

### Quick Start

```python
from oxylabs import RealtimeClient

# Set your Oxylabs API Credentials.
username = "username"
password = "password"

# Initialize the Realtime client with your credentials.
client = RealtimeClient(username, password)

# Use `bing_search` as a source to scrape Bing with nike as a query.
result = client.bing.scrape_search("nike")

print(result.raw)
```

### Integration Methods

There are three integration methods for the Oxylabs SERP API, each exposed via
different packages:

- Realtime (Sync) - `RealtimeClient(username, password)`
- Push-Pull (Async) - `AsyncClient(username, password)`
- Proxy Endpoint - `ProxyClient(username, password)`

Learn more about integration methods [on the official documentation](https://developers.oxylabs.io/scraper-apis/web-scraper-api/integration-methods)
and how this SDK uses them [here](#integration-methods-1).

### Sources

The Oxylabs API scrapes according to the sources provided via the API:

| Target                 | Sources
|------------------------| --------------
| **Amazon**             | `amazon`, `amazon_product`, `amazon_search`, `amazon_pricing`, `amazon_sellers`, `amazon_bestsellers`, `amazon_reviews`, `amazon_questions`
| **Google**             | `google`, `google_search`, `google_ads`, `google_travel_hotels`, `google_images`, `google_suggest`,`google_trends_explore`,`google_maps`,`google_lens`
| **Google Shopping**    | `google_shopping`, `google_shopping_product`, `google_shopping_search`, `google_shopping_pricing`
| **Bing**               | `bing`, `bing_search`
| **Kroger**             | `kroger`, `kroger_product`, `kroger_search`
| **Wayfair**            | `wayfair`, `wayfair_search`
| **Youtube Transcript** | `youtube_transcript`
| **Other Websites**     | `universal`

These are the equivalent targets and methods available for scraping in the Python SDK:

| Target                 | Methods
|------------------------| --------------
| **amazon**             | `scrape_search`, `scrape_url`, `scrape_product`, `scrape_pricing`, `scrape_reviews`, `scrape_questions`, `scrape_bestsellers`, `scrape_sellers` 
| **bing**               | `scrape_search`, `scrape_url`
| **google**             | `scrape_search`, `scrape_url`, `scrape_ads`, `scrape_suggestions`, `scrape_travel_hotels`, `scrape_images`, `scrape_trends_explore`, `scrape_maps`, `scrape_lens`
| **google_shopping**    | `scrape_shopping_search`, `scrape_shopping_url`, `scrape_shopping_products`, `scrape_product_pricing`
| **kroger**             | `scrape_product`, `scrape_search`, `scrape_url`
| **wayfair**            | `scrape_search`, `scrape_url`
| **youtube_transcript** | `scrape_transcript`
| **universal**          | `scrape_url`

In the SDK you'll just need to call the relevant method name from the client.

For example if you wish to scrape Bing search you can do it with the following code:

```python
client = RealtimeClient(username, password)
result = client.bing.scrape_search("football")
```

### Query Parameters

Each source has different accepted query parameters. For a detailed list of
accepted parameters by each source you can head over to
https://developers.oxylabs.io/scraper-apis/web-scraper-api.

By default, scrape functions will use default parameters. If you need to send
specific query parameters, here is an example of how to do it:

```python
client = RealtimeClient(username, password)
result = client.bing.scrape_search(
    "football",
    start_page=1,
    pages=3,
    limit=4,
    domain="com",
)
```

### Configurable Options

For consistency and ease of use, this SDK provides a list of pre-defined
commonly used parameter values as constants in our library. You can use them by
importing the oxylabs type module.

```python
from oxylabs.utils.types import user_agent_type, render, domain
```

For the full list you can check the `types` directory. You can send in these
values as strings too.

These can be used as follows:

```python
from oxylabs import RealtimeClient
from oxylabs.utils.types import user_agent_type, render, domain

client = RealtimeClient(username, password)
result = client.google.scrape_search(
    "adidas",
    user_agent_type=user_agent_type.DESKTOP,
    render=render.HTML,
    domain=domain.COM,
)
```

### Context Options for Google sources

You can send in context options relevant to `google`, `amazon` and `universal`
sources. Here are the [supported context values for google search](https://developers.oxylabs.io/scraper-apis/web-scraper-api/google/search).
Similarly you can find supported context values for other sources in the
documentation.
Here's an example for Google Search scraping:

```python
client = RealtimeClient(username, password)
result = client.google.scrape_search(
    "adidas",
    parse=True,
    context=[
        {"key": "results_language", "value": "en"},
        {"key": "filter", "value": 0},
        {"key": "tbm", "value": "isch"},
        {
            "key": "limit_per_page",
            "value": [
                {"page": 1, "limit": 10},
                {"page": 2, "limit": 10},
            ],
        },
    ],
)
```

### Parse instructions

SDK supports [custom parsing](https://developers.oxylabs.io/scraper-apis/custom-parser) which lets
you define your own parsing and data processing logic that is executed on a raw scraping result.

```python
# Use `bing_search` as a source to scrape Bing using custom parsing
# instructions.
client = RealtimeClient(username, password)
result = client.bing.scrape_url(
    "https://www.bing.com/search?q=nike",
    parse=True,
    parsing_instructions={
        "number_of_results": {
            "_fns": [
                {
                    "_fn": "xpath_one",
                    "_args": [".//span[@class='sb_count']/text()"],
                }
            ]
        }
    },
)
```

### Browser instructions

SDK allows you to define your own [browser instructions](https://developers.oxylabs.io/scraper-apis/web-scraper-api/features/browser-instructions)
that are executed when rendering JavaScript.

```python
client = RealtimeClient(username, password)
result = client.universal.scrape_url(
    "https://www.ebay.com/",
    render="html",
    browser_instructions=[
        {
            "type": "input",
            "value": "pizza boxes",
            "selector": {
                "type": "xpath",
                "value": "//input[@class='gh-tb ui-autocomplete-input']"
            }
        },
        {
            "type": "click",
            "selector": {
                "type": "xpath",
                "value": "//input[@type='submit']"
            }
        },
        {
            "type": "wait",
            "wait_time_s": 10
        }
])
```

### Dedicated parsers
Oxylab's Web Scraper API has dedicated parsers for some sources. You can find a list of available
dedicated parsers [here](https://developers.oxylabs.io/scraper-apis/web-scraper-api/features/dedicated-parsers). If you want to use a dedicated parser to get structured data,
then add **parse=True** parameter when calling scrape method.

Here is an example of using a dedicated parser:

```python
# Scrape Amazon search results for keyword "headset"
# Then print a list of products including their ASIN and title
client = RealtimeClient(username, password)
response = client.amazon.scrape_search("headset", parse=True)

for result in response.results:
    for item in result.content["results"]["organic"]:
        print(f"{item["asin"]}: {item["title"]}")
```

## Integration Methods

### Realtime Integration

Realtime is a synchronous integration method. This means that upon sending your
job submission request, **you will have to keep the connection open** until we
successfully finish your job or return an error.

The **TTL** of Realtime connections is **150 seconds**. There may be rare cases
where your connection times out before you receive a response from us, for
example, if our system is under heavier-than-usual load or the job you submitted
was extremely hard to complete:

### Push-Pull(Polling) Integration <a id="push-pull"></a>

Push-Pull is an asynchronous integration method. This SDK implements this
integration with a polling technique to poll the endpoint for results after a
set interval of time.

Using it is as straightforward as using the Realtime integration. The only
difference is that it will return an asyncio Task that will eventually contain
the Response. Below is an example of this integration method:

```python
import asyncio
from oxylabs import AsyncClient

async def main():
    # Set your Oxylabs API Credentials.
    username = "username"
    password = "password"

    # Initialize the async client with your credentials.
    client = AsyncClient(username, password)

    # 'timeout' specifies the maximum time (in seconds) to wait for the scraping
    #  job to complete.
    # It is applicable for both Realtime and Push-Pull integrations.
    # 'poll_interval' is used only in Push-Pull integrations to set the delay
    # (in seconds)
    # between consecutive status checks of the job.
    tasks = [
        client.bing.scrape_url(
            "https://www.bing.com/search?q=adidas",
            parse=True,
            timeout=35,
            poll_interval=3,
        ),
        client.bing.scrape_url(
            "https://www.bing.com/search?q=puma",
            parse=True,
            timeout=45,
            poll_interval=5,
        ),
    ]

    for future in asyncio.as_completed(tasks):
        result = await future


if __name__ == "__main__":
    asyncio.run(main())
```

### Proxy Endpoint

This method is also synchronous (like Realtime), but instead of using our
service via a RESTful interface, you **can use our endpoint like a proxy**. Use
Proxy Endpoint if you've used proxies before and would just like to get
unblocked content from us.

Since the parameters in this method are sent as headers there are only a few
parameters which this integration method accepts. You can find those parameters
at
https://developers.oxylabs.io/scraper-apis/web-scraper-api/integration-methods/proxy-endpoint#accepted-parameters.

The Proxy endpoint integration is very open-ended allowing many different use
cases:

```python
from oxylabs import ProxyClient

# Set your Oxylabs API Credentials.
username = "username"
password = "password"

# Initialize the ProxyClient with your credentials.
proxy = ProxyClient(username, password)

# Customize headers for specific requirements (optional).
proxy.add_user_agent_header("desktop_chrome")
proxy.add_geo_location_header("Germany")
proxy.add_render_header("html")

# Use the proxy to make a request.
result = proxy.get("https://www.example.com")

print(result.text)
```

## Additional Resources

See the official [API Documentation](https://developers.oxylabs.io/) for
details on each API's actual interface, which is implemented by this SDK.

## Contributing

See [CONTRIBUTING](CONTRIBUTING.md) for more information.

## Security

See [Security Issue
Notifications](CONTRIBUTING.md#security-issue-notifications) for more
information.

## License

This project is licensed under the [MIT License](LICENSE).

## About Oxylabs

Established in 2015, Oxylabs are a market-leading web intelligence collection
platform, driven by the highest business, ethics, and compliance standards,
enabling companies worldwide to unlock data-driven insights.

[![image](https://oxylabs.io/images/og-image.png)](https://oxylabs.io/)
