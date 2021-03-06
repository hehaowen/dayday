# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-17 01:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('article', '0001_initial'),
        ('daydays', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OthersInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField()),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.ArticlesInfo')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='daydays.UserInfo')),
            ],
            options={
                'verbose_name': '购物车',
                'verbose_name_plural': '购物车',
            },
        ),
    ]
