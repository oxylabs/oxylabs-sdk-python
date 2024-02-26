from utils.defaults import (
    DEFAULT_DOMAIN,
    DEFAULT_LIMIT_SERP,
    DEFAULT_PAGES,
    DEFAULT_START_PAGE,
    DEFAULT_USER_AGENT,
    set_default_domain,
    set_default_limit,
    set_default_pages,
    set_default_start_page,
    set_default_user_agent,
)
from utils.utils import BaseSearchOpts, BaseUrlOpts, validate_url, Config, BaseGoogleOpts
from utils.constants import Render, Domain, UserAgent, Source, Locale
import dataclasses
import json


AcceptedTbmParameters = [
    "app",
	"bks",
	"blg",
	"dsc",
	"isch",
	"nws",
	"pts",
	"plcs",
	"rcp",
	"lcl",
]

AcceptedSearchTypeParameters = [
    "web_search",
	"image_search",
	"google_shopping",
	"youtube_search",
]


@dataclasses.dataclass
class GoogleSearchOpts(BaseSearchOpts):
    
    locale: str = None
    geo_location: str = None
    render: Render = None
    
    def check_parameter_validity(self):

        if not UserAgent.is_user_agent_valid(self.user_agent_type):
            raise ValueError(f"Invalid user agent parameter: {self.user_agent_type}")
        
        if self.render and not Render.is_render_valid(self.render):
            raise ValueError(f"Invalid render parameter: {self.render}")
        
        if self.limit <= 0 or self.pages <= 0 or self.start_page <= 0:
            raise ValueError(
                "Limit, pages and start_page parameters must be greater than 0"
            )
            
            
class GoogleSearchOpts(BaseGoogleOpts):
    domain: Domain = None
    start_page: int = None
    pages: int = None
    limit: int = None
    locale: Locale = None
    parse: bool = None

class GoogleUrlOpts(BaseGoogleOpts):
    pass

class GoogleAdsOpts(BaseGoogleOpts):
    domain: Domain = None
    start_page: int = None
    pages: int = None
    locale: str = None
    parse: bool = None

class GoogleSuggestionsOpts(BaseGoogleOpts):
    locale: str = None

class GoogleHotelsOpts(BaseGoogleOpts):
    domain: Domain = None
    start_page: int = None
    pages: int = None
    limit: int = None
    locale: str = None
    parse_instructions: None

class GoogleTravelHotelsOpts(BaseGoogleOpts):
    domain: Domain = None
    start_page: int = None
    locale: str = None

class GoogleImagesOpts(BaseGoogleOpts):
    domain: Domain = None
    start_page: int = None
    pages: int = None
    locale: str = None
    parse: bool = None

class GoogleTrendsExploreOpts(BaseGoogleOpts):
    pass
