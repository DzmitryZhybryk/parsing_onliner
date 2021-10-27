import pytest
import yaml
from tools.clients.http_client import HTTPClient
from tools.parsers.onliner_html_models import OnlinerCategory, OnlinerArticle


@pytest.fixture()
def test_data(request) -> dict:
    """
    Method reads the yaml file and return parameters depending on the test that called it
    :return: params dict
    """
    with open(f'{request.fspath.dirname}/data.yaml') as file:
        return yaml.load(file).get(request.function.__name__)


@pytest.fixture(scope='session')
def http_client() -> HTTPClient:
    return HTTPClient()


@pytest.fixture()
def actual_categories_number(test_data, http_client) -> int:
    """
    Method create OnlinerCategory object
    :param test_data: dict with parameters
    :param http_client: http client
    :return: the number of all categories
    """
    onliner_category_object = OnlinerCategory(test_data.get('url'), http_client, 'Форум')
    return len(onliner_category_object.get_category_names_list)


@pytest.fixture()
def chek_word_in_text(test_data, http_client):
    """
    Method create OnlinerArticle object for receive all articles text
    :param test_data: dict with parameters
    :param http_client: http client
    :return: all articles text
    """
    onliner_category_object = OnlinerCategory(test_data.get('url'), http_client)
    links = [items.url for items in onliner_category_object.get_articles_list]
    all_articles_text = [OnlinerArticle(link, http_client).get_articles_info_list(False) for link in links]
    return all_articles_text


@pytest.fixture()
def article_is_not_empty(test_data, http_client):
    """
    Method create OnlinerCategory object for receive article length
    :param test_data: dict with parameters
    :param http_client: http client
    :return: article length
    """
    onliner_article_object = OnlinerArticle(test_data.get('url'), http_client)
    return len(onliner_article_object.get_articles_info_list(is_articles_info=False))

