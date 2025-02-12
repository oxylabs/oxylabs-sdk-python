
class Response:
    def __init__(self, data):
        if data is None:
            data = {}
        self.raw = data
        self.results = [Results(item) for item in data.get("results", [])]
        self.job = Job(data.get("job", {}))


class Results:
    def __init__(self, data):
        if data is None:
            data = {}
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
            data = {}
        self.raw = data
        self.url = data.get("url")
        self.title = data.get("title")
        self.pages = data.get("pages")
        self.query = data.get("query")
        self.images = data.get("images")
        self.variants = Variants(data.get("variants", {}))
        self.highlights = data.get("highlights", [])
        self.description = data.get("description")
        self.related_items = RelatedItems(data.get("related_items", {}))
        self.specifications = Specifications(data.get("specifications", {}))
        self.page = data.get("page")
        self.errors = data.get("_errors")
        self.results = Result(data.get("results", {}))
        self.rating = data.get("rating")
        self.pricing = [Pricing(item) for item in data.get("pricing", [])]
        self.ads = [AmazonProductAds(item) for item in data.get("ads", [])]
        self.asin = data.get("asin")
        self.price = data.get("price")
        self.stock = data.get("stock")
        self.coupon = data.get("coupon")
        self.category = [
            AmazonProductCategory(item) for item in data.get("category", [])
        ]
        self.currency = data.get("currency")
        self.delivery = [
            AmazonProductDelivery(item) for item in data.get("delivery", [])
        ]
        self.warnings = data.get("_warnings", [])
        self.deal_type = data.get("deal_type")
        self.page_type = data.get("page_type")
        self.price_sns = data.get("price_sns")
        self.variation = data.get("variation")
        self.has_videos = data.get("has_videos")
        self.sales_rank = [
            AmazonProductSalesRank(item) for item in data.get("sales_rank", [])
        ]
        self.top_review = data.get("top_review")
        self.asin_in_url = data.get("asin_in_url")
        self.price_upper = data.get("price_upper")
        self.pricing_str = data.get("pricing_str")
        self.pricing_url = data.get("pricing_url")
        self.discount_end = data.get("discount_end")
        self.manufacturer = data.get("manufacturer")
        self.max_quantity = data.get("max_quantity")
        self.price_buybox = data.get("price_buybox")
        self.product_name = data.get("product_name")
        self.bullet_points = data.get("bullet_points")
        self.is_addon_item = data.get("is_addon_item")
        self.price_initial = data.get("price_initial")
        self.pricing_count = data.get("pricing_count")
        self.reviews_count = data.get("reviews_count")
        self.sns_discounts = data.get("sns_discounts", [])
        self.developer_info = data.get("developer_info", [])
        self.lightning_deal = data.get("lightning_deal")
        self.price_shipping = data.get("price_shipping")
        self.is_prime_pantry = data.get("is_prime_pantry")
        self.product_details = ProductDetails(data.get("product_details", {}))
        self.featured_merchant = data.get("featured_merchant", [])
        self.is_prime_eligible = data.get("is_prime_eligible")
        self.product_dimensions = data.get("product_dimensions")
        self.refurbished_product = AmazonRefurbishedProduct(
            data.get("refurbished_product", {})
        )
        self.answered_questions_count = data.get("answered_questions_count")
        self.rating_star_distribution = [
            AmazonRatingStarDistribution(item)
            for item in data.get("rating_star_distribution", [])
        ]
        self.reviews = [
            AmazonReviews(item) for item in data.get("reviews", [])
        ]
        self.questions = AmazonQuestions(data.get("questions", {}))
        self.questions_total = data.get("questions_total")
        self.business_name = data.get("business_name")
        self.recent_feedback = [
            RecentFeedback(item) for item in data.get("recent_feedback", [])
        ]
        self.business_address = data.get("business_address")
        self.feedback_summary_table = FeedbackSummaryTable(
            data.get("feedback_summary_table", {})
        )
        self.review_count = data.get("review_count")
        self.last_visible_page = data.get("last_visible_page")
        self.parse_status_code = data.get("parse_status_code")


