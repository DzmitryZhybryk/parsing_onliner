import pytest
from typing import Dict, List

import yaml

from tools.clients.http_client import HTTPClient
from tools.parsers.onliner_html_models import OnlinerCategory, OnlinerArticle


@pytest.fixture()
def test_data(request) -> Dict[str, str]:
    """
    Fixture reads the yaml file and returns parameters depending on the test that called it
    :return: parameters dict
    """
    with open(f'{request.fspath.dirname}/data.yaml') as file:
        return yaml.load(file).get(request.function.__name__)


@pytest.fixture(scope='session')
def http_client() -> HTTPClient:
    """
    Fixture make http response
    :return: HTTPClient
    """
    return HTTPClient()


@pytest.fixture()
def actual_onliner_categories_list(test_data: dict, http_client: HTTPClient) -> list:
    """
    Fixture create OnlinerCategory object and returns the number of all categories
    :param test_data: dict with parameters
    :param http_client: http client
    :return: the number of all categories
    """
    exception = 'Форум'
    onliner_category_object = OnlinerCategory(test_data.get('url'), http_client, exception)
    return onliner_category_object.get_category_names_list


@pytest.fixture()
def check_word_in_text(test_data: dict, http_client: HTTPClient) -> List[str]:
    """
    Fixture create OnlinerArticle object for receive all articles text
    :param test_data: dict with parameters
    :param http_client: http client
    :return: all articles text
    """
    onliner_category_object = OnlinerCategory(test_data.get('url'), http_client)
    links = [items.url for items in onliner_category_object.get_articles_list]
    all_articles_text = [OnlinerArticle(link, http_client).get_articles_info_list(False) for link in links]
    return all_articles_text


@pytest.fixture()
def article_is_not_empty(test_data: dict, http_client: HTTPClient) -> int:
    """
    Method create OnlinerCategory object for receive article length
    :param test_data: dict with parameters
    :param http_client: http client
    :return: article length
    """
    onliner_article_object = OnlinerArticle(test_data.get('url'), http_client)
    return bool(onliner_article_object.get_articles_info_list(is_articles_info=False))

