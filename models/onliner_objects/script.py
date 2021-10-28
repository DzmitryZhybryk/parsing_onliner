from tools.clients.http_client import HTTPClient
from tools.parsers.onliner_html_models import OnlinerCategory, MainOnlinerPage, OnlinerArticle

if __name__ == '__main__':
    http_client = HTTPClient()

    article_links = OnlinerCategory('https://auto.onliner.by/', http_client)
    print(article_links.get_articles_list)

    category_links = MainOnlinerPage('https://www.onliner.by/', http_client)
    print(category_links.get_onliner_categories_object)

    category_names = OnlinerCategory('https://www.onliner.by/', http_client, 'Форум')
    print(category_names.get_category_names_list)

    article_info = OnlinerArticle('https://people.onliner.by/2021/10/13/vooruzhennyj-lukom', http_client)
    print(article_info.get_articles_info_list())

    article_text = OnlinerArticle('https://people.onliner.by/2021/10/13/vooruzhennyj-lukom', http_client)
    print(article_text.get_articles_info_list(is_articles_info=False))
