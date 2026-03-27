# Changelog
## 3.0.0
  Updated Sources

  | Source | Change |
  |---|---|
  | **Amazon** | Added missing params |
  | **Google** | Added `scrape_ai_mode`, `scrape_news` |
  | **Google Shopping** | Removed deprecated `scrape_product_pricing`
  |
  | **Kroger** | Added `context` param to `scrape_search` |
  | **Universal** | Deprecated `locale` and `parser_type` params |

  New Sources

  **General**
  YouTube (`search`, `metadata`, `channel`, `subtitles`, `transcript`,
   `trainability`, `autocomplete`, `download`†)
   
  youtube_transcript deprecated, use youtube.scrape_transcript instead
   
  eBay, Etsy, TikTok, Shop, ChatGPT, Perplexity

  **North American Retail**
  Walmart, Best Buy, Target, Costco, Lowe's, Menards, Instacart, Bed
  Bath & Beyond, Petco, Grainger, Publix, Staples, Shein, Avnet

  **European**
  Allegro, Cdiscount, Idealo, MediaMarkt

  **Asian**
  Alibaba, AliExpress, Flipkart, IndiaMart, Lazada, Rakuten,
  Tokopedia, Dcard

  **Latin American**
  Mercado Libre, Mercado Livre, Magazine Luiza, Falabella, Bodega
  Aurrera

  **Real Estate**
  Airbnb, Zillow

  - Regional sources reorganized into geographic subdirectories
  (`asian/`, `european/`, `latin_american/`, `north_american/`,
  `real_estate/`)
  - Tests added for all new sources and Universal
  - README updated to reflect all changes


## 2.0.0
- SERP and Ecommerce source split has been removed. New common modules have been created: API, Client and Response.
- Support for new sources has been added: google_maps, google_lens, kroger, kroger_product, kroger_search, youtube_transcript.
- Added browser_instructions parameter for universal source.
- Docs update.

## 1.0.7
- Add an SDK version identifier to all requests.

## 1.0.6

- Security updates in 3rd party libraries.
- Docs update.

## 1.0.5

- Cleaned up tests from obsolete credentials.

## 1.0.4

- Security updates in 3rd party libraries.

## 1.0.3

- Updated import paths to resolve module not found errors.
- Scraper methods now accept direct parameters and include a response object for easier access to results and metadata.
- Replaced print statements with the logging module for better error handling.
- Introduced AsyncClient, RealtimeClient, and ProxyClient to support all sources, providing a more organized structure.

## 1.0.2

- Fixed function and class naming.
- Added request timeout in proxy.
- Removed Yandex and Baidu sources from SERP.

## 1.0.1

- Fixed issue with uploaded package.

## 1.0.0

- Initial release of Oxylabs SDK.
- Scraper APIs:
  - SERP
  - Ecommerce
- Integration methods:
  - Proxy
  - Push-Pull
  - Realtime
