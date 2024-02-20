from serp.serp import SerpClient, SerpClientAsync
from serp.bing import Bing


# Initialize the clients
serp_client = SerpClient('username', 'password')
serp_client_async = SerpClientAsync('username', 'password')

# Initialize the search engine classes
bing = Bing(serp_client.client)


# Now we can call the methods to perform the scraping
# For example:
bing.scrape_bing_search()
