class SERPResponse:
    def __init__(self, data):
        if data is None:
            return
        self.parse = data.get("parse")
        self.parse_instructions = data.get("parse_instructions")
        self.results = [Results(item) for item in data.get("results", [])]
        self.job = Job(data.get("job", {}))
        self.status_code = data.get("status_code")
        self.status = data.get("status")


class Results:
    def __init__(self, data):
        if data is None:
            return
        self.custom_content_parsed = data.get("custom_content_parsed", {})
        self.content_parsed = Content(data.get("content_parsed", {}))
        self.content = data.get("content")
        self.created_at = data.get("created_at")
        self.updated_at = data.get("updated_at")
        self.page = data.get("page")
        self.url = data.get("url")
        self.job_id = data.get("job_id")
        self.status_code = data.get("status_code")
        self.parser_type = data.get("parser_type")


class Content:
    def __init__(self, data):
        if data is None:
            return
        self.url = data.get("url")
        self.page = data.get("page")
        self.errors = data.get("_errors")
        self.results = Result(data.get("results", {}))
        self.last_visible_page = data.get("last_visible_page")
        self.parse_status_code = data.get("parse_status_code")


class Result:
    def __init__(self, data):
        if data is None:
            return
        self.pla = Pla(data.get("pla", {}))
        self.paid = [Paid(item) for item in data.get("paid", [])]
        self.images = Image(data.get("images", {}))
        self.organic = [Organic(item) for item in data.get("organic", [])]
        self.twitter = Twitter(data.get("twitter", {}))
        self.knowledge = Knowledge(data.get("knowledge", {}))
        self.local_pack = LocalPack(data.get("local_pack", {}))
        self.top_stories = TopStory(data.get("top_stories", {}))
        self.popular_products = [
            PopularProducts(item) for item in data.get("popular_products", [])
        ]
        self.related_searches = RelatedSearches(data.get("related_searches", {}))
        self.related_questions = RelatedQuestions(data.get("related_questions", {}))
        self.search_information = SearchInformation(data.get("search_information", {}))
        self.item_carousel = ItemCarousel(data.get("item_carousel", {}))
        self.recipes = Recipes(data.get("recipes", {}))
        self.videos = Videos(data.get("videos", {}))
        self.featured_snippet = [
            FeaturedSnippet(item) for item in data.get("featured_snippet", [])
        ]
        self.related_searches_categorized = [
            RelatedSearchesCategorized(item)
            for item in data.get("related_searches_categorized", [])
        ]
        self.hotels = Hotels(data.get("hotels", {}))
        self.flights = Flights(data.get("flights", {}))
        self.video_box = VideoBox(data.get("video_box", {}))
        self.local_service_ads = LocalServiceAds(data.get("local_service_ads", {}))
        self.navigation = [Navigation(item) for item in data.get("navigation", [])]
        self.instant_answers = [
            InstantAnswers(item) for item in data.get("instant_answers", [])
        ]
        self.visually_similar_images = VisuallySimilarImages(
            data.get("visually_similar_images", {})
        )
        self.total_results_count = data.get("total_results_count")


class Pla:
    def __init__(self, data):
        if data is None:
            return
        self.items = [PlaItem(item) for item in data.get("items", [])]
        self.pos_overall = data.get("pos_overall")


class PlaItem:
    def __init__(self, data):
        if data is None:
            return
        self.pos = data.get("pos")
        self.url = data.get("url")
        self.price = data.get("price")
        self.title = data.get("title")
        self.seller = data.get("seller")
        self.url_image = data.get("url_image")
        self.image_data = data.get("image_data")


class Paid:
    def __init__(self, data):
        if data is None:
            return
        self.pos = data.get("pos")
        self.url = data.get("url")
        self.desc = data.get("desc")
        self.title = data.get("title")
        self.data_rw = data.get("data_rw")
        self.data_pcu = data.get("data_pcu", [])
        self.sitelinks = PaidSitelinks(data.get("sitelinks", {}))
        self.url_shown = data.get("url_shown")
        self.pos_overall = data.get("pos_overall")