class Result:
    def __init__(self, data):
        if data is None:
            data = {}
        self.raw = data
        self.paid = [Paid(item) for item in data.get("paid", [])]
        self.filters = [Filters(item) for item in data.get("filters", [])]
        self.search_information = SearchInformation(
            data.get("search_information")
        )
        self.suggested = [
            SuggestedAmazonSearch(item) for item in data.get("suggested", [])
        ]
        self.amazon_choices = [
            AmazonChoices(item) for item in data.get("amazon_choices", [])
        ]
        self.instant_recommendations = [
            InstantRecommendations(item)
            for item in data.get("instant_recommendations", [])
        ]
        self.pos = data.get("pos")
        self.url = data.get("url")
        self.asin = data.get("asin")
        self.price = data.get("price")
        self.title = data.get("title")
        self.rating = data.get("rating")
        self.currency = data.get("currency")
        self.is_prime = data.get("is_prime")
        self.price_str = data.get("price_str")
        self.price_upper = data.get("price_upper")
        self.ratings_count = data.get("ratings_count")
        self.pla = Pla(data.get("pla", {}))
        self.images = Image(data.get("images", {}))
        self.twitter = Twitter(data.get("twitter", {}))
        self.knowledge = Knowledge(data.get("knowledge", {}))
        self.local_pack = LocalPack(data.get("local_pack", {}))
        self.top_stories = TopStory(data.get("top_stories", {}))
        self.popular_products = [
            PopularProducts(item) for item in data.get("popular_products", [])
        ]
        self.related_searches = RelatedSearches(
            data.get("related_searches", {})
        )
        self.related_questions = RelatedQuestions(
            data.get("related_questions", {})
        )
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
        self.local_service_ads = LocalServiceAds(
            data.get("local_service_ads", {})
        )
        self.navigation = [
            Navigation(item) for item in data.get("navigation", [])
        ]
        self.instant_answers = [
            InstantAnswers(item) for item in data.get("instant_answers", [])
        ]
        self.visually_similar_images = VisuallySimilarImages(
            data.get("visually_similar_images", {})
        )
        self.total_results_count = data.get("total_results_count")


class Paid:
    def __init__(self, data):
        if data is None:
            data = {}
        self.raw = data
        self.pos = data.get("pos")
        self.url = data.get("url")
        self.desc = data.get("desc")
        self.title = data.get("title")
        self.data_rw = data.get("data_rw")
        self.data_pcu = data.get("data_pcu")
        self.sitelinks = PaidSitelinks(data.get("sitelinks", {}))
        self.url_shown = data.get("url_shown")
        self.asin = data.get("asin")
        self.price = data.get("price")
        self.rating = data.get("rating")
        self.rel_pos = data.get("rel_pos")
        self.currency = data.get("currency")
        self.url_image = data.get("url_image")
        self.best_seller = data.get("best_seller")
        self.price_upper = data.get("price_upper")
        self.is_sponsored = data.get("is_sponsored")
        self.manufacturer = data.get("manufacturer")
        self.pricing_count = data.get("pricing_count")
        self.reviews_count = data.get("reviews_count")
        self.is_amazons_choice = data.get("is_amazons_choice")
        self.no_price_reason = data.get("no_price_reason")
        self.sales_volume = data.get("sales_volume")
        self.is_prime = data.get("is_prime")
        self.shipping_information = data.get("shipping_information")
        self.pos_overall = data.get("pos_overall")


class PaidSitelinks:
    def __init__(self, data):
        if data is None:
            data = {}
        self.raw = data
        self.expanded = [Expanded(item) for item in data.get("expanded", [])]
        self.inline = [Inline(item) for item in data.get("inline", [])]


class Expanded:
    def __init__(self, data):
        if data is None:
            data = {}
        self.raw = data
        self.url = data.get("url")
        self.desc = data.get("desc")
        self.title = data.get("title")


class Inline:
    def __init__(self, data):
        if data is None:
            data = {}
        self.raw = data
        self.url = data.get("url")
        self.desc = data.get("desc")
        self.title = data.get("title")


class Filters:
    def __init__(self, data):
        if data is None:
            data = {}
        self.raw = data
        self.name = data.get("name")
        self.values = [FilterValues(item) for item in data.get("values", [])]


class FilterValues:
    def __init__(self, data):
        if data is None:
            data = {}
        self.raw = data
        self.url = data.get("url")
        self.value = data.get("value")


