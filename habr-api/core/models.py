from datetime import date

from django.db import models

from core import common_models as cm
from core import behaviors as bh


class Author(cm.Common):
    """
    Сущность автора поста, может сделать много постов
    """
    AUTHOR_URL = 'https://habrahabr.ru/users/{}/'

    nickname = models.CharField(
        verbose_name='Никнейм',
        max_length=100,
        unique=True
    )
    karma = models.FloatField(
        verbose_name='Карма',
        blank=True,
        null=True
    )
    rating = models.FloatField(
        verbose_name='Рейтинг',
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'автор'
        verbose_name_plural = 'авторы'

    def __str__(self):
        return self.nickname

    @property
    def url(self):
        return self.AUTHOR_URL.format(self.nickname[1:])


class Post(bh.Titleable, bh.Textable, cm.Common):
    """
    Сущность поста с хабра
    """
    POST_URL = 'https://habrahabr.ru/post/{}/'

    number = models.BigIntegerField(
        verbose_name='Номер',
        unique=True
    )
    date = models.DateField(
        verbose_name='Дата',
        default=date.today
    )
    author = models.ForeignKey(
        'core.Author',
        verbose_name='Автор',
        related_name='post_list'
    )

    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'посты'

    def __str__(self):
        return self.title

    @property
    def url(self):
        return self.POST_URL.format(self.number)