class PaidSitelinks:
    def __init__(self, data):
        if data is None:
            return
        self.expanded = [Expanded(item) for item in data.get("expanded", [])]
        self.inline = [Inline(item) for item in data.get("inline", [])]


class Expanded:
    def __init__(self, data):
        if data is None:
            return
        self.url = data.get("url")
        self.desc = data.get("desc")
        self.title = data.get("title")


class Inline:
    def __init__(self, data):
        if data is None:
            return
        self.url = data.get("url")
        self.desc = data.get("desc")
        self.title = data.get("title")


class Image:
    def __init__(self, data):
        if data is None:
            return
        self.items = [ImageItem(item) for item in data.get("items", [])]
        self.pos_overall = data.get("pos_overall")


class ImageItem:
    def __init__(self, data):
        if data is None:
            return
        self.alt = data.get("alt")
        self.pos = data.get("pos")
        self.url = data.get("url")
        self.data = data.get("data")
        self.source = data.get("source")


class Organic:
    def __init__(self, data):
        if data is None:
            return
        self.pos = data.get("pos")
        self.url = data.get("url")
        self.desc = data.get("desc")
        self.title = data.get("title")
        self.images = [item for item in data.get("images", [])]
        self.site_links = OrganicSitelinks(data.get("sitelinks", {}))
        self.url_shown = data.get("url_shown")
        self.pos_overall = data.get("pos_overall")


class OrganicSitelinks:
    def __init__(self, data):
        if data is None:
            return
        self.expanded = [Expanded(item) for item in data.get("expanded", [])]
        self.inline = [Inline(item) for item in data.get("inline", [])]


class Twitter:
    def __init__(self, data):
        if data is None:
            return
        self.pos = data.get("pos")
        self.url = data.get("url")
        self.items = [TwitterItem(item) for item in data.get("items", [])]
        self.title = data.get("title")
        self.pos_overall = data.get("pos_overall")


class TwitterItem:
    def __init__(self, data):
        if data is None:
            return
        self.pos = data.get("pos")
        self.url = data.get("url")
        self.content = data.get("content")
        self.time_frame = data.get("time_frame")


class Knowledge:
    def __init__(self, data):
        if data is None:
            return
        self.title = data.get("title")
        self.images = [item for item in data.get("images", [])]
        self.factoids = [Factoid(item) for item in data.get("factoids", [])]
        self.profiles = [Profile(item) for item in data.get("profiles", [])]
        self.subtitle = data.get("subtitle")
        self.description = data.get("description")
        self.related_searches = [
            RelatedSearches(item) for item in data.get("related_searches", [])
        ]


class Factoid:
    def __init__(self, data):
        if data is None:
            return
        self.links = [LinkElement(item) for item in data.get("links", [])]
        self.title = data.get("title")
        self.content = data.get("content")


class LinkElement:
    def __init__(self, data):
        if data is None:
            return
        self.href = data.get("href")
        self.title = data.get("title")


class Profile:
    def __init__(self, data):
        if data is None:
            return
        self.url = data.get("url")
        self.title = data.get("title")


class RelatedSearches:
    def __init__(self, data):
        if data is None:
            return
        self.url = data.get("url")
        self.title = data.get("title")
        self.section_title = data.get("section_title")


class LocalPack:
    def __init__(self, data):
        if data is None:
            return
        self.items = [LocalPackItem(item) for item in data.get("items", [])]
        self.pos_overall = data.get("pos_overall")


class LocalPackItem:
    def __init__(self, data):
        if data is None:
            return
        self.cid = data.get("cid")
        self.pos = data.get("pos")
        self.links = [LocalPackLink(item) for item in data.get("links", [])]
        self.phone = data.get("phone")
        self.title = data.get("title")
        self.rating = data.get("rating")
        self.address = data.get("address")
        self.subtitle = data.get("subtitle")
        self.rating_count = data.get("rating_count")


class LocalPackLink:
    def __init__(self, data):
        if data is None:
            return
        self.href = data.get("href")
        self.title = data.get("title")