class Organic:
    def __init__(self, data):
        if data is None:
            data = {}
        self.raw = data
        self.pos = data.get("pos")
        self.url = data.get("url")
        self.desc = data.get("desc")
        self.type = data.get("type")
        self.price = data.get("price")
        self.title = data.get("title")
        self.currency = data.get("currency")
        self.merchant = Merchant(data.get("merchant", {}))
        self.price_str = data.get("price_str")
        self.product_id = data.get("product_id")
        self.asin = data.get("asin")
        self.rating = data.get("rating")
        self.url_image = data.get("url_image")
        self.best_seller = data.get("best_seller")
        self.price_upper = data.get("price_upper")
        self.is_sponsored = data.get("is_sponsored")
        self.manufacturer = data.get("manufacturer")
        self.pricing_count = data.get("pricing_count")
        self.reviews_count = data.get("reviews_count")
        self.is_amazons_choice = data.get("is_amazons_choice")
        self.no_price_reason = data.get("no_price_reason")
        self.is_prime = data.get("is_prime")
        self.sales_volume = data.get("sales_volume")
        self.variations = [
            Variations(item) for item in data.get("variations", [])
        ]
        self.images = [item for item in data.get("images", [])]
        self.site_links = OrganicSitelinks(data.get("sitelinks", {}))
        self.url_shown = data.get("url_shown")
        self.pos_overall = data.get("pos_overall")


class Merchant:
    def __init__(self, data):
        if data is None:
            data = {}
        self.raw = data
        self.url = data.get("url")
        self.name = data.get("name")


class Variations:
    def __init__(self, data):
        if data is None:
            data = {}
        self.raw = data
        self.asin = data.get("asin")
        self.title = data.get("title")
        self.price = data.get("price")
        self.price_strikethrough = data.get("price_strikethrough")
        self.not_available = data.get("not_available")


class SearchInformation:
    def __init__(self, data):
        if data is None:
            data = {}
        self.raw = data
        self.query = data.get("query")
        self.showing_results_for = data.get("showing_results_for")
        self.image = SearchInformationImage(data.get("image", {}))
        self.total_results_count = data.get("total_results_count")


class Variants:
    def __init__(self, data):
        if data is None:
            data = {}
        self.raw = data
        self.type = data.get("type")
        self.items = [VariantItem(item) for item in data.get("items", [])]


class VariantItem:
    def __init__(self, data):
        if data is None:
            data = {}
        self.raw = data
        self.value = data.get("value")
        self.selected = data.get("selected")
        self.available = data.get("available")
        self.product_id = data.get("product_id")


class RelatedItems:
    def __init__(self, data):
        if data is None:
            data = {}
        self.raw = data
        self.items = [RelatedItem(item) for item in data.get("items", [])]


class RelatedItem:
    def __init__(self, data):
        if data is None:
            data = {}
        self.raw = data
        self.url = data.get("url")
        self.price = data.get("price")
        self.title = data.get("title")
        self.rating = data.get("rating")
        self.currency = data.get("currency")
        self.reviews_count = data.get("reviews_count")


class Specifications:
    def __init__(self, data):
        if data is None:
            data = {}
        self.raw = data
        self.items = [
            SpecificationItem(item) for item in data.get("items", [])
        ]
        self.section_title = data.get("section_title")


class SpecificationItem:
    def __init__(self, data):
        if data is None:
            data = {}
        self.raw = data
        self.title = data.get("title")
        self.value = data.get("value")


class Pricing:
    def __init__(self, data):
        if data is None:
            data = {}
        self.raw = data
        self.price = data.get("price")
        self.seller = data.get("seller")
        self.details = data.get("details")
        self.currency = data.get("currency")
        self.condition = data.get("condition")
        self.price_tax = data.get("price_tax")
        self.price_total = data.get("price_total")
        self.seller_link = data.get("seller_link")
        self.price_shipping = data.get("price_shipping")
        self.delivery = data.get("delivery")
        self.seller_id = data.get("seller_id")
        self.rating_count = data.get("rating_count")
        self.delivery_options = data.get("delivery_options")


