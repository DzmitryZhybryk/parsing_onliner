from tools.clients.http_client import HTTPClient
from tools.parsers.onliner_html_models import OnlinerCategory, MainOnlinerPage, OnlinerArticle

if __name__ == '__main__':
    http_client = HTTPClient()

    article_links = OnlinerCategory('https://auto.onliner.by/', http_client)
    print(article_links.get_articles_object)

    category_links = MainOnlinerPage('https://www.onliner.by/', http_client)
    print(category_links.get_onliner_categories_object)

    category_names = OnlinerCategory('https://www.onliner.by/', http_client)
    print(category_names.get_categories_name)

    article_info = OnlinerArticle('https://auto.onliner.by/2021/09/27/v-velikobritanii-deficit-topliva', http_client)
    print(article_info.get_articles_info_list)
