# encoding=utf-8
from django.db import models


# Create your models here.
class UserInfo(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=40)
    mail = models.EmailField()
    shou = models.CharField(max_length=20, null=True)
    address = models.CharField(max_length=100, null=True)
    postcode = models.CharField(max_length=6, null=True)
    phonenumber = models.CharField(max_length=11, null=True)
    createtime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

    class Meta:
        ordering = ['-createtime']
        verbose_name = '用户信息'
        verbose_name_plural = '用户信息'