class SuggestedAmazonSearch:
    def __init__(self, data):
        if data is None:
            data = {}
        self.raw = data
        self.url = data.get("url")
        self.asin = data.get("asin")
        self.price = data.get("price")
        self.title = data.get("title")
        self.rating = data.get("rating")
        self.currency = data.get("currency")
        self.url_image = data.get("url_image")
        self.best_seller = data.get("best_seller")
        self.price_upper = data.get("price_upper")
        self.is_sponsored = data.get("is_sponsored")
        self.manufacturer = data.get("manufacturer")
        self.pricing_count = data.get("pricing_count")
        self.reviews_count = data.get("reviews_count")
        self.is_amazons_choice = data.get("is_amazons_choice")
        self.pos = data.get("pos")
        self.shipping_information = data.get("shipping_information")
        self.sales_volume = data.get("sales_volume")
        self.no_price_reason = data.get("no_price_reason")
        self.suggested_query = data.get("suggested_query")


class AmazonChoices:
    def __init__(self, data):
        if data is None:
            data = {}
        self.raw = data
        self.url = data.get("url")
        self.asin = data.get("asin")
        self.price = data.get("price")
        self.title = data.get("title")
        self.rating = data.get("rating")
        self.currency = data.get("currency")
        self.url_image = data.get("url_image")
        self.best_seller = data.get("best_seller")
        self.price_upper = data.get("price_upper")
        self.is_sponsored = data.get("is_sponsored")
        self.manufacturer = data.get("manufacturer")
        self.pricing_count = data.get("pricing_count")
        self.reviews_count = data.get("reviews_count")
        self.is_amazons_choice = data.get("is_amazons_choice")
        self.pos = data.get("pos")
        self.is_prime = data.get("is_prime")
        self.shipping_information = data.get("shipping_information")
        self.sales_volume = data.get("sales_volume")
        self.no_price_reason = data.get("no_price_reason")
        self.variations = [
            Variations(item) for item in data.get("variations", [])
        ]


class InstantRecommendations:
    def __init__(self, data):
        if data is None:
            data = {}
        self.raw = data
        self.url = data.get("url")
        self.asin = data.get("asin")
        self.price = data.get("price")
        self.title = data.get("title")
        self.rating = data.get("rating")
        self.currency = data.get("currency")
        self.url_image = data.get("url_image")
        self.best_seller = data.get("best_seller")
        self.price_upper = data.get("price_upper")
        self.is_sponsored = data.get("is_sponsored")
        self.manufacturer = data.get("manufacturer")
        self.pricing_count = data.get("pricing_count")
        self.reviews_count = data.get("reviews_count")
        self.is_amazons_choice = data.get("is_amazons_choice")
        self.pos = data.get("pos")
        self.sales_volume = data.get("sales_volume")
        self.no_price_reason = data.get("no_price_reason")


class AmazonProductAds:
    def __init__(self, data):
        if data is None:
            data = {}
        self.raw = data
        self.pos = data.get("pos")
        self.asin = data.get("asin")
        self.type = data.get("type")
        self.price = data.get("price")
        self.title = data.get("title")
        self.images = data.get("images", [])
        self.rating = data.get("rating")
        self.location = data.get("location")
        self.price_upper = data.get("price_upper")
        self.reviews_count = data.get("reviews_count")
        self.is_prime_eligible = data.get("is_prime_eligible")


class AmazonProductCategory:
    def __init__(self, data):
        if data is None:
            data = {}
        self.raw = data
        self.ladder = [
            {"url": item.get("url"), "name": item.get("name")}
            for item in data.get("ladder", [])
        ]


class AmazonProductDelivery:
    def __init__(self, data):
        if data is None:
            data = {}
        self.raw = data
        self.date = Date(data.get("date", {}))
        self.type = data.get("type")


class Date:
    def __init__(self, data):
        if data is None:
            data = {}
        self.raw = data
        self.by = data.get("by")
        self.from_date = data.get("from")


class AmazonProductSalesRank:
    def __init__(self, data):
        if data is None:
            data = {}
        self.raw = data
        self.rank = data.get("rank")
        self.ladder = [
            {"url": item.get("url"), "name": item.get("name")}
            for item in data.get("ladder", [])
        ]


class ProductDetails:
    def __init__(self, data):
        if data is None:
            data = {}
        self.raw = data
        self.asin = data.get("asin")
        self.batteries = data.get("batteries")
        self.item_weight = data.get("item_weight")
        self.manufacturer = data.get("manufacturer")
        self.customer_reviews = data.get("customer_reviews")
        self.best_sellers_rank = data.get("best_sellers_rank")
        self.country_of_origin = data.get("country_of_origin")
        self.item_model_number = data.get("item_model_number")
        self.product_dimensions = data.get("product_dimensions")
        self.date_first_available = data.get("date_first_available")
        self.is_discontinued_by_manufacturer = data.get(
            "is_discontinued_by_manufacturer"
        )


