#!/bin/bash

# Run source tests
python -m unittest tests.sources.bing.test_bing.TestBingSearchSync
python -m unittest tests.sources.bing.test_bing.TestBingSearchAsync
python -m unittest tests.sources.bing.test_bing.TestBingUrlSync
python -m unittest tests.sources.bing.test_bing.TestBingUrlAsync

python -m unittest tests.sources.wayfair.test_wayfair.TestWayfairSearchSync
python -m unittest tests.sources.wayfair.test_wayfair.TestWayfairSearchAsync
python -m unittest tests.sources.wayfair.test_wayfair.TestWayfairUrlSync
python -m unittest tests.sources.wayfair.test_wayfair.TestWayfairUrlAsync

# Run proxy tests
python -m unittest tests.proxy.test_proxy.TestProxyGet
