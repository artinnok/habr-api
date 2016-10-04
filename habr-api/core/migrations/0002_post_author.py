# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-04 18:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='post_list', to='core.Author', verbose_name='Автор'),
            preserve_default=False,
        ),
    ]
