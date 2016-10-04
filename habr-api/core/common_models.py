from django.db import models
from django.utils.timezone import now

from core import behaviors as bh


class Common(models.Model):
    created = models.DateTimeField(
        default=now,
        verbose_name='Время и дата создания',
        editable=False
    )

    class Meta:
        abstract = True


class CommonUser(bh.Phoneable, bh.Emailable, Common):
    name = models.CharField(
        verbose_name='Имя',
        max_length=200
    )

    class Meta:
        abstract = True
