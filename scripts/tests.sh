#!/bin/bash

# Run serp tests
python -m unittest tests.sources.serp.test_bing.TestBingSearchSync
python -m unittest tests.sources.serp.test_bing.TestBingSearchAsync
python -m unittest tests.sources.serp.test_bing.TestBingUrlSync
python -m unittest tests.sources.serp.test_bing.TestBingUrlAsync

# Run ecommerce tests
python -m unittest tests.sources.ecommerce.test_wayfair.TestWayfairSearchSync
python -m unittest tests.sources.ecommerce.test_wayfair.TestWayfairSearchAsync
python -m unittest tests.sources.ecommerce.test_wayfair.TestWayfairUrlSync
python -m unittest tests.sources.ecommerce.test_wayfair.TestWayfairUrlAsync

# Run proxy tests
python -m unittest tests.proxy.test_proxy.TestProxyGet
