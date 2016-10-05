# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-04 23:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20161005_0156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='post_list', to='core.Author', verbose_name='Автор'),
        ),
    ]