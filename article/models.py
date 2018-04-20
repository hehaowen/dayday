# encoding=utf-8
from django.db import models
# 富文本编辑器
from ckeditor_uploader.fields import RichTextUploadingField


class TitleInfo(models.Model):
    title = models.CharField(max_length=10, verbose_name='分类')
    image = models.ImageField(upload_to='image', blank=True)
    isDlete = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '类别'
        verbose_name_plural = '类别'


class ArticlesInfo(models.Model):
    aname = models.CharField(max_length=40, verbose_name='商品名称')
    intro = models.CharField(max_length=50, verbose_name='商品简介')
    gprice = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='价格')
    count = models.IntegerField()
    gunit = models.CharField(max_length=20, verbose_name='商品个数')
    crt = models.IntegerField()
    bigImage = models.ImageField(upload_to='upload_big')
    image = models.ImageField(upload_to='upload')
    isDelete = models.BooleanField(default=False)
    textcontext = RichTextUploadingField(default='')
    createtime = models.DateTimeField(auto_now_add=True)
    sorts = models.ForeignKey(TitleInfo)

    def __str__(self):
        return self.aname

    def clickup(self):
        self.crt += 1
        self.save(update_fields=['crt'])

    class Meta:
        verbose_name = '商品信息'
        verbose_name_plural = '商品信息'
        ordering = ['-createtime']



