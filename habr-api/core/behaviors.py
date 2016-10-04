from django.db import models
from imagekit.models import ProcessedImageField


class Titleable(models.Model):
    title = models.CharField(
        verbose_name='Название',
        max_length=200
    )

    class Meta:
        abstract = True


class Textable(models.Model):
    text = models.TextField(
        verbose_name='Текст'
    )

    class Meta:
        abstract = True


class Imageable(models.Model):
    image = ProcessedImageField(
        verbose_name='Изображение',
        options={'optimize': True}
    )

    class Meta:
        abstract = True


class Emailable(models.Model):
    email = models.EmailField(
        verbose_name='Электронная почта'
    )

    class Meta:
        abstract = True


class Phoneable(models.Model):
    phone = models.CharField(
        verbose_name='Контактный телефон',
        max_length=50
    )

    class Meta:
        abstract = True