class AmazonRefurbishedProduct:
    def __init__(self, data):
        if data is None:
            data = {}
        self.raw = data
        self.link = Link(data.get("link", {}))
        self.condition_title = data.get("condition_title")


class Link:
    def __init__(self, data):
        if data is None:
            data = {}
        self.raw = data
        self.url = data.get("url")
        self.title = data.get("title")


class AmazonRatingStarDistribution:
    def __init__(self, data):
        if data is None:
            data = {}
        self.raw = data
        self.rating = data.get("rating")
        self.percentage = data.get("percentage")


class AmazonReviews:
    def __init__(self, data):
        if data is None:
            data = {}
        self.raw = data
        self.id = data.get("id")
        self.title = data.get("title")
        self.author = data.get("author")
        self.rating = data.get("rating")
        self.content = data.get("content")
        self.timestamp = data.get("timestamp")
        self.is_verified = data.get("is_verified")
        self.product_attributes = data.get("product_attributes")


class AmazonQuestions:
    def __init__(self, data):
        if data is None:
            data = {}
        self.raw = data
        self.title = data.get("title")
        self.votes = data.get("votes")
        self.answers = [Answer(item) for item in data.get("answers", [])]


class Answer:
    def __init__(self, data):
        if data is None:
            data = {}
        self.raw = data
        self.author = data.get("author")
        self.content = data.get("content")
        self.timestamp = data.get("timestamp")


class RecentFeedback:
    def __init__(self, data):
        if data is None:
            data = {}
        self.raw = data
        self.feedback = data.get("feedback")
        self.rated_by = data.get("rated_by")
        self.rating_stars = data.get("rating_stars")


class FeedbackSummaryTable:
    def __init__(self, data):
        if data is None:
            data = {}
        self.raw = data
        self.counts = Counts(data.get("counts", {}))
        self.neutral = Counts(data.get("neutral", {}))
        self.negative = Counts(data.get("negative", {}))
        self.positive = Counts(data.get("positive", {}))


class Counts:
    def __init__(self, data):
        if data is None:
            data = {}
        self.raw = data
        self.thirty_days = data.get("30_days")
        self.ninety_days = data.get("90_days")
        self.all_time = data.get("all_time")
        self.twelve_months = data.get("12_months")


class Job:
    def __init__(self, data):
        if data is None:
            data = {}
        self.raw = data
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
        self.links = [JobLink(item) for item in data.get("_links", [])]


class Context:
    def __init__(self, data):
        if data is None:
            data = {}
        self.raw = data
        self.key = data.get("key")
        self.value = data.get("value")


class JobLink:
    def __init__(self, data):
        if data is None:
            data = {}
        self.raw = data
        self.rel = data.get("rel")
        self.href = data.get("href")
        self.method = data.get("method")

class Pla:
    def __init__(self, data):
        if data is None:
            data = {}
        self.raw = data
        self.items = [PlaItem(item) for item in data.get("items", [])]
        self.pos_overall = data.get("pos_overall")

class PlaItem:
    def __init__(self, data):
        if data is None:
            data = {}
        self.raw = data
        self.pos = data.get("pos")
        self.url = data.get("url")
        self.price = data.get("price")
        self.title = data.get("title")
        self.seller = data.get("seller")
        self.url_image = data.get("url_image")
        self.image_data = data.get("image_data")

class Image:
    def __init__(self, data):
        if data is None:
            data = {}
        self.items = [ImageItem(item) for item in data.get("items", [])]
        self.pos_overall = data.get("pos_overall")


class ImageItem:
    def __init__(self, data):
        if data is None:
            data = {}
        self.raw = data
        self.alt = data.get("alt")
        self.pos = data.get("pos")
        self.url = data.get("url")
        self.data = data.get("data")
        self.source = data.get("source")


class OrganicSitelinks:
    def __init__(self, data):
        if data is None:
            data = {}
        self.raw = data
        self.expanded = [Expanded(item) for item in data.get("expanded", [])]
        self.inline = [Inline(item) for item in data.get("inline", [])]


