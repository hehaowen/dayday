# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-09 03:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=40)),
                ('mail', models.EmailField(max_length=254)),
                ('shou', models.CharField(max_length=20, null=True)),
                ('address', models.CharField(max_length=100, null=True)),
                ('postcode', models.CharField(max_length=6, null=True)),
                ('phonenumber', models.CharField(max_length=11, null=True)),
                ('createtime', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '用户信息',
                'verbose_name_plural': '用户信息',
                'ordering': ['-createtime'],
            },
        ),
    ]
