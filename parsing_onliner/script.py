from onliner_html_models import MainOnlinerPage, OnlinerCategory, OnlinerArticle
from http_client import HTTPClient

if __name__ == '__main__':
    http_client = HTTPClient()

    article_links = OnlinerCategory('https://money.onliner.by/', http_client)
    print(article_links.onliner_articles)

    category_links = MainOnlinerPage('https://www.onliner.by/', http_client)
    print(category_links.onliner_links)

    category_names = OnlinerCategory('https://www.onliner.by/', http_client)
    print(category_names.onliner_category_names)

    article_info = OnlinerArticle('https://auto.onliner.by/2021/09/27/v-velikobritanii-deficit-topliva', http_client)
    print(article_info.onliner_articles)
