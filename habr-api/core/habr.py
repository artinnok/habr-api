import re

from bs4 import BeautifulSoup
import requests

from core.models import Post, Author


PAGE_URL = 'https://habrahabr.ru/page{}/'
MIN_PAGE = 1
MAX_PAGE = 20

SELECTOR_MAP = {
    # post
    'date': {'name': 'span', 'class_': 'post__time_published'},
    'title': {'name': 'a', 'class_': 'post__title_link'},
    'post': {'name': 'a', 'class_': 'post__title_link'},

    # author
    'author': {'name': 'a', 'class_': 'post-author__link'},
    'karma': {'name': 'div', 'class_': 'voting-wjt__counter-score'},
    'rating': {'name': 'div', 'class_': 'statistic__value_magenta'},
}


class Parser:
    def parse_nickname(self, soup):
        nickname = (foo.text for foo in soup.find_all(**SELECTOR_MAP['author']))
        nickname = (foo.strip() for foo in nickname)
        return nickname

    def parse_number(self, soup):
        def extract_number(text):
            number = re.search('(?P<number>[0-9]+)', text).group('number')
            return int(number)
        number = (foo['href'] for foo in soup.find_all(**SELECTOR_MAP['post']))
        number = (extract_number(foo) for foo in number)
        return number

    def parse(self):
        for item in range(MIN_PAGE, MAX_PAGE + 1):
            page = requests.get(PAGE_URL.format(item))
            soup = BeautifulSoup(page.text, 'html.parser')
            nickname = self.parse_nickname(soup)
            number = self.parse_number(soup)
            saver = Saver()
            for nick, num in zip(nickname, number):
                saver.save(nick, num)


class Saver:
    def save(self, nick, num):
        author, author_created = Author.objects.get_or_create(nickname=nick)
        post, post_created = Post.objects.get_or_create(number=num,
                                                        author=author)
        return post, author

    def get_soup(self, url):
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'html.parser')
        return soup

    def save_author_data(self):
        def prepare_data(soup, selector):
            data = soup.find(**SELECTOR_MAP[selector])
            data = data.text.replace(',', '.').replace('–', '-')
            return data
        for author in Author.objects.all():
            soup = self.get_soup(author.url)
            karma = prepare_data(soup, 'karma')
            rating = prepare_data(soup, 'rating')
            author.karma = karma
            author.rating = rating
            author.save()

    def save_post_data(self):
        for post in Post.objects.all():
            soup = self.get_soup(post.url)
            title = soup.find(**SELECTOR_MAP['title'])
            print(title.next_sibling)
