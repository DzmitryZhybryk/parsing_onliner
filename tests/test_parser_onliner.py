import pytest


def test_onliner_categories_count(test_data, actual_categories_number):
    assert actual_categories_number == test_data.get('excepted_result'), 'Error message'


@pytest.mark.parametrize('test_input', ['авто', 'машина'])
def test_onliner_auto_categories_links(test_input, chek_word_in_text):
    for items in chek_word_in_text:
        assert test_input in items, 'Error message'


@pytest.mark.xfail(strict=True)
@pytest.mark.parametrize('test_input', ['Минск'])
def test_onliner_people_categories_links(test_input, chek_word_in_text):
    for items in chek_word_in_text:
        assert test_input not in items, 'Error message'


def test_onliner_article_is_not_empty(test_data, article_is_not_empty):
    assert article_is_not_empty > 0, 'Error message'