class TopStory:
    def __init__(self, data):
        if data is None:
            return
        self.items = [TopStoryItem(item) for item in data.get("items", [])]
        self.pos_overall = data.get("pos_overall")


class TopStoryItem:
    def __init__(self, data):
        if data is None:
            return
        self.pos = data.get("pos")
        self.url = data.get("url")
        self.title = data.get("title")
        self.source = data.get("source")
        self.time_frame = data.get("time_frame")


class PopularProducts:
    def __init__(self, data):
        if data is None:
            return
        self.pos = data.get("pos")
        self.price = data.get("price")
        self.rating = data.get("rating")
        self.seller = data.get("seller")
        self.title = data.get("title")
        self.image_data = data.get("image_data")


class RelatedSearches:
    def __init__(self, data):
        if data is None:
            return
        self.pos_overall = data.get("pos_overall")
        self.related_searches = [item for item in data.get("related_searches", [])]


class RelatedQuestions:
    def __init__(self, data):
        if data is None:
            return
        self.pos_overall = data.get("pos_overall")
        self.related_questions = [
            RelatedQuestionsItem(item) for item in data.get("related_questions", [])
        ]


class RelatedQuestionsItem:
    def __init__(self, data):
        if data is None:
            return
        self.pos = data.get("pos")
        self.answer = data.get("answer")
        self.source = data.get("source")
        self.question = data.get("question")


class Source:
    def __init__(self, data):
        if data is None:
            return
        self.url = data.get("url")
        self.title = data.get("title")
        self.url_shown = data.get("url_shown")


class SearchInformation:
    def __init__(self, data):
        if data is None:
            return
        self.image = SearchInformationImage(data.get("image", {}))
        self.query = data.get("query")
        self.showing_results_for = data.get("showing_results_for")
        self.total_results_count = data.get("total_results_count")


class SearchInformationImage:
    def __init__(self, data):
        if data is None:
            return
        self.url = data.get("url")
        self.width = data.get("width")
        self.height = data.get("height")
        self.other_sizes = data.get("other_sizes")


class ItemCarousel:
    def __init__(self, data):
        if data is None:
            return
        self.items = [ItemCarouselItem(item) for item in data.get("items", [])]
        self.pos_overall = data.get("pos_overall")
        self.title = data.get("title")


class ItemCarouselItem:
    def __init__(self, data):
        if data is None:
            return
        self.pos = data.get("pos")
        self.href = data.get("href")
        self.title = data.get("title")
        self.subtitle = data.get("subtitle")


class Recipes:
    def __init__(self, data):
        if data is None:
            return
        self.items = [RecipesItem(item) for item in data.get("items", [])]
        self.pos_overall = data.get("pos_overall")


class RecipesItem:
    def __init__(self, data):
        if data is None:
            return
        self.pos = data.get("pos")
        self.url = data.get("url")
        self.title = data.get("title")
        self.rating = data.get("rating")
        self.source = data.get("source")
        self.duration = data.get("duration")


class Videos:
    def __init__(self, data):
        if data is None:
            return
        self.items = [VideosItem(item) for item in data.get("items", [])]
        self.pos_overall = data.get("pos_overall")


class VideosItem:
    def __init__(self, data):
        if data is None:
            return
        self.pos = data.get("pos")
        self.url = data.get("url")
        self.title = data.get("title")
        self.author = data.get("author")
        self.source = data.get("source")


class FeaturedSnippet:
    def __init__(self, data):
        if data is None:
            return
        self.url = data.get("url")
        self.desc = data.get("desc")
        self.title = data.get("title")
        self.url_shown = data.get("url_shown")
        self.pos_overall = data.get("pos_overall")


class RelatedSearchesCategorized:
    def __init__(self, data):
        if data is None:
            return
        self.items = [
            RelatedSearchesCategorizedItem(item) for item in data.get("items", [])
        ]
        self.category = data.get("category")
        self.pos_overall = data.get("pos_overall")


class RelatedSearchesCategorizedItem:
    def __init__(self, data):
        if data is None:
            return
        self.url = data.get("url")
        self.title = data.get("title")


