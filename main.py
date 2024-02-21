from serp.serp import SerpClient, SerpClientAsync
from serp.bing import Bing


# Initialize the clients
serp_client = SerpClient('hamdan', 'gzR4pHW9eiEM#Ky')


browser = Bing(serp_client)

results = browser.scrape_bing_search('nike')
