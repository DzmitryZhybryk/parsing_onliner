"""Storage module for class OnlinerArticle, OnlinerCategory and MainOnlinerPageLinks"""
import logging
from typing import List
from requests import codes
from models.onliner_objects.parsing import OnlinerHTMLParser
from tools.clients.http_client import HTTPClient

DEFAULT_HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko)'
                  ' Chrome/93.0.4577.82 Safari/537.36', 'accept': '*/*'}


class OnlinerArticle:
    """Article information class"""

    def __init__(self, article_url: str, http_client: HTTPClient):
        """
        :param article_url: article url address
        """
        self.url = article_url
        self.http_client = http_client

    @property
    def get_articles_info_list(self) -> List[dict]:
        """
        Method to call the parser_onliner_articles method
        :return: list with information about article name, article date and article author
        """
        response = self.http_client.get(self.url, DEFAULT_HEADERS)
        if response.status_code == codes.ok:
            articles_info = OnlinerHTMLParser.get_articles(response.text)
            return articles_info
        logging.error(f'status code - {response.status_code}, error type - {response.reason}')
        return []


class OnlinerCategory:
    """Class works with categories"""

    def __init__(self, category_url: str, http_client: HTTPClient, exception: str = None):
        """
        :param category_url: category url address
        """
        self.url = category_url
        self.http_client = http_client
        self.__exception = exception

    @property
    def get_articles_object(self) -> List[OnlinerArticle]:
        """
        Method to call the parser_onliner_articles_link method
        :return: list with OnlinerArticle class object
        """
        response = self.http_client.get(self.url, DEFAULT_HEADERS)
        if response.status_code == codes.ok:
            articles_links = OnlinerHTMLParser.get_articles_link(response.text, self.url)
            return [OnlinerArticle(link, self.http_client) for link in articles_links]
        logging.error(f'status code - {response.status_code}, error type - {response.reason}')
        return []

    @property
    def get_categories_name(self) -> List[str]:
        """
        Method to call the parser_onliner_category_names method
        :return: category names list
        """
        response = self.http_client.get(self.url, DEFAULT_HEADERS)
        if response.status_code == codes.ok:
            category_names = OnlinerHTMLParser.get_categories_data(html=response.text, is_links=False,
                                                                   exception=self.__exception)
            return category_names
        logging.error(f'status code - {response.status_code}, error type - {response.reason}')
        return []


class MainOnlinerPage:
    """Class works with main onliner page"""

    def __init__(self, url: str, http_client: HTTPClient, exception: str = None):
        """
        :param url: main page url code
        :param exception: used for exclusion something from result
        """
        self.url = url
        self.http_client = http_client
        self.__exception = exception

    @property
    def get_onliner_categories_object(self) -> List[OnlinerCategory]:
        """
        Method to call the parser_onliner_categories_link method
        :return: list with OnlinerCategory class object
        """
        response = self.http_client.get(self.url, DEFAULT_HEADERS)
        if response.status_code == codes.ok:
            categories_links = OnlinerHTMLParser.get_categories_data(html=response.text, exception=self.__exception)
            return [OnlinerCategory(link, self.http_client) for link in categories_links]
        logging.error(f'status code - {response.status_code}, error type - {response.reason}')
        return []
