from oxylabs import Serp, SerpAsync, Ecommerce, EcommerceAsync
from oxylabs.serp import (
    Bing,
    BingAsync,
    Baidu,
    BaiduAsync,
    Yandex,
    YandexAsync,
    Google,
    GoogleAsync,
)
from oxylabs.ecommerce import (
    Amazon,
    AmazonAsync,
    GoogleShopping,
    Universal,
    GoogleShoppingAsync,
    Wayfair,
    WayfairAsync,
    UniversalAsync,
)


class InitSerp(Bing, Baidu, Yandex, Google):
    """
    Initializes the Serp class with the provided username and password.

    Args:
        username (str): The username for authentication.
        password (str): The password for authentication.
    """

    def __init__(self, username: str, password: str) -> None:
        self.client = Serp(username, password)


class InitSerpAsync(BingAsync, BaiduAsync, YandexAsync, GoogleAsync):
    """
    Initializes the SerpAsync client with the provided username and password.

    Args:
        username (str): The username for authentication.
        password (str): The password for authentication.
    """

    def __init__(self, username: str, password: str) -> None:
        self.client = SerpAsync(username, password)


class InitEcommerce(Amazon, GoogleShopping, Wayfair, Universal):
    """
    Initializes the Ecommerce client with the provided username and password.

    Args:
        username (str): The username for authentication.
        password (str): The password for authentication.
    """

    def __init__(self, username: str, password: str) -> None:
        self.client = Ecommerce(username, password)


class InitEcommerceAsync(
    AmazonAsync, GoogleShoppingAsync, WayfairAsync, UniversalAsync
):
    """
    Initializes the EcommerceAsync client with the provided username and password.

    Args:
        username (str): The username for authentication.
        password (str): The password for authentication.
    """

    def __init__(self, username: str, password: str) -> None:
        self.client = EcommerceAsync(username, password)
