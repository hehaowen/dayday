# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-09 12:33
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArticlesInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aname', models.CharField(max_length=40, verbose_name='商品名称')),
                ('intro', models.CharField(max_length=50, verbose_name='商品简介')),
                ('gprice', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='价格')),
                ('count', models.IntegerField()),
                ('gunit', models.CharField(max_length=20, verbose_name='商品个数')),
                ('image', models.ImageField(upload_to='upload')),
                ('isDelete', models.BooleanField(default=False)),
                ('textcontext', ckeditor_uploader.fields.RichTextUploadingField(default='')),
                ('createtime', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '商品信息',
                'verbose_name_plural': '商品信息',
                'ordering': ['-createtime'],
            },
        ),
        migrations.CreateModel(
            name='TitleInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10, verbose_name='分类')),
                ('image', models.ImageField(upload_to='image')),
                ('isDlete', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': '类别',
                'verbose_name_plural': '类别',
            },
        ),
        migrations.AddField(
            model_name='articlesinfo',
            name='sorts',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.TitleInfo'),
        ),
    ]
