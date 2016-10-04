from django.db import models


class Titleable(models.Model):
    title = models.CharField(
        verbose_name='Название',
        max_length=200,
        blank=True

    )

    class Meta:
        abstract = True


class Textable(models.Model):
    text = models.TextField(
        verbose_name='Текст',
        blank=True
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
