# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-20 02:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_auto_20180420_0931'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlesinfo',
            name='bigImage',
            field=models.ImageField(default=1, upload_to='upload_big'),
            preserve_default=False,
        ),
    ]