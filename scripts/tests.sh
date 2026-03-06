#!/bin/bash

# Run source tests
python -m unittest tests.sources.amazon.test_amazon.TestAmazonSearchParams
python -m unittest tests.sources.amazon.test_amazon.TestAmazonUrlParams
python -m unittest tests.sources.amazon.test_amazon.TestAmazonProductParams
python -m unittest tests.sources.amazon.test_amazon.TestAmazonPricingParams
python -m unittest tests.sources.amazon.test_amazon.TestAmazonBestsellersParams
python -m unittest tests.sources.amazon.test_amazon.TestAmazonSellersParams

python -m unittest tests.sources.bing.test_bing.TestBingSearchSync
python -m unittest tests.sources.bing.test_bing.TestBingUrlSync
python -m unittest tests.sources.bing.test_bing.TestBingSearchAsync
python -m unittest tests.sources.bing.test_bing.TestBingUrlAsync

python -m unittest tests.sources.google.test_google.TestGoogleAiModeSync
python -m unittest tests.sources.google.test_google.TestGoogleNewsSync

python -m unittest tests.sources.google_shopping.test_google_shopping.TestGoogleShoppingSearchSync
python -m unittest tests.sources.google_shopping.test_google_shopping.TestGoogleShoppingUrlSync
python -m unittest tests.sources.google_shopping.test_google_shopping.TestGoogleShoppingProductsSync
python -m unittest tests.sources.google_shopping.test_google_shopping.TestGoogleShoppingPricingRemoved

python -m unittest tests.sources.universal.test_universal.TestUniversalUrlSync

python -m unittest tests.sources.ebay.test_ebay.TestEbaySearchSync
python -m unittest tests.sources.ebay.test_ebay.TestEbayProductSync
python -m unittest tests.sources.ebay.test_ebay.TestEbayUrlSync

python -m unittest tests.sources.etsy.test_etsy.TestEtsySearchSync
python -m unittest tests.sources.etsy.test_etsy.TestEtsyProductSync
python -m unittest tests.sources.etsy.test_etsy.TestEtsyUrlSync

python -m unittest tests.sources.tiktok.test_tiktok.TestTiktokShopSearchSync
python -m unittest tests.sources.tiktok.test_tiktok.TestTiktokShopProductSync
python -m unittest tests.sources.tiktok.test_tiktok.TestTiktokShopUrlSync

python -m unittest tests.sources.chatgpt.test_chatgpt.TestChatgptSync

python -m unittest tests.sources.perplexity.test_perplexity.TestPerplexitySync

python -m unittest tests.sources.youtube.test_youtube.TestYoutubeTranscriptSync
python -m unittest tests.sources.youtube.test_youtube.TestYoutubeSearchSync
python -m unittest tests.sources.youtube.test_youtube.TestYoutubeSearchMaxSync
python -m unittest tests.sources.youtube.test_youtube.TestYoutubeMetadataSync
python -m unittest tests.sources.youtube.test_youtube.TestYoutubeChannelSync
python -m unittest tests.sources.youtube.test_youtube.TestYoutubeSubtitlesSync
python -m unittest tests.sources.youtube.test_youtube.TestYoutubeVideoTrainabilitySync
python -m unittest tests.sources.youtube.test_youtube.TestYoutubeAutocompleteSync
python -m unittest tests.sources.youtube.test_youtube.TestYoutubeDownloadAsync

python -m unittest tests.sources.wayfair.test_wayfair.TestWayfairSearchSync
python -m unittest tests.sources.wayfair.test_wayfair.TestWayfairUrlSync
python -m unittest tests.sources.wayfair.test_wayfair.TestWayfairSearchAsync
python -m unittest tests.sources.wayfair.test_wayfair.TestWayfairUrlAsync

python -m unittest tests.sources.kroger.test_kroger.TestKrogerSearchSync
python -m unittest tests.sources.kroger.test_kroger.TestKrogerProductSync
python -m unittest tests.sources.kroger.test_kroger.TestKrogerUrlSync

python -m unittest tests.sources.walmart.test_walmart.TestWalmartSearchSync
python -m unittest tests.sources.walmart.test_walmart.TestWalmartProductSync
python -m unittest tests.sources.walmart.test_walmart.TestWalmartUrlSync

python -m unittest tests.sources.target_store.test_target_store.TestTargetStoreSearchSync
python -m unittest tests.sources.target_store.test_target_store.TestTargetStoreProductSync
python -m unittest tests.sources.target_store.test_target_store.TestTargetStoreCategorySync
python -m unittest tests.sources.target_store.test_target_store.TestTargetStoreUrlSync

python -m unittest tests.sources.bestbuy.test_bestbuy.TestBestbuySearchSync
python -m unittest tests.sources.bestbuy.test_bestbuy.TestBestbuyProductSync

python -m unittest tests.sources.costco.test_costco.TestCostcoSearchSync
python -m unittest tests.sources.costco.test_costco.TestCostcoProductSync
python -m unittest tests.sources.costco.test_costco.TestCostcoUrlSync

python -m unittest tests.sources.instacart.test_instacart.TestInstacartSearchSync
python -m unittest tests.sources.instacart.test_instacart.TestInstacartProductSync
python -m unittest tests.sources.instacart.test_instacart.TestInstacartUrlSync

python -m unittest tests.sources.lowes.test_lowes.TestLowesSearchSync
python -m unittest tests.sources.lowes.test_lowes.TestLowesProductSync
python -m unittest tests.sources.lowes.test_lowes.TestLowesUrlSync

python -m unittest tests.sources.menards.test_menards.TestMenardsSearchSync
python -m unittest tests.sources.menards.test_menards.TestMenardsProductSync
python -m unittest tests.sources.menards.test_menards.TestMenardsUrlSync

