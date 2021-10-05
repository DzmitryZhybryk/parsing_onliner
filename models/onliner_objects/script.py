from parsing_onliner.tools.parsers.onliner_html_models import MainOnlinerPage, OnlinerCategory, OnlinerArticle
from parsing_onliner.tools.clients.http_client import HTTPClient

if __name__ == '__main__':
    http_client = HTTPClient()

    article_links = OnlinerCategory('https://people.onliner.by', http_client)
    print(article_links.get_article_object)

    category_links = MainOnlinerPage('https://www.onliner.by/', http_client)
    print(category_links.get_onliner_category_object)

    category_names = OnlinerCategory('https://www.onliner.by/', http_client)
    print(category_names.get_category_names)

    article_info = OnlinerArticle('https://auto.onliner.by/2021/09/27/v-velikobritanii-deficit-topliva', http_client)
    print(article_info.get_articles_info_list)
