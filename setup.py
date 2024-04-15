from setuptools import setup, find_packages

def get_version(rel_path):
    with open(rel_path, 'r') as file:
        for line in file.read().splitlines():
            if line.startswith('__version__'):
                delim = '"' if '"' in line else "'"
                return line.split(delim)[1]
        else:
            raise RuntimeError("Unable to find version string.")

long_description = """
The official Python library for the Oxylabs Scraper APIs.

Collect public data at scale with industry-leading web scraping solutions and the world's largest ethical proxy network.
Documentation can be found at https://github.com/mslmio/oxylabs-sdk-python.
"""

setup(
    name="oxylabs",
    version=get_version("oxylabs/version.py"),
    description="Official Python library for Oxylabs Scraper APIs",
    long_description=long_description,
    url="https://oxylabs.io/",
    author="Oxylabs",
    author_email="support@oxylabs.io",
    license="MIT",
    packages=find_packages(),
    install_requires=["aiohttp", "requests"],
)