class Twitter:
    def __init__(self, data):
        if data is None:
            data = {}
        self.raw = data
        self.pos = data.get("pos")
        self.url = data.get("url")
        self.items = [TwitterItem(item) for item in data.get("items", [])]
        self.title = data.get("title")
        self.pos_overall = data.get("pos_overall")


class TwitterItem:
    def __init__(self, data):
        if data is None:
            data = {}
        self.raw = data
        self.pos = data.get("pos")
        self.url = data.get("url")
        self.content = data.get("content")
        self.time_frame = data.get("time_frame")


class Knowledge:
    def __init__(self, data):
        if data is None:
            data = {}
        self.raw = data
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
            data = {}
        self.raw = data
        self.links = [LinkElement(item) for item in data.get("links", [])]
        self.title = data.get("title")
        self.content = data.get("content")


class LinkElement:
    def __init__(self, data):
        if data is None:
            data = {}
        self.raw = data
        self.href = data.get("href")
        self.title = data.get("title")


class Profile:
    def __init__(self, data):
        if data is None:
            data = {}
        self.raw = data
        self.url = data.get("url")
        self.title = data.get("title")


class RelatedSearches:
    def __init__(self, data):
        if data is None:
            data = {}
        self.raw = data
        self.url = data.get("url")
        self.title = data.get("title")
        self.section_title = data.get("section_title")
        self.pos_overall = data.get("pos_overall")
        self.related_searches = [
            item for item in data.get("related_searches", [])
        ]


class LocalPack:
    def __init__(self, data):
        if data is None:
            data = {}
        self.raw = data
        self.items = [LocalPackItem(item) for item in data.get("items", [])]
        self.pos_overall = data.get("pos_overall")


class LocalPackItem:
    def __init__(self, data):
        if data is None:
            data = {}
        self.raw = data
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
            data = {}
        self.raw = data
        self.href = data.get("href")
        self.title = data.get("title")


class TopStory:
    def __init__(self, data):
        if data is None:
            data = {}
        self.raw = data
        self.items = [TopStoryItem(item) for item in data.get("items", [])]
        self.pos_overall = data.get("pos_overall")


class TopStoryItem:
    def __init__(self, data):
        if data is None:
            data = {}
        self.pos = data.get("pos")
        self.url = data.get("url")
        self.title = data.get("title")
        self.source = data.get("source")
        self.time_frame = data.get("time_frame")


class PopularProducts:
    def __init__(self, data):
        if data is None:
            data = {}
        self.raw = data
        self.pos = data.get("pos")
        self.price = data.get("price")
        self.rating = data.get("rating")
        self.seller = data.get("seller")
        self.title = data.get("title")
        self.image_data = data.get("image_data")

class RelatedQuestions:
    def __init__(self, data):
        if data is None:
            data = {}
        self.raw = data
        self.pos_overall = data.get("pos_overall")
        self.related_questions = [
            RelatedQuestionsItem(item)
            for item in data.get("related_questions", [])
        ]


class RelatedQuestionsItem:
    def __init__(self, data):
        if data is None:
            data = {}
        self.raw = data
        self.pos = data.get("pos")
        self.answer = data.get("answer")
        self.source = data.get("source")
        self.question = data.get("question")


class Source:
    def __init__(self, data):
        if data is None:
            data = {}
        self.raw = data
        self.url = data.get("url")
        self.title = data.get("title")
        self.url_shown = data.get("url_shown")

class SearchInformationImage:
    def __init__(self, data):
        if data is None:
            data = {}
        self.raw = data
        self.url = data.get("url")
        self.width = data.get("width")
        self.height = data.get("height")
        self.other_sizes = data.get("other_sizes")


class ItemCarousel:
    def __init__(self, data):
        if data is None:
            data = {}
        self.raw = data
        self.items = [ItemCarouselItem(item) for item in data.get("items", [])]
        self.pos_overall = data.get("pos_overall")
        self.title = data.get("title")


class ItemCarouselItem:
    def __init__(self, data):
        if data is None:
            data = {}
        self.raw = data
        self.pos = data.get("pos")
        self.href = data.get("href")
        self.title = data.get("title")
        self.subtitle = data.get("subtitle")


class Recipes:
    def __init__(self, data):
        if data is None:
            data = {}
        self.raw = data
        self.items = [RecipesItem(item) for item in data.get("items", [])]
        self.pos_overall = data.get("pos_overall")


