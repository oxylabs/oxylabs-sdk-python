import logging
from oxylabs.internal.api import APICredentials, RealtimeAPI, AsyncAPI
from oxylabs.sources.amazon import Amazon, AmazonAsync
from oxylabs.sources.bing import Bing, BingAsync
from oxylabs.sources.google import Google, GoogleAsync
from oxylabs.sources.google_shopping import GoogleShopping, GoogleShoppingAsync
from oxylabs.sources.kroger import Kroger, KrogerAsync
from oxylabs.sources.universal import Universal, UniversalAsync
from oxylabs.sources.wayfair import Wayfair, WayfairAsync
from oxylabs.sources.youtube_transcript import YoutubeTranscript, YoutubeTranscriptAsync

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class RealtimeClient:
    def __init__(self, username: str, password: str, **kwargs) -> None:
        """
        Initializes an instance of the RealtimeClient class.

        Args:
            username (str): The username for API authentication.
            password (str): The password for API authentication.
        """
        api = RealtimeAPI(APICredentials(username, password), **kwargs)
        self.amazon = Amazon(api)
        self.bing = Bing(api)
        self.google = Google(api)
        self.google_shopping = GoogleShopping(api)
        self.kroger = Kroger(api)
        self.universal = Universal(api)
        self.wayfair = Wayfair(api)
        self.youtube_transcript = YoutubeTranscript(api)

class AsyncClient:
    def __init__(self, username: str, password: str, **kwargs) -> None:
        """
        Initializes an instance of the AsyncClient class.

        Args:
            username (str): The username for API authentication.
            password (str): The password for API authentication.
        """
        api = AsyncAPI(APICredentials(username, password), **kwargs)
        self.amazon = AmazonAsync(api)
        self.bing = BingAsync(api)
        self.google = GoogleAsync(api)
        self.google_shopping = GoogleShoppingAsync(api)
        self.kroger = KrogerAsync(api)
        self.universal = UniversalAsync(api)
        self.wayfair = WayfairAsync(api)
        self.youtube_transcript = YoutubeTranscriptAsync(api)


