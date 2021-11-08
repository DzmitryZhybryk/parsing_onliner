import pytest


def test_onliner_categories_count(test_data: dict, actual_onliner_categories_list: list):
    assert len(actual_onliner_categories_list) == test_data.get(
        'excepted_result'), 'The number of categories should be six!'


@pytest.mark.parametrize('test_input', ['авто', 'машина'])
def test_onliner_auto_categories_articles(test_input: str, check_word_in_text: list):
    for items in check_word_in_text:
        assert test_input not in items, f'All auto categories articles should to have {test_input} word!'


@pytest.mark.parametrize('test_input', ['Минск'])
def test_onliner_people_categories_articles(test_input: str, check_word_in_text: list):
    for items in check_word_in_text:
        assert test_input not in items, f'All people categories should not have {test_input} word!'


def test_onliner_article_is_not_empty(test_data, article_is_not_empty: int):
    assert article_is_not_empty == test_data.get('excepted_result'), 'The article should not be empty!'