class RecipesItem:
    def __init__(self, data):
        if data is None:
            data = {}
        self.raw = data
        self.pos = data.get("pos")
        self.url = data.get("url")
        self.title = data.get("title")
        self.rating = data.get("rating")
        self.source = data.get("source")
        self.duration = data.get("duration")


class Videos:
    def __init__(self, data):
        if data is None:
            data = {}
        self.raw = data
        self.items = [VideosItem(item) for item in data.get("items", [])]
        self.pos_overall = data.get("pos_overall")


class VideosItem:
    def __init__(self, data):
        if data is None:
            data = {}
        self.raw = data
        self.pos = data.get("pos")
        self.url = data.get("url")
        self.title = data.get("title")
        self.author = data.get("author")
        self.source = data.get("source")


class FeaturedSnippet:
    def __init__(self, data):
        if data is None:
            data = {}
        self.raw = data
        self.url = data.get("url")
        self.desc = data.get("desc")
        self.title = data.get("title")
        self.url_shown = data.get("url_shown")
        self.pos_overall = data.get("pos_overall")


class RelatedSearchesCategorized:
    def __init__(self, data):
        if data is None:
            data = {}
        self.raw = data
        self.items = [
            RelatedSearchesCategorizedItem(item)
            for item in data.get("items", [])
        ]
        self.category = data.get("category")
        self.pos_overall = data.get("pos_overall")


class RelatedSearchesCategorizedItem:
    def __init__(self, data):
        if data is None:
            data = {}
        self.raw = data
        self.url = data.get("url")
        self.title = data.get("title")


class Category:
    def __init__(self, data):
        if data is None:
            data = {}
        self.raw = data
        self.name = data.get("name")
        self.type = data.get("type")


class Hotels:
    def __init__(self, data):
        if data is None:
            data = {}
        self.raw = data
        self.date_to = data.get("date_to")
        self.results = [HotelsResult(item) for item in data.get("results", [])]
        self.date_from = data.get("date_from")
        self.pos_overall = data.get("pos_overall")


class HotelsResult:
    def __init__(self, data):
        if data is None:
            data = {}
        self.raw = data
        self.price = data.get("price")
        self.title = data.get("title")
        self.from_location = data.get("from")


class Flights:
    def __init__(self, data):
        if data is None:
            data = {}
        self.raw = data
        self.to = data.get("to")
        self.from_location = data.get("from")
        self.results = [
            FlightsResult(item) for item in data.get("results", [])
        ]
        self.date_from = data.get("date_from")
        self.pos_overall = data.get("pos_overall")


class FlightsResult:
    def __init__(self, data):
        if data is None:
            data = {}
        self.raw = data
        self.url = data.get("url")
        self.type = data.get("type")
        self.price = data.get("price")
        self.airline = data.get("airline")
        self.duration = data.get("duration")


class VideoBox:
    def __init__(self, data):
        if data is None:
            data = {}
        self.raw = data
        self.url = data.get("url")
        self.title = data.get("title")
        self.pos_overall = data.get("pos_overall")


class LocalServiceAds:
    def __init__(self, data):
        if data is None:
            data = {}
        self.raw = data
        self.pos_overall = data.get("pos_overall")
        self.items = [
            LocalServiceAdsItem(item) for item in data.get("items", [])
        ]


class LocalServiceAdsItem:
    def __init__(self, data):
        if data is None:
            data = {}
        self.raw = data
        self.pos = data.get("pos")
        self.url = data.get("url")
        self.title = data.get("title")
        self.rating = data.get("rating")
        self.reviews_count = data.get("reviews_count")
        self.google_guaranteed = data.get("google_guaranteed")


class Navigation:
    def __init__(self, data):
        if data is None:
            data = {}
        self.raw = data
        self.url = data.get("url")
        self.title = data.get("title")
        self.pos = data.get("pos")


class InstantAnswers:
    def __init__(self, data):
        if data is None:
            data = {}
        self.raw = data
        self.type = data.get("type")
        self.parsed = data.get("_parsed")
        self.pos_overall = data.get("pos_overall")


class VisuallySimilarImages:
    def __init__(self, data):
        if data is None:
            data = {}
        self.raw = data
        self.all_images_url = data.get("all_images_url")
        self.featured_images = data.get("featured_images")
