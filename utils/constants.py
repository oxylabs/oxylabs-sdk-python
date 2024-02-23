from enum import Enum


class UserAgent(Enum):
    """
    Enumeration representing different user agents.

    Attributes:
        UA_MOBILE (str): Mobile user agent.
        UA_TABLET (str): Tablet user agent.
        UA_DESKTOP (str): Desktop user agent.
        UA_MOBILE_IOS (str): iOS mobile user agent.
        UA_TABLET_IOS (str): iOS tablet user agent.
        UA_DESKTOP_EDGE (str): Microsoft Edge desktop user agent.
        UA_DESKTOP_OPERA (str): Opera desktop user agent.
        UA_DESKTOP_SAFARI (str): Safari desktop user agent.
        UA_MOBILE_ANDROID (str): Android mobile user agent.
        UA_DESKTOP_CHROME (str): Chrome desktop user agent.
        UA_TABLET_ANDROID (str): Android tablet user agent.
        UA_DESKTOP_FIREFOX (str): Firefox desktop user agent.
    """

    UA_MOBILE = "mobile"
    UA_TABLET = "tablet"
    UA_DESKTOP = "desktop"
    UA_MOBILE_IOS = "mobile_ios"
    UA_TABLET_IOS = "tablet_ios"
    UA_DESKTOP_EDGE = "desktop_edge"
    UA_DESKTOP_OPERA = "desktop_opera"
    UA_DESKTOP_SAFARI = "desktop_safari"
    UA_MOBILE_ANDROID = "mobile_android"
    UA_DESKTOP_CHROME = "desktop_chrome"
    UA_TABLET_ANDROID = "tablet_android"
    UA_DESKTOP_FIREFOX = "desktop_firefox"

    @classmethod
    def is_user_agent_valid(cls, ua: str) -> bool:
        """
        Check if the given user agent is valid.

        Args:
            ua (str): The user agent to check.

        Returns:
            bool: True if the user agent is valid, False otherwise.
        """
        return ua in [member.value for member in cls.__members__.values()]


class Render(Enum):
    """
    Enum class representing different rendering options.
    """

    PNG = "png"
    HTML = "html"

    @classmethod
    def is_render_valid(cls, render: str) -> bool:
        """
        Check if the given render option is valid.

        Args:
            render (str): The render option to check.

        Returns:
            bool: True if the render option is valid, False otherwise.
        """
        return render in [member.value for member in cls.__members__.values()]


class Source(Enum):
    """
    Enum representing different data sources.
    """

    GoogleUrl = "google"
    GoogleAds = "google_ads"
    GoogleHotels = "google_hotels"
    GoogleSearch = "google_search"
    GoogleImages = "google_images"
    GoogleSuggestions = "google_suggest"
    GoogleTravelHotels = "google_travel_hotels"
    GoogleTrendsExplore = "google_trends_explore"

    BingUrl = "bing"
    BingSearch = "bing_search"

    YandexUrl = "yandex"
    YandexSearch = "yandex_search"

    BaiduUrl = "baidu"
    BaiduSearch = "baidu_search"

    GoogleShoppingUrl = "google_shopping"
    GoogleShoppingSearch = "google_shopping_search"
    GoogleShoppingProduct = "google_shopping_product"
    GoogleShoppingPricing = "google_shopping_pricing"

    Wayfair = "wayfair"
    WayfairSearch = "wayfair_search"

    Universal = "universal_ecommerce"

    AmazonUrl = "amazon"
    AmazonSearch = "amazon_search"
    AmazonProduct = "amazon_product"
    AmazonPricing = "amazon_pricing"
    AmazonReviews = "amazon_reviews"
    AmazonQuestions = "amazon_questions"
    AmazonBestsellers = "amazon_bestsellers"
    AmazonSellers = "amazon_sellers"


