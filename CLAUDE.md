# Oxylabs Python SDK

Python SDK for Oxylabs Web Scraper APIs. Provides sync (`RealtimeClient`) and async (`AsyncClient`) wrappers for 50+ scraping sources.

## Repository Structure

```
src/oxylabs/
├── internal/
│   ├── api.py              # Base API classes (RealtimeAPI, AsyncAPI)
│   └── client.py           # RealtimeClient, AsyncClient — registers all sources
├── sources/
│   ├── <source>/<source>.py # Each source has sync + async class
│   ├── north_american/      # bestbuy, costco, lowes, walmart, target_store, etc.
│   ├── asian/               # alibaba, aliexpress, flipkart, lazada, etc.
│   ├── european/            # allegro, cdiscount, idealo, mediamarkt
│   ├── latin_american/      # falabella, mercadolibre, mercadolivre, etc.
│   ├── real_estate/         # airbnb, zillow
│   └── response.py          # Shared Response class
├── utils/
│   ├── types/source.py      # Source name constants (e.g. AMAZON_SEARCH = "amazon_search")
│   └── utils.py             # Helpers (prepare_config, check_parsing_instructions_validity)
└── proxy/proxy.py

tests/sources/               # Mirrors source structure
```

## Documentation → SDK Path Mapping

Documentation changes come from `scraping-solutions/web-scraper-api/`. Two main areas:

### Targets (`targets/`)
- **Hyphens → underscores:** `north-american-e-commerce` → `north_american`
- **Doc file → SDK method:** `search.md` → `scrape_search()`, `product.md` → `scrape_product()`, `url.md` → `scrape_url()`
- **Top-level targets:** `targets/amazon/` → `src/oxylabs/sources/amazon/amazon.py`
- **Regional targets:** `targets/north-american-e-commerce/bestbuy/` → `src/oxylabs/sources/north_american/bestbuy/bestbuy.py`
- **Regional groupings:**
  - `north-american-e-commerce/` → `north_american/`
  - `asian-e-commerce/` → `asian/`
  - `european-e-commerce/` → `european/`
  - `latin-american-e-commerce/` → `latin_american/`
  - `real-estate/` → `real_estate/`

### Features (`features/`)
Cross-cutting parameters that may apply across multiple sources. The table below lists known examples — new feature docs may introduce parameters not listed here. Apply the same pattern: if a feature doc describes a new request payload parameter, it likely needs to be added to SDK methods.

| Feature doc | SDK parameter | Notes |
|---|---|---|
| `custom-parser/parser-presets.md` | `parser_preset` | Use a saved parser preset |
| `js-rendering-and-browser-control/browser-instructions/` | `browser_instructions` | Browser automation, requires `render="html"` |
| `localization/proxy-location.md` | `session_id` | Sticky session for same proxy IP |
| `http-context-and-job-management/client-notes.md` | `client_notes` | Tracking notes saved with the job |
| `result-processing-and-storage/result-aggregator.md` | `aggregate_name` | Route results to a named aggregator |
| `result-processing-and-storage/cloud-storage/` | `storage_type`, `storage_url` | Cloud storage destination |
| `result-processing-and-storage/output-types/markdown-output.md` | `markdown` | Get markdown output |
| `result-processing-and-storage/output-types/capturing-network-requests-fetch-xhr.md` | `xhr` | Capture Fetch/XHR requests, requires `render="html"` |
| `result-processing-and-storage/output-types/download-images.md` | `content_encoding` | Base64 encoding for binary content |

**Not SDK-relevant** (skip these — they explain existing params or are guides):
- README/overview pages
- `writing-instructions-manually/` — explains existing `parsing_instructions`
- `javascript-rendering.md` — explains existing `render`
- `user-agent-type.md` — explains existing `user_agent_type`
- `domain-locale-results-language.md`, `serp-localization.md`, `e-commerce-localization.md` — explain existing params
- `scheduler.md`, `dedicated-parsers.md` — separate API features, not request params

