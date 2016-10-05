import re

import requests
from bs4 import BeautifulSoup
from celery import shared_task

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


def parse_text(soup):
    text = soup.find(**SELECTOR_MAP['text'])
    text = list(text.stripped_strings)
    text = ''.join(text)
    return text


def get_soup(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    return soup


def is_today(date):
    if re.search('сегодня', date):
        return True
    return False


def is_parsed(url):
    return Post.objects.filter(url=url).exists()


@shared_task(name='parse')
def parse():
    for item in range(MIN_PAGE, MAX_PAGE):
        soup = get_soup(PAGE_URL.format(item))

        links = [foo['href'] for foo in soup.find_all(**SELECTOR_MAP['url'])]
        dates = [foo.text for foo in soup.find_all(**SELECTOR_MAP['date'])]
        for link, date in zip(links, dates):
            if not is_parsed(link) and is_today(date):
                post_soup = get_soup(link)

                title = parse_title(post_soup)
                text = parse_text(post_soup)
                author = parse_author(post_soup)

                author, created = Author.objects.get_or_create(
                    link=HABR_URL + author)
                Post.objects.create(link=link, author=author, title=title,
                                    text=text)