class Domain(Enum):
    """
    Enum class representing different domain values.
    """

    DOMAIN_RU = "ru"
    DOMAIN_UA = "ua"
    DOMAIN_TR = "tr"
    DOMAIN_CN = "cn"
    DOMAIN_COM_AI = "com.ai"
    DOMAIN_COM_PR = "com.pr"
    DOMAIN_SR = "sr"
    DOMAIN_ML = "ml"
    DOMAIN_COM_LB = "com.lb"
    DOMAIN_BF = "bf"
    DOMAIN_FM = "fm"
    DOMAIN_COM_MX = "com.mx"
    DOMAIN_BJ = "bj"
    DOMAIN_EE = "ee"
    DOMAIN_MV = "mv"
    DOMAIN_NE = "ne"
    DOMAIN_AT = "at"
    DOMAIN_GG = "gg"
    DOMAIN_AE = "ae"
    DOMAIN_CO_UZ = "co.uz"
    DOMAIN_AM = "am"
    DOMAIN_COM_SA = "com.sa"
    DOMAIN_TL = "tl"
    DOMAIN_COM_NA = "com.na"
    DOMAIN_COM_BH = "com.bh"
    DOMAIN_DK = "dk"
    DOMAIN_COM_SB = "com.sb"
    DOMAIN_RO = "ro"
    DOMAIN_BY = "by"
    DOMAIN_COM_CO = "com.co"
    DOMAIN_COM_GI = "com.gi"
    DOMAIN_CO_ID = "co.id"
    DOMAIN_MS = "ms"
    DOMAIN_COM_NG = "com.ng"
    DOMAIN_IS = "is"
    DOMAIN_COM_EG = "com.eg"
    DOMAIN_COM_ET = "com.et"
    DOMAIN_COM_AF = "com.af"
    DOMAIN_CH = "ch"
    DOMAIN_CO_AO = "co.ao"
    DOMAIN_CL = "cl"
    DOMAIN_CO_ZA = "co.za"
    DOMAIN_COM_NF = "com.nf"
    DOMAIN_DK_RO = "ro"
    DOMAIN_MD = "md"
    DOMAIN_ES = "es"
    DOMAIN_BJ_YO = "bj"
    DOMAIN_HU = "hu"
    DOMAIN_DJ = "dj"
    DOMAIN_COM_MT = "com.mt"
    DOMAIN_COM_EC = "com.ec"
    DOMAIN_CO_IN = "co.in"
    DOMAIN_LK = "lk"
    DOMAIN_CO_KE = "co.ke"
    DOMAIN_GY = "gy"
    DOMAIN_BE = "be"
    DOMAIN_VG = "vg"
    DOMAIN_CO_BW = "co.bw"
    DOMAIN_COM_VN = "com.vn"
    DOMAIN_CO_TZ = "co.tz"
    DOMAIN_NE_HA = "ne"
    DOMAIN_CO_ZW = "co.zw"
    DOMAIN_TO = "to"
    DOMAIN_KZ = "kz"
    DOMAIN_COM_UY = "com.uy"
    DOMAIN_IQ = "iq"
    DOMAIN_COM_TW = "com.tw"
    DOMAIN_RW = "rw"
    DOMAIN_AD = "ad"
    DOMAIN_COM_LY = "com.ly"
    DOMAIN_AL = "al"
    DOMAIN_CO_IL = "co.il"
    DOMAIN_KI = "ki"
    DOMAIN_COM = "com"
    DOMAIN_MU = "mu"
    DOMAIN_SC = "sc"
    DOMAIN_COM_HK = "com.hk"
    DOMAIN_COM_PA = "com.pa"
    DOMAIN_CA = "ca"
    DOMAIN_GE = "ge"
    DOMAIN_COM_GT = "com.gt"
    DOMAIN_LI = "li"
    DOMAIN_COM_KH = "com.kh"
    DOMAIN_CO_CR = "co.cr"
    DOMAIN_COM_BO = "com.bo"
    DOMAIN_CO_VE = "co.ve"
    DOMAIN_COM_NI = "com.ni"
    DOMAIN_TD = "td"
    DOMAIN_CF = "cf"
    DOMAIN_TK = "tk"
    DOMAIN_BI = "bi"
    DOMAIN_MG = "mg"
    DOMAIN_COM_BD = "com.bd"
    DOMAIN_COM_BZ = "com.bz"
    DOMAIN_GM = "gm"
    DOMAIN_LA = "la"
    DOMAIN_COM_KW = "com.kw"
    DOMAIN_CM = "cm"
    DOMAIN_HT = "ht"
    DOMAIN_NO = "no"
    DOMAIN_COM_FJ = "com.fj"
    DOMAIN_TM = "tm"
    DOMAIN_COM_SL = "com.sl"
    DOMAIN_COM_MM = "com.mm"
    DOMAIN_IM = "im"
    DOMAIN_SI = "si"
    DOMAIN_COM_QA = "com.qa"
    DOMAIN_COM_PE = "com.pe"
    DOMAIN_CD = "cd"
    DOMAIN_TT = "tt"
    DOMAIN_COM_TR = "com.tr"
    DOMAIN_TG = "tg"
    DOMAIN_CO_LS = "co.ls"
    DOMAIN_GR = "gr"
    DOMAIN_GL = "gl"
    DOMAIN_MK = "mk"
    DOMAIN_CO_ZM = "co.zm"
    DOMAIN_COM_PH = "com.ph"
    DOMAIN_IT = "it"
    DOMAIN_CO_JP = "co.jp"
    DOMAIN_WS = "ws"
    DOMAIN_COM_AR = "com.ar"
    DOMAIN_CO_MZ = "co.mz"
    DOMAIN_AZ = "az"
    DOMAIN_CO_CK = "co.ck"
    DOMAIN_FI = "fi"
    DOMAIN_COM_BN = "com.bn"
    DOMAIN_PT = "pt"
    DOMAIN_COM_TJ = "com.tj"
    DOMAIN_COM_CY = "com.cy"
    DOMAIN_CV = "cv"
    DOMAIN_COM_MY = "com.my"
    DOMAIN_IE = "ie"
    DOMAIN_COM_SG = "com.sg"
    DOMAIN_DE = "de"
    DOMAIN_BA = "ba"
    DOMAIN_LU = "lu"
    DOMAIN_BG = "bg"
    DOMAIN_CO_VI = "co.vi"
    DOMAIN_COM_OM = "com.om"
    DOMAIN_AS = "as"
    DOMAIN_DZ = "dz"
    DOMAIN_FR = "fr"
    DOMAIN_LV = "lv"
    DOMAIN_LT = "lt"
    DOMAIN_PS = "ps"
    DOMAIN_SE = "se"
    DOMAIN_CG = "cg"
    DOMAIN_NR = "nr"
    DOMAIN_CO_UG = "co.ug"
    DOMAIN_COM_VC = "com.vc"
    DOMAIN_JO = "jo"
    DOMAIN_CO_TH = "co.th"
    DOMAIN_RS = "rs"
    DOMAIN_BS = "bs"
    DOMAIN_COM_PK = "com.pk"
    DOMAIN_CO_UK = "co.uk"
    DOMAIN_SO = "so"
    DOMAIN_GA = "ga"
    DOMAIN_COM_UA = "com.ua"
    DOMAIN_HR = "hr"
    DOMAIN_COM_CU = "com.cu"
    DOMAIN_SK = "sk"
    DOMAIN_COM_NP = "com.np"
    DOMAIN_NU = "nu"
    DOMAIN_MN = "mn"
    DOMAIN_VU = "vu"
    DOMAIN_NL = "nl"
    DOMAIN_PT_ST = "st"
    DOMAIN_COM_BR = "com.br"
    DOMAIN_TH = "co.th"
    DOMAIN_MW = "mw"
    DOMAIN_COM_PG = "com.pg"
    DOMAIN_PL = "pl"
    DOMAIN_CO_NZ = "co.nz"
    DOMAIN_KG = "kg"
    DOMAIN_CI = "ci"
    DOMAIN_SH = "sh"
    DOMAIN_COM_DO = "com.do"
    DOMAIN_SN = "sn"
    DOMAIN_COM_JM = "com.jm"
    DOMAIN_CO_MA = "co.ma"
    DOMAIN_COM_TN = "com.tn"
    DOMAIN_DM = "dm"
    DOMAIN_COM_SV = "com.sv"
    DOMAIN_COM_SG_2 = "com.sg"
    DOMAIN_GP = "gp"
    DOMAIN_ME = "me"
    DOMAIN_COM_AG = "com.ag"
    DOMAIN_CZ = "cz"
    DOMAIN_COM_PY = "com.py"
    DOMAIN_MR_IN = "co.in"
    DOMAIN_COM_GH = "com.gh"
    DOMAIN_ST_LS = "co.ls"
    DOMAIN_BT = "bt"
    DOMAIN_RU_KZ = "kz"
    DOMAIN_IT_SM = "sm"
    DOMAIN_JE = "je"
    DOMAIN_TN = "tn"
    DOMAIN_COM_AU = "com.au"
    DOMAIN_ME_ME = "me"
    DOMAIN_PN = "pn"
    DOMAIN_HN = "hn"
    DOMAIN_CO_KR = "co.kr"
    DOMAIN_AR = "com.ar"
    DOMAIN_BO = "com.bo"
    DOMAIN_BZ = "com.bz"
    DOMAIN_UY = "com.uy"
    DOMAIN_COM_VE = "com.ve"
    DOMAIN_ID_TL = "tl"


class Locale(Enum):
    """
    Enum class representing different locale values.
    """

    LOCALE_EN = "en"
    LOCALE_RU = "ru"
    LOCALE_BY = "by"
    LOCALE_DE = "de"
    LOCALE_FR = "fr"
    LOCALE_ID = "id"
    LOCALE_KK = "kk"
    LOCALE_TT = "tt"
    LOCALE_TR = "tr"
    LOCALE_UK = "uk"
