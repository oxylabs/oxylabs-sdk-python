import logging
from oxylabs.internal.api import APICredentials, RealtimeAPI, AsyncAPI
from oxylabs.sources.real_estate.airbnb import Airbnb, AirbnbAsync
from oxylabs.sources.real_estate.zillow import Zillow, ZillowAsync
from oxylabs.sources.amazon import Amazon, AmazonAsync
from oxylabs.sources.asian.alibaba import Alibaba, AlibabaAsync
from oxylabs.sources.asian.aliexpress import Aliexpress, AliexpressAsync
from oxylabs.sources.asian.avnet import Avnet, AvnetAsync
from oxylabs.sources.asian.flipkart import Flipkart, FlipkartAsync
from oxylabs.sources.asian.indiamart import Indiamart, IndiamartAsync
from oxylabs.sources.asian.lazada import Lazada, LazadaAsync
from oxylabs.sources.asian.rakuten import Rakuten, RakutenAsync
from oxylabs.sources.asian.tokopedia import Tokopedia, TokopediaAsync
from oxylabs.sources.bing import Bing, BingAsync
from oxylabs.sources.north_american.bedbathandbeyond import Bedbathandbeyond, BedbathandbeyondAsync
from oxylabs.sources.north_american.bestbuy import Bestbuy, BestbuyAsync
from oxylabs.sources.north_american.bodegaaurrera import Bodegaaurrera, BodegaaurreraAsync
from oxylabs.sources.north_american.costco import Costco, CostcoAsync
from oxylabs.sources.north_american.grainger import Grainger, GraingerAsync
from oxylabs.sources.north_american.instacart import Instacart, InstacartAsync
from oxylabs.sources.north_american.lowes import Lowes, LowesAsync
from oxylabs.sources.north_american.menards import Menards, MenardsAsync
from oxylabs.sources.north_american.petco import Petco, PetcoAsync
from oxylabs.sources.north_american.publix import Publix, PublixAsync
from oxylabs.sources.north_american.target_store import TargetStore, TargetStoreAsync
from oxylabs.sources.european.allegro import Allegro, AllegroAsync
from oxylabs.sources.european.cdiscount import Cdiscount, CdiscountAsync
from oxylabs.sources.european.idealo import Idealo, IdealoAsync
from oxylabs.sources.european.mediamarkt import Mediamarkt, MediamarktAsync
from oxylabs.sources.chatgpt import Chatgpt, ChatgptAsync
from oxylabs.sources.latin_american.dcard import Dcard, DcardAsync
from oxylabs.sources.ebay import Ebay, EbayAsync
from oxylabs.sources.etsy import Etsy, EtsyAsync
from oxylabs.sources.google import Google, GoogleAsync
from oxylabs.sources.google_shopping import GoogleShopping, GoogleShoppingAsync
from oxylabs.sources.kroger import Kroger, KrogerAsync
from oxylabs.sources.perplexity import Perplexity, PerplexityAsync
from oxylabs.sources.asian.shein import Shein, SheinAsync
from oxylabs.sources.north_american.staples import Staples, StaplesAsync
from oxylabs.sources.north_american.walmart import Walmart, WalmartAsync
from oxylabs.sources.latin_american.falabella import Falabella, FalabellaAsync
from oxylabs.sources.latin_american.mercadolibre import Mercadolibre, MercadolibreAsync
from oxylabs.sources.latin_american.mercadolivre import Mercadolivre, MercadolivreAsync
from oxylabs.sources.latin_american.magazineluiza import Magazineluiza, MagazineluizaAsync
from oxylabs.sources.tiktok import Tiktok, TiktokAsync
from oxylabs.sources.universal import Universal, UniversalAsync
from oxylabs.sources.wayfair import Wayfair, WayfairAsync
from oxylabs.sources.youtube import Youtube, YoutubeAsync

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
        self.airbnb = Airbnb(api)
        self.alibaba = Alibaba(api)
        self.aliexpress = Aliexpress(api)
        self.allegro = Allegro(api)
        self.amazon = Amazon(api)
        self.avnet = Avnet(api)
        self.bedbathandbeyond = Bedbathandbeyond(api)
        self.bestbuy = Bestbuy(api)
        self.bodegaaurrera = Bodegaaurrera(api)
        self.bing = Bing(api)
        self.cdiscount = Cdiscount(api)
        self.chatgpt = Chatgpt(api)
        self.costco = Costco(api)
        self.dcard = Dcard(api)
        self.ebay = Ebay(api)
        self.etsy = Etsy(api)
        self.falabella = Falabella(api)
        self.flipkart = Flipkart(api)
        self.indiamart = Indiamart(api)
        self.lazada = Lazada(api)
        self.rakuten = Rakuten(api)
        self.tokopedia = Tokopedia(api)
        self.google = Google(api)
        self.google_shopping = GoogleShopping(api)
        self.grainger = Grainger(api)
        self.idealo = Idealo(api)
        self.instacart = Instacart(api)
        self.kroger = Kroger(api)
        self.lowes = Lowes(api)
        self.mediamarkt = Mediamarkt(api)
        self.menards = Menards(api)
        self.mercadolibre = Mercadolibre(api)
        self.mercadolivre = Mercadolivre(api)
        self.magazineluiza = Magazineluiza(api)
        self.petco = Petco(api)
        self.publix = Publix(api)
        self.target_store = TargetStore(api)
        self.perplexity = Perplexity(api)
        self.shein = Shein(api)
        self.staples = Staples(api)
        self.tiktok = Tiktok(api)
        self.universal = Universal(api)
        self.wayfair = Wayfair(api)
        self.walmart = Walmart(api)
        self.youtube = Youtube(api)
        self.zillow = Zillow(api)

