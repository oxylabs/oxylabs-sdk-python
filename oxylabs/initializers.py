from .serp import (
    InitSERP,
    InitSERPAsync,
    Bing,
    BingAsync,
    Baidu,
    BaiduAsync,
    Yandex,
    YandexAsync,
    Google,
    GoogleAsync,
)
from .ecommerce import (
    InitEcommerce,
    InitEcommerceAsync,
    Amazon,
    AmazonAsync,
    GoogleShopping,
    Universal,
    GoogleShoppingAsync,
    Wayfair,
    WayfairAsync,
    UniversalAsync,
)


class SERP(Bing, Baidu, Yandex, Google):
    """
    Initializes the Serp class with the provided username and password.

    Args:
        username (str): The username for authentication.
        password (str): The password for authentication.
    """

    def __init__(self, username: str, password: str) -> None:
        self.client = InitSERP(username, password)


class SERPAsync(BingAsync, BaiduAsync, YandexAsync, GoogleAsync):
    """
    Initializes the SerpAsync client with the provided username and password.

    Args:
        username (str): The username for authentication.
        password (str): The password for authentication.
    """

    def __init__(self, username: str, password: str) -> None:
        self.client = InitSERPAsync(username, password)


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