## Types of Documentation Changes

### 1. Updated Target — Parameter changes on existing methods

A diff modifies an existing target page with new or changed parameters in the request payload.

**What to do:**
1. Find the corresponding SDK source file
2. Add the new parameter to the method signature (both sync and async classes) with `Optional` type and `None` default
3. Add the parameter to the payload dict
4. Add a test verifying the parameter flows through

### 2. New Feature — New methods on an existing source

A diff adds a new `.md` page for a source that already has an SDK class.

**What to do:**
1. Determine if the page describes a new API source or is just a usage guide. Skip usage guides.
2. Add the source constant to `src/oxylabs/utils/types/source.py` if needed
3. Add the new `scrape_<method>` to both sync and async classes in the existing source file
4. Add tests

### 3. New Target — Entirely new source with no SDK class

A diff adds documentation for a target with no SDK class.

**What to do:**
1. Add source constants to `src/oxylabs/utils/types/source.py`
2. Create `src/oxylabs/sources/<target>/__init__.py` and `<target>.py` with sync + async classes
3. Register in `src/oxylabs/internal/client.py` — import and add as attribute on both `RealtimeClient` and `AsyncClient`
4. Create tests in `tests/sources/<target>/test_<target>.py`

### 4. Cross-cutting Feature Change

A diff modifies a file under `features/` that maps to an SDK parameter (see table above).

**What to do:**
1. Identify which parameter changed or was added
2. If it's a new parameter, add it to relevant source methods (check the feature docs for which sources support it)
3. If it applies broadly, add to all source methods that have a payload
4. Add tests

## Code Patterns

### Method signature (sync)
```python
def scrape_search(
    self,
    query: str,                                    # required param
    domain: Optional[str] = None,                  # optional params
    locale: Optional[str] = None,
    geo_location: Optional[str] = None,
    user_agent_type: Optional[str] = None,
    render: Optional[str] = None,
    callback_url: Optional[str] = None,
    context: Optional[list] = None,
    parse: Optional[bool] = None,
    parsing_instructions: Optional[dict] = None,
    request_timeout: Optional[int] = 165,          # always last named param
    **kwargs                                        # always at the end
) -> Response:
    config = prepare_config(request_timeout=request_timeout)
    payload = {
        "source": source.AMAZON_SEARCH,
        "query": query,
        "domain": domain,
        # ... all params ...
        **kwargs,
    }
    check_parsing_instructions_validity(parsing_instructions)
    api_response = self._api_instance.get_response(payload, config)
    return Response(api_response)
```

### Method signature (async)
Same as sync but:
- `async def` and `await`
- Extra params: `job_completion_timeout` and `poll_interval`
- Uses `prepare_config(..., async_integration=True)`

### Test pattern
```python
def test_<method>_<param>(self):
    client = RealtimeClient('user', 'pass')
    api = client.<target>._api_instance
    captured = {}
    api._get_http_response = lambda payload, method, config: (captured.update(payload) or {"mock": True})

    client.<target>.scrape_<method>(<required_arg>, <param>=<value>)

    self.assertEqual(captured["<param>"], <value>)
```

## Important Rules

- Each source file has TWO classes: sync (e.g. `Amazon`) and async (e.g. `AmazonAsync`). Always update both.
- Only care about **payload fields** from the docs — ignore language-specific syntax in code examples.
- If docs have typos in one language but correct spelling in others, use the **correct spelling**.
- Parameters are `Optional[str]` by default unless clearly a different type (int, bool, list, dict).
- `**kwargs` is always last. `request_timeout` (default 165) is always the last named param before `**kwargs`.
- Context params (passed via `context` list) don't need dedicated method arguments.
- `source` is never a method param — it's hardcoded in the payload.
- Code style: `black` with 79-char line length, `isort` for imports.