class AsyncClient:
    def __init__(self, username: str, password: str, **kwargs) -> None:
        """
        Initializes an instance of the AsyncClient class.

        Args:
            username (str): The username for API authentication.
            password (str): The password for API authentication.
        """
        api = AsyncAPI(APICredentials(username, password), **kwargs)
        self.airbnb = AirbnbAsync(api)
        self.alibaba = AlibabaAsync(api)
        self.aliexpress = AliexpressAsync(api)
        self.allegro = AllegroAsync(api)
        self.amazon = AmazonAsync(api)
        self.avnet = AvnetAsync(api)
        self.bedbathandbeyond = BedbathandbeyondAsync(api)
        self.bestbuy = BestbuyAsync(api)
        self.bodegaaurrera = BodegaaurreraAsync(api)
        self.bing = BingAsync(api)
        self.cdiscount = CdiscountAsync(api)
        self.chatgpt = ChatgptAsync(api)
        self.costco = CostcoAsync(api)
        self.dcard = DcardAsync(api)
        self.ebay = EbayAsync(api)
        self.etsy = EtsyAsync(api)
        self.falabella = FalabellaAsync(api)
        self.flipkart = FlipkartAsync(api)
        self.indiamart = IndiamartAsync(api)
        self.lazada = LazadaAsync(api)
        self.rakuten = RakutenAsync(api)
        self.tokopedia = TokopediaAsync(api)
        self.google = GoogleAsync(api)
        self.google_shopping = GoogleShoppingAsync(api)
        self.grainger = GraingerAsync(api)
        self.idealo = IdealoAsync(api)
        self.instacart = InstacartAsync(api)
        self.kroger = KrogerAsync(api)
        self.lowes = LowesAsync(api)
        self.mediamarkt = MediamarktAsync(api)
        self.menards = MenardsAsync(api)
        self.mercadolibre = MercadolibreAsync(api)
        self.mercadolivre = MercadolivreAsync(api)
        self.magazineluiza = MagazineluizaAsync(api)
        self.petco = PetcoAsync(api)
        self.publix = PublixAsync(api)
        self.target_store = TargetStoreAsync(api)
        self.perplexity = PerplexityAsync(api)
        self.shein = SheinAsync(api)
        self.staples = StaplesAsync(api)
        self.tiktok = TiktokAsync(api)
        self.universal = UniversalAsync(api)
        self.wayfair = WayfairAsync(api)
        self.walmart = WalmartAsync(api)
        self.youtube = YoutubeAsync(api)
        self.zillow = ZillowAsync(api)


