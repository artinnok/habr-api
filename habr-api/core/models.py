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

    def get_tf(self, word):
        text = self.text.split(' ')
        length = len(text)
        count = text.count(word)
        tf = count / length
        return tf

    def get_idf(self, word):
        all_count = Post.objects.count()
        count = Post.objects.filter(text__icontains=word).count()
        idf = log10(all_count / count)
        return idf

    def get_tf_idf(self, word):
        tf = self.get_tf(word)
        idf = self.get_idf(word)
        return tf * idf

    def __str__(self):
        return self.title
