"""Storage module for class OnlinerHTMLParser"""
from typing import List
from urllib.parse import urljoin
from models.onliner_objects.variables import ArticleField
from bs4 import BeautifulSoup


class OnlinerHTMLParser:
    """Parsing class for working with Onliner pages"""

    @staticmethod
    def get_categories_data(html: str, is_links: bool = True, exception: str = None) -> List[str]:
        """
        Method of obtaining categories links and categories names
        :param html: links to categories of html page codes
        :param is_links: flag for selecting the desired iteration
        :param exception: use for exclusion something from result
        :return: article links or category names
        """
        all_categories_links = []
        soup = BeautifulSoup(html, 'html.parser')
        data = soup.find_all('div', class_='b-main-page-grid-4')
        for items in data:
            if is_links:
                item = items.find('header', class_='b-main-page-blocks-header-2').find('a').get('href')
            else:
                item = items.find('header', class_='b-main-page-blocks-header-2').find('a').get_text(strip=True)
            if item == exception:
                continue
            all_categories_links.append(item)
        return all_categories_links

    @staticmethod
    def __http_check(link: str, category_url: str) -> str:
        """
        Helper parser_onliner_articles_link method
        :param link: article link
        :param category_url: category url
        :return: verified links to include HTTP
        """
        return link if category_url in link else urljoin(category_url, link)

    @staticmethod
    def __helper_get_articles_link(*soup_objects: list, category_url: str) -> List[str]:
        """
        Helper parser_onliner_articles_link method
        :param soup_objects: list soup objects
        :param category_url: category url
        :return: article links
        """
        result = []
        for items in soup_objects:
            for item in items:
                link = item.get('href')
                result.append(OnlinerHTMLParser.__http_check(link, category_url))
        return result

    @staticmethod
    def get_articles_link(html: str, category_url: str) -> List[str]:
        """
        Method of obtaining articles link
        :param html: links to categories of html page codes
        :param category_url: category url
        :return: article links
        """
        soup = BeautifulSoup(html, 'html.parser')
        first_list_soup_object = soup.find('div', class_='news-grid__flex').find_all('a', class_='news-tiles__stub')
        second_list_soup_object = soup.find('div', class_='news-grid__flex').find_all('a', class_='news-tidings__stub')
        all_articles_links = list(
            OnlinerHTMLParser.__helper_get_articles_link(first_list_soup_object, second_list_soup_object,
                                                         category_url=category_url))
        return all_articles_links

    @staticmethod
    def __helper_get_articles(text: str) -> str:
        """
        Helper parser_onliner_articles method
        :param text: article info
        :return: correct article info
        """
        return text.replace('\xa0', '').replace('nbsp', '')

    @staticmethod
    def get_articles(html: str) -> List[dict]:
        """
        Method of obtaining article information
        :param html: html page cod article links
        :return: article information
        """
        soup = BeautifulSoup(html, 'html.parser')
        article_info = list()
        items = soup.find('div', class_='news-header__author news-helpers_hide_mobile').get_text(
            strip=True)
        article_author = OnlinerHTMLParser.__helper_get_articles(items)
        article_info.append({
            ArticleField.ARTICLE_NAMES.value: soup.find('div', class_='news-header__title').get_text(strip=True),
            ArticleField.ARTICLE_DATE.value: soup.find('div', class_='news-header__time').get_text(strip=True),
            ArticleField.ARTICLE_AUTHOR.value: article_author
        })
        return article_info

    @staticmethod
    def get_article_text(html: str) -> str:
        soup = BeautifulSoup(html, 'html.parser')
        article_text = ''
        items = soup.find('div', class_="news-text").find_all('p')
        for item in items:
            item = item.get_text(strip=True)
            item = OnlinerHTMLParser.__helper_get_articles(item)
            article_text = f'{article_text}{item}'
        return article_text