class Category:
    def __init__(self, data):
        if data is None:
            return
        self.name = data.get("name")
        self.type = data.get("type")


class Hotels:
    def __init__(self, data):
        if data is None:
            return
        self.date_to = data.get("date_to")
        self.results = [HotelsResult(item) for item in data.get("results", [])]
        self.date_from = data.get("date_from")
        self.pos_overall = data.get("pos_overall")


class HotelsResult:
    def __init__(self, data):
        if data is None:
            return
        self.price = data.get("price")
        self.title = data.get("title")
        self.from_location = data.get("from")


class Flights:
    def __init__(self, data):
        if data is None:
            return
        self.to = data.get("to")
        self.from_location = data.get("from")
        self.results = [FlightsResult(item) for item in data.get("results", [])]
        self.date_from = data.get("date_from")
        self.pos_overall = data.get("pos_overall")


class FlightsResult:
    def __init__(self, data):
        if data is None:
            return
        self.url = data.get("url")
        self.type = data.get("type")
        self.price = data.get("price")
        self.airline = data.get("airline")
        self.duration = data.get("duration")


class VideoBox:
    def __init__(self, data):
        if data is None:
            return
        self.url = data.get("url")
        self.title = data.get("title")
        self.pos_overall = data.get("pos_overall")


class LocalServiceAds:
    def __init__(self, data):
        if data is None:
            return
        self.pos_overall = data.get("pos_overall")
        self.items = [LocalServiceAdsItem(item) for item in data.get("items", [])]


class LocalServiceAdsItem:
    def __init__(self, data):
        if data is None:
            return
        self.pos = data.get("pos")
        self.url = data.get("url")
        self.title = data.get("title")
        self.rating = data.get("rating")
        self.reviews_count = data.get("reviews_count")
        self.google_gauranteed = data.get("google_gauranteed")


class Navigation:
    def __init__(self, data):
        if data is None:
            return
        self.url = data.get("url")
        self.title = data.get("title")
        self.pos = data.get("pos")


class InstantAnswers:
    def __init__(self, data):
        if data is None:
            return
        self.type = data.get("type")
        self.parsed = data.get("_parsed")
        self.pos_overall = data.get("pos_overall")


class VisuallySimilarImages:
    def __init__(self, data):
        if data is None:
            return
        self.all_images_url = data.get("all_images_url")
        self.featured_images = data.get("featured_images")


class Job:
    def __init__(self, data):
        if data is None:
            return
        self.callback_url = data.get("callback_url")
        self.client_id = data.get("client_id")
        self.context = [Context(item) for item in data.get("context", [])]
        self.created_at = data.get("created_at")
        self.domain = data.get("domain")
        self.geo_location = data.get("geo_location")
        self.id = data.get("id")
        self.limit = data.get("limit")
        self.locale = data.get("locale")
        self.pages = data.get("pages")
        self.parse = data.get("parse")
        self.parser_type = data.get("parser_type")
        self.parsing_instructions = data.get("parsing_instructions")
        self.browser_instructions = data.get("browser_instructions")
        self.render = data.get("render")
        self.url = data.get("url")
        self.query = data.get("query")
        self.source = data.get("source")
        self.start_page = data.get("start_page")
        self.status = data.get("status")
        self.storage_type = data.get("storage_type")
        self.storage_url = data.get("storage_url")
        self.subdomain = data.get("subdomain")
        self.content_encoding = data.get("content_encoding")
        self.updated_at = data.get("updated_at")
        self.user_agent_type = data.get("user_agent_type")
        self.session_info = data.get("session_info")
        self.statuses = data.get("statuses")
        self.client_notes = data.get("client_notes")
        self.links = [JobLink(item) for item in data.get("links", [])]


class Context:
    def __init__(self, data):
        if data is None:
            return
        self.key = data.get("key")
        self.value = data.get("value")


class JobLink:
    def __init__(self, data):
        if data is None:
            return
        self.rel = data.get("rel")
        self.href = data.get("href")
        self.method = data.get("method")
