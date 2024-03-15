from oxylabs import InitSerp, InitSerpAsync, InitEcommerce, InitEcommerceAsync
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


class Serp(Bing, Baidu, Yandex, Google):
    """
    Initializes the Serp class with the provided username and password.

    Args:
        username (str): The username for authentication.
        password (str): The password for authentication.
    """

    def __init__(self, username: str, password: str) -> None:
        self.client = InitSerp(username, password)


class SerpAsync(BingAsync, BaiduAsync, YandexAsync, GoogleAsync):
    """
    Initializes the SerpAsync client with the provided username and password.

    Args:
        username (str): The username for authentication.
        password (str): The password for authentication.
    """

    def __init__(self, username: str, password: str) -> None:
        self.client = InitSerpAsync(username, password)


class Ecommerce(Amazon, GoogleShopping, Wayfair, Universal):
    """
    Initializes the Ecommerce client with the provided username and password.

    Args:
        username (str): The username for authentication.
        password (str): The password for authentication.
    """

    def __init__(self, username: str, password: str) -> None:
        self.client = InitEcommerce(username, password)


class EcommerceAsync(AmazonAsync, GoogleShoppingAsync, WayfairAsync, UniversalAsync):
    """
    Initializes the EcommerceAsync client with the provided username and password.

    Args:
        username (str): The username for authentication.
        password (str): The password for authentication.
    """

    def __init__(self, username: str, password: str) -> None:
        self.client = InitEcommerceAsync(username, password)
