"""Storage module for class OnlinerHTMLParser"""
from typing import List
from bs4 import BeautifulSoup
from variables import ArticleField


class OnlinerHTMLParser:
    """Class parsing links"""

    @staticmethod
    def parser_onliner_categories_link(html: str, exception=None) -> List[str]:
        """
        Method gets all categories links
        :param html: html page cod for parsing
        :param exception: used for exclusion something from result
        :return: categories links
        """
        all_categories_links = []
        soup = BeautifulSoup(html, 'html.parser')
        items = soup.find_all('div', class_='b-main-page-grid-4')
        for item in items:
            item_href = item.find('header', class_='b-main-page-blocks-header-2').find('a').get('href')
            if item_href == exception:
                continue
            all_categories_links.append(item_href)
        return all_categories_links

    @staticmethod
    def __helper_parser_onliner_articles_link(link: str) -> str:
        """
        Helper parser_onliner_articles_link method
        :param link: article link
        :return: verified links to include HTTP
        """
        return link if 'https:/' in link else f'https:/{link}'

    @staticmethod
    def parser_onliner_articles_link(html: str) -> List[str]:
        """
        Method gets article links
        :param html: links to categories of html page codes
        :return: article links
        """
        soup = BeautifulSoup(html, 'html.parser')
        first_soup_object = soup.find('div', class_='news-grid__flex').find_all('a', class_='news-tiles__stub')
        second_soup_object = soup.find('div', class_='news-grid__flex').find_all('a', class_='news-tidings__stub')
        all_articles_links = []
        for item in first_soup_object:
            link = item.get('href')
            all_articles_links.append(OnlinerHTMLParser.__helper_parser_onliner_articles_link(link))
        for item in second_soup_object:
            link = item.get('href')
            all_articles_links.append(OnlinerHTMLParser.__helper_parser_onliner_articles_link(link))
        return all_articles_links

    @staticmethod
    def parser_onliner_category_names(html: str, exception=None) -> List[str]:
        """
        Method gets all category names
        :param html: html page cod for parsing
        :param exception: used for exclusion something from result
        :return: article names list
        """
        all_categories_names = []
        soup = BeautifulSoup(html, 'html.parser')
        items = soup.find_all('div', class_='b-main-page-grid-4')
        print(items)
        for item in items:
            item_name = item.find_all('header', class_='b-main-page-blocks-header-2').find('a').get_text(strip=True)
            if item_name == exception:
                continue
            all_categories_names.append(item_name)
        return all_categories_names

    @staticmethod
    def __helper_parser_onliner_articles(text: str) -> str:
        """
        Helper parser_onliner_articles method
        :param text: article info
        :return: correct article info
        """
        if '\xa0' in text and 'nbsp' in text:
            text = text.replace('\xa0', '')
            text = text.replace('nbsp', '')
        return text

    @staticmethod
    def parser_onliner_articles(html: str) -> List[dict]:
        pass
        """
        Method gets information about articles
        :param html: html page cod article links
        :return: article information
        """
        soup = BeautifulSoup(html, 'html.parser')
        article_info = list()
        article_author = soup.find('div', class_='news-header__author news-helpers_hide_mobile').get_text(
            strip=True)
        article_author = OnlinerHTMLParser.__helper_parser_onliner_articles(article_author)
        article_info.append({
            ArticleField.ARTICLE_NAMES.value: soup.find('div', class_='news-header__title').get_text(strip=True),
            ArticleField.ARTICLE_DATE.value: soup.find('div', class_='news-header__time').get_text(strip=True),
            ArticleField.ARTICLE_AUTHOR.value: article_author
        })
        return article_info
