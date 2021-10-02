from onliner_html_models import MainOnlinerPage, OnlinerCategory, OnlinerArticle

if __name__ == '__main__':
    article_links = OnlinerCategory('https://money.onliner.by/')
    print(article_links.onliner_articles)

    category_links = MainOnlinerPage('https://www.onliner.by/')
    print(category_links.onliner_links)

    article_info = OnlinerArticle('https://auto.onliner.by/2021/09/27/v-velikobritanii-deficit-topliva')
    print(article_info.onliner_articles)