python -m unittest tests.sources.petco.test_petco.TestPetcoSearchSync
python -m unittest tests.sources.petco.test_petco.TestPetcoUrlSync

python -m unittest tests.sources.publix.test_publix.TestPublixSearchSync
python -m unittest tests.sources.publix.test_publix.TestPublixProductSync
python -m unittest tests.sources.publix.test_publix.TestPublixUrlSync

python -m unittest tests.sources.staples.test_staples.TestStaplesSearchSync

python -m unittest tests.sources.bedbathandbeyond.test_bedbathandbeyond.TestBedbathandbeyondSearchSync
python -m unittest tests.sources.bedbathandbeyond.test_bedbathandbeyond.TestBedbathandbeyondProductSync
python -m unittest tests.sources.bedbathandbeyond.test_bedbathandbeyond.TestBedbathandbeyondUrlSync

python -m unittest tests.sources.bodegaaurrera.test_bodegaaurrera.TestBodegaaurrerapSearchSync
python -m unittest tests.sources.bodegaaurrera.test_bodegaaurrera.TestBodegaaurreraProductSync
python -m unittest tests.sources.bodegaaurrera.test_bodegaaurrera.TestBodegaaurreraUrlSync

python -m unittest tests.sources.grainger.test_grainger.TestGraingerSearchSync
python -m unittest tests.sources.grainger.test_grainger.TestGraingerProductSync
python -m unittest tests.sources.grainger.test_grainger.TestGraingerUrlSync

python -m unittest tests.sources.alibaba.test_alibaba.TestAlibabaSearchSync
python -m unittest tests.sources.alibaba.test_alibaba.TestAlibabaProductSync
python -m unittest tests.sources.alibaba.test_alibaba.TestAlibabaUrlSync

python -m unittest tests.sources.aliexpress.test_aliexpress.TestAliexpressSearchSync
python -m unittest tests.sources.aliexpress.test_aliexpress.TestAliexpressProductSync
python -m unittest tests.sources.aliexpress.test_aliexpress.TestAliexpressUrlSync

python -m unittest tests.sources.avnet.test_avnet.TestAvnetSearchSync

python -m unittest tests.sources.flipkart.test_flipkart.TestFlipkartSearchSync
python -m unittest tests.sources.flipkart.test_flipkart.TestFlipkartProductSync
python -m unittest tests.sources.flipkart.test_flipkart.TestFlipkartUrlSync

python -m unittest tests.sources.indiamart.test_indiamart.TestIndiamartSearchSync
python -m unittest tests.sources.indiamart.test_indiamart.TestIndiamartProductSync
python -m unittest tests.sources.indiamart.test_indiamart.TestIndiamartUrlSync

python -m unittest tests.sources.lazada.test_lazada.TestLazadaSearchSync
python -m unittest tests.sources.lazada.test_lazada.TestLazadaProductSync
python -m unittest tests.sources.lazada.test_lazada.TestLazadaUrlSync

python -m unittest tests.sources.rakuten.test_rakuten.TestRakutenSearchSync
python -m unittest tests.sources.rakuten.test_rakuten.TestRakutenUrlSync

python -m unittest tests.sources.shein.test_shein.TestSheinSearchSync

python -m unittest tests.sources.tokopedia.test_tokopedia.TestTokopediaSearchSync
python -m unittest tests.sources.tokopedia.test_tokopedia.TestTokopediaUrlSync

python -m unittest tests.sources.allegro.test_allegro.TestAllegroSearchSync
python -m unittest tests.sources.allegro.test_allegro.TestAllegroProductSync

python -m unittest tests.sources.cdiscount.test_cdiscount.TestCdiscountSearchSync
python -m unittest tests.sources.cdiscount.test_cdiscount.TestCdiscountProductSync
python -m unittest tests.sources.cdiscount.test_cdiscount.TestCdiscountUrlSync

python -m unittest tests.sources.idealo.test_idealo.TestIdealoSearchSync

python -m unittest tests.sources.mediamarkt.test_mediamarkt.TestMediamarktSearchSync
python -m unittest tests.sources.mediamarkt.test_mediamarkt.TestMediamarktProductSync
python -m unittest tests.sources.mediamarkt.test_mediamarkt.TestMediamarktUrlSync

python -m unittest tests.sources.dcard.test_dcard.TestDcardSearchSync

python -m unittest tests.sources.falabella.test_falabella.TestFalabellaSearchSync
python -m unittest tests.sources.falabella.test_falabella.TestFalabellaProductSync
python -m unittest tests.sources.falabella.test_falabella.TestFalabellaUrlSync

python -m unittest tests.sources.magazineluiza.test_magazineluiza.TestMagazineluizaSearchSync
python -m unittest tests.sources.magazineluiza.test_magazineluiza.TestMagazineluizaProductSync
python -m unittest tests.sources.magazineluiza.test_magazineluiza.TestMagazineluizaUrlSync

python -m unittest tests.sources.mercadolibre.test_mercadolibre.TestMercadolibreSearchSync
python -m unittest tests.sources.mercadolibre.test_mercadolibre.TestMercadolibreProductSync
python -m unittest tests.sources.mercadolibre.test_mercadolibre.TestMercadolibreUrlSync

python -m unittest tests.sources.mercadolivre.test_mercadolivre.TestMercadolivreSearchSync
python -m unittest tests.sources.mercadolivre.test_mercadolivre.TestMercadolivreProductSync

python -m unittest tests.sources.airbnb.test_airbnb.TestAirbnbProductSync
python -m unittest tests.sources.airbnb.test_airbnb.TestAirbnbUrlSync

python -m unittest tests.sources.zillow.test_zillow.TestZillowUrlSync

# Run proxy tests
python -m unittest tests.proxy.test_proxy.TestProxyGet
