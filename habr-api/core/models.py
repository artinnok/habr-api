from math import log10

from django.db import models

from core import common_models as cm
from core import behaviors as bh


class Author(cm.Common):
    """
    Сущность автора поста, может сделать много постов
    """
    link = models.URLField(
        verbose_name='Ссылка',
        unique=True
    )

    class Meta:
        verbose_name = 'автор'
        verbose_name_plural = 'авторы'

    def __str__(self):
        return self.link


class Post(bh.Titleable, bh.Textable, cm.Common):
    """
    Сущность поста с хабра
    """
    link = models.URLField(
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

    @classmethod
    def get_tf(cls, word):
        text = cls.text.split(' ')
        length = len(text)
        count = text.count(word)
        tf = count / length
        return tf

    @classmethod
    def get_idf(cls, word):
        all_count = Post.objects.count()
        count = Post.objects.filter(text__icontains=word).count()
        idf = log10(all_count / count)
        return idf

    @classmethod
    def get_tf_idf(cls, word):
        tf = cls.get_tf(word)
        idf = cls.get_idf(word)
        return tf * idf

    def __str__(self):
        return self.title
