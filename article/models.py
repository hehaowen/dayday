#encoding=utf-8
from django.db import models
# 富文本编辑器
from tinymce.models import HTMLField


class TitleInfo(models.Model):
    title = models.CharField(max_length=10)
    image = models.ImageField(upload_to='image')
    isDlete = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '类别'
        verbose_name_plural = '类别'

class ArticlesInfo(models.Model):
    aname = models.CharField(max_length=20)
    intro = models.CharField(max_length=50)
    gprice = models.DecimalField(max_digits=7, decimal_places=2)
    count = models.IntegerField()
    gunit = models.CharField(max_length=20)
    image = models.ImageField(upload_to='upload')
    isDelete = models.BooleanField(default=False)
    textcontext = HTMLField(null=True)
    sorts = models.ForeignKey(TitleInfo)
    def __str__(self):
        return self.aname

    class Meta:
        verbose_name = '商品信息'
        verbose_name_plural = '商品信息'



