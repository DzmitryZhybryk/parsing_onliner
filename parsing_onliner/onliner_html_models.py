"""Storage module for class OnlinerArticle, OnlinerCategory and MainOnlinerPageLinks"""
from typing import List
from parsing import OnlinerHTMLParser
from error_handling import Logging
from requests import codes

DEFAULT_HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko)'
                  ' Chrome/93.0.4577.82 Safari/537.36', 'accept': '*/*'}


class OnlinerArticle:
    """Class gets article information"""

    def __init__(self, article_url: str, http_client):
        """
        :param article_url: article url address
        """
        self.url = article_url
        self.http_client = http_client
        self.onliner_articles = self.__get_articles_info_list()

    def __get_articles_info_list(self) -> List[dict]:
        """
        Method gets articles information
        :return: list with information about article name, article date and article author for articles
        """
        response = self.http_client.get(self.url, DEFAULT_HEADERS)
        if response.status_code == codes.ok:
            articles_info = OnlinerHTMLParser.parser_onliner_articles(response.text)
            return articles_info
        Logging.error_info(response.status_code, response.reason)
        return []


class OnlinerCategory:
    """Class gets OnlinerArticle object"""

    def __init__(self, category_url: str, http_client):
        """
        :param category_url: categories url address
        """
        self.url = category_url
        self.http_client = http_client
        self.onliner_articles = self.__get_article_object()

    def __get_article_object(self) -> List[OnlinerArticle]:
        """
        Method gets all categories links
        :return: list with object OnlinerArticle class
        """
        response = self.http_client.get(self.url, DEFAULT_HEADERS)
        if response.status_code == codes.ok:
            articles_links = OnlinerHTMLParser.parser_onliner_articles_link(response.text)
            return [OnlinerArticle(link, http) for link, http in articles_links]
        Logging.error_info(response.status_code, response.reason)
        return []


class MainOnlinerPage:
    """Class gets OnlinerCategory object"""

    def __init__(self, url: str, http_client, exception=None):
        """
        :param url: main page url code
        :param exception: used for exclusion something from result
        """
        self.url = url
        self.http_client = http_client
        self.__exception = exception
        self.onliner_links = self.__get_onliner_category_object()

    def __get_onliner_category_object(self) -> List[OnlinerCategory]:
        """
        Method gets all categories links
        :return: list with object OnlinerCategory class
        """
        response = self.http_client.get(self.url, DEFAULT_HEADERS)
        if response.status_code == codes.ok:
            categories_links = OnlinerHTMLParser.parser_onliner_categories_link(response.text, self.__exception)
            return [OnlinerCategory(link, http) for link, http in categories_links]
        Logging.error_info(response.status_code, response.reason)
        return []
