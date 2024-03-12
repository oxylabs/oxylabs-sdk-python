# Oxylabs Python SDK

This is a Python SDK for the [Oxylabs](https://oxylabs.io) [Scraper APIs](https://developers.oxylabs.io/scraper-apis/getting-started).

This will help simplify integrating with Oxylabs's APIs, which can help you with retrieving search engine results (SERP), eCommerce data, real estate data, and more.

The Python SDK provides you with several benefits over using the raw APIs directly:

- **Simplified Interface**: abstracts away complexities, offering a straightforward user interface for interacting with the Oxylabs SERP API.
- **Automated Request Management**: streamlines the handling of API requests and responses for enhanced efficiency and reliability.
- **Error Handling**: provides meaningful error messages and handles common API errors, simplifying troubleshooting.
- **Result Parsing**: streamlines the process of extracting relevant data from SERP results, allowing developers to focus on application logic.

## Requirements

- Python 3.5 or above.

You can check your Python version by running the following command in your preferred terminal:

```sh
python --version
```

Or, for systems with multiple Python versions installed:

```sh
python3 --version
```

If you need to install or update python you can do so by following the steps mentioned [here](https://www.python.org/downloads/).

## Authentication

You will need an Oxylabs API username and password which you can get by signing up at https://oxylabs.io. You can check things out with a free trial at https://oxylabs.io/products/scraper-api/serp.

## Installation

```bash
pip install oxylabs
```

### Quick Start

```python
package main

import (
	"fmt"

	"github.com/mslmio/oxylabs-sdk-go/serp"
)

func main() {
	// Set your Oxylabs API Credentials.
	const username = "username"
	const password = "password"

	// Initialize the SERP realtime client with your credentials.
	c := serp.Init(username, password)

	// Use `google_search` as a source to scrape Google with adidas as a query.
	res, err := c.ScrapeGoogleSearch(
		"adidas",
	)
	if err != nil {
		panic(err)
	}

	fmt.Printf("Results: %+v\n", res)
}
```

### Integration Methods

There are three integration method for the Oxylabs SERP API, each exposed via different packages:

- Realtime (Sync) - `serp.Init(username, password)`
- Push-Pull (Async) - `serp.InitAsync(username, password)`
- Proxy Endpoint - `proxy.Init(username, password)`

Learn more about integration methods [on the official documentation](https://developers.oxylabs.io/scraper-apis/getting-started/integration-methods) and how this SDK uses them [here](#integration-methods-1).

### Sources

The Oxylabs SERP API scrapes according to the source provided via the API.

There are currently four search engines you can scrape with the Oxylabs SERP API, each with different sources.

| Search Engine | Sources
| ------------- | --------------
| **Google**    | `google`, `google_search`, `google_ads`, `google_hotels`, `google_travel_hotels`, `google_images`, `google_suggest`, `google_trends_explore`  
| **Yandex**    | `yandex`, `yandex_search`  
| **Bing**      | `bing`, `bing_search`
| **Baidu**     | `baidu`, `baidu_search`

In the SDK you'll just need to call the relevant function name from the client.

For example if you wish to scrape Yandex with `yandex_search` as a source:

```go
res, err := c.ScrapeYandexSearch("football")
```

### Query Parameters

Each source has different accepted query parameters. For a detailed list of accepted parameters by each source you can head over to https://developers.oxylabs.io/scraper-apis/serp-scraper-api.

By default, scrape functions will use default parameters. If you need to send specific query parameters, here is an example of how to do it:

```go
res, err := c.ScrapeYandexSearch(
	"football",
	&serp.YandexSearchOpts{
		StartPage: 1,
		Pages:     3,
		Limit:     4,
		Domain:    "com",
		Locale:    "en",
	},
)
```

### Configurable Options

For consistency and ease of use, this SDK provides a list of pre-defined commonly used parameter values as constants in our library. You can use them by importing the oxylabs package.

```go
import (
	"github.com/mslmio/oxylabs-sdk-go/oxylabs"
)
```

Currently these are available for the `Render` and`UserAgent` parameters. For the full list you can check `oxylabs/types.go`. You can send in these values as strings too.

These can be used as follows:

```go
res, err := c.ScrapeGoogleSearch(
	"adidas",
	&serp.GoogleSearchOpts{
		UserAgent: oxylabs.UA_DESKTOP_CHROME, // desktop_chrome
		Render:    oxylabs.HTML,              // html
		Domain:    oxylabs.DOMAIN_COM,        // com
	},
)
```

### Context Options for Google sources

You can send in context options relevant to `google` sources. Here's an example for Google Search scraping:

```go
res, err := c.ScrapeGoogleSearch(
	"adidas",
	&serp.GoogleSearchOpts{
		Parse: true,
		Context: []func(oxylabs.ContextOption){
			oxylabs.ResultsLanguage("en"),
			oxylabs.Filter(1),
			oxylabs.Tbm("isch"),
			oxylabs.LimitPerPage([]serp.PageLimit{{Page: 1, Limit: 1}, {Page: 2, Limit: 6}}),
		},
	},
)
```

### Parse instructions

SDK supports [custom parsing](https://developers.oxylabs.io/scraper-apis/custom-parser). 
There are 2 ways to provide `parsing_instructions` `_fns`:

```go
package main

import (
	"fmt"
	"github.com/mslmio/oxylabs-sdk-go/ecommerce"
	"github.com/mslmio/oxylabs-sdk-go/oxylabs"
)

func main() {
	const username = "username"
	const password = "password"

	// Initialize the SERP push-pull client with your credentials.
	c := ecommerce.InitAsync(username, password)

	ch, err := c.ScrapeUniversalUrl(
		"https://example.com",
		&ecommerce.UniversalUrlOpts{
			Parse: true,
			ParseInstructions: &map[string]interface{}{
				"title": map[string]interface{}{
					// Providing `_fns` as a map[string]interface{}.
					"_fns": []map[string]interface{}{
						{
							"_fn":   oxylabs.Xpath,
							"_args": []string{"//h1/text()"},
						},
					},
				},
				"second_paragraph": map[string]interface{}{
					// Providing `_fns` as a `[]oxylabs.Fn`.
					"_fns": []oxylabs.Fn{
						{
							Name: oxylabs.Xpath,
							Args: []string{"/html/body/div/p[2]"},
						},
					},
				},
			},
		},
	)
	if err != nil {
		fmt.Println(err)
		return
	}
	res := <-ch
	fmt.Println(res)
}
```

## Integration Methods

### Realtime Integration

Realtime is a synchronous integration method. This means that upon sending your job submission request, **you will have to keep the connection open** until we successfully finish your job or return an error.

The **TTL** of Realtime connections is **150 seconds**. There may be rare cases where your connection times out before you receive a response from us, for example, if our system is under heavier-than-usual load or the job you submitted was extremely hard to complete:

### Push Pull(Polling) Integration <a id="push-pull"></a>

Push-Pull is an asynchronous integration method. This SDK implements this integration with a polling technique to poll the endpoint for results after a set interval of time.

Using it as straightforward as using the realtime integration. The only difference is that it will return a channel with the Response. Below is an example of this integration method:

```go
package main

import (
	"fmt"

	"github.com/mslmio/oxylabs-sdk-go/oxylabs"
	"github.com/mslmio/oxylabs-sdk-go/serp"
)

func main() {
	const username = "username"
	const password = "password"

	// Initialize the SERP push-pull client with your credentials.
	c := serp.InitAsync(username, password)

	ch, err := c.ScrapeGoogleAds(
		"adidas shoes",
		&serp.GoogleAdsOpts{
			UserAgent: oxylabs.UA_DESKTOP,
			Parse:     true,
		},
	)
	if err != nil {
		panic(err)
	}

	res := <-ch
	fmt.Printf("Results: %+v\n", res)
}
```

### Proxy Endpoint

This method is also synchronous (like Realtime), but instead of using our service via a RESTful interface, you **can use our endpoint like a proxy**. Use Proxy Endpoint if you've used proxies before and would just like to get unblocked content from us.

Since the parameters in this method are sent as as headers there are only a few parameters which this integration method accepts. You can find those parameters at
https://developers.oxylabs.io/scraper-apis/getting-started/integration-methods/proxy-endpoint#accepted-parameters.

The proxy endpoint integration is very open ended allowing many different use cases. To cater this, the user is provided a pre-configured `http.Client` and they can use it as they deem fit:

```go
package main

import (
	"fmt"
	"io"
	"net/http"

	"github.com/mslmio/oxylabs-sdk-go/oxylabs"
	"github.com/mslmio/oxylabs-sdk-go/proxy"
)

func main() {
	const username = "username"
	const password = "password"

	// Init returns an http client pre configured with the proxy settings.
	c, _ := proxy.Init(username, password)

	request, _ := http.NewRequest(
		"GET",
		"https://www.example.com",
		nil,
	)

	// Add relevant Headers.
	proxy.AddUserAgentHeader(request, oxylabs.UA_DESKTOP)
	proxy.AddRenderHeader(request, oxylabs.HTML)
	proxy.AddParseHeader(request, "google_search")

	request.SetBasicAuth(username, password)
	response, _ := c.Do(request)

	resp, _ := io.ReadAll(response.Body)
	fmt.Println(string(resp))
}
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

Established in 2015, Oxylabs are a market-leading web intelligence collection platform, driven by the highest business, ethics, and compliance standards, enabling companies worldwide to unlock data-driven insights.

[![image](https://oxylabs.io/images/og-image.png)](https://oxylabs.io/)
