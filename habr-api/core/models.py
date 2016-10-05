from datetime import date

from django.db import models

from core import common_models as cm
from core import behaviors as bh


class Author(cm.Common):
    """
    Сущность автора поста, может сделать много постов
    """
    url = models.URLField(
        verbose_name='Ссылка',
        unique=True
    )

    class Meta:
        verbose_name = 'автор'
        verbose_name_plural = 'авторы'

    def __str__(self):
        return self.url


class Post(bh.Titleable, bh.Textable, cm.Common):
    """
    Сущность поста с хабра
    """
    url = models.URLField(
        verbose_name='Ссылка',
        unique=True
    )
    author = models.ForeignKey(
        'core.Author',
        verbose_name='Автор',
        related_name='post_list',
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'посты'

    def __str__(self):
        return self.title
