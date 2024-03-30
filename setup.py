from setuptools import setup

from oxylabs.version import SDK_VERSION

long_description = """
The official Python library for the Oxylabs Scraper APIs.

Collect public data at scale with industry-leading web scraping solutions and the world's largest ethical proxy network.
Documentation can be found at [https://github.com/mslmio/oxylabs-sdk-python](https://github.com/mslmio/oxylabs-sdk-python).
"""

setup(
    name="oxylabs",
    version=SDK_VERSION,
    description="Official Python library for Oxylabs Scraper APIs",
    long_description=long_description,
    url="https://oxylabs.io/",
    author="Oxylabs",
    author_email="support@oxylabs.io",
    license="MIT",
    packages=["oxylabs"],
    install_requires=["aiohttp", "requests"],
)
