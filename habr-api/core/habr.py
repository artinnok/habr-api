import re

from bs4 import BeautifulSoup
import requests

from core.models import Post, Author


PAGE_URL = 'https://habrahabr.ru/page{}/'
HABR_URL = 'https://habrahabr.ru'
MIN_PAGE = 1
MAX_PAGE = 10

SELECTOR_MAP = {
    # post
    'url': {'name': 'a', 'class_': 'post__title_link'},
    'date': {'name': 'span', 'class_': 'post__time_published'},
    'title': {'name': 'span', 'class_': 'post__title-arrow'},
    'text': {'name': 'div', 'class_': 'content html_format'},

    # author
    'author1': {'name': 'a', 'class_': 'author-info__name'},
    'author2': {'name': 'a', 'class_': 'author-info__nickname'},
}


def parse_author(soup):
    author = soup.find(**SELECTOR_MAP['author1'])
    if not author:
        author = soup.find(**SELECTOR_MAP['author2'])
    return author['href']


def parse_title(soup):
    title = soup.find(**SELECTOR_MAP['title'])
    return title.find_next_sibling().text


def is_today(date):
    if re.search('сегодня', date):
        return True
    return False


def is_parsed(url):
    return Post.objects.filter(url=url).exists()


def parse():
    for item in range(MIN_PAGE, MAX_PAGE):
        page = requests.get(PAGE_URL.format(item))
        soup = BeautifulSoup(page.text, 'html.parser')
        links = [foo['href'] for foo in soup.find_all(**SELECTOR_MAP['url'])]
        dates = [foo.text for foo in soup.find_all(**SELECTOR_MAP['date'])]
        for url, date in zip(links, dates):
            if not is_parsed(url) and is_today(date):
                post = requests.get(url)
                post_soup = BeautifulSoup(post.text, 'html.parser')
                title = parse_title(post_soup)
                text = soup.find(**SELECTOR_MAP['text'])
                author = parse_author(post_soup)
                author, created = Author.objects.get_or_create(
                    url=HABR_URL + author)
                post = Post.objects.create(url=url, author=author,
                                           title=title, date=date)