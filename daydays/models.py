# encoding=utf-8
from django.db import models


# Create your models here.
class UserInfo(models.Model):
    username = models.CharField(max_length=20,verbose_name="用户名")
    password = models.CharField(max_length=40,verbose_name="密码")
    mail = models.EmailField()
    shou = models.CharField(max_length=20, null=True,verbose_name="收件人")
    address = models.CharField(max_length=100, null=True,verbose_name="收货地址")
    postcode = models.CharField(max_length=6, null=True,verbose_name="邮编")
    phonenumber = models.CharField(max_length=11, null=True,verbose_name="手机号码")
    createtime = models.DateTimeField(auto_now_add=True,verbose_name="创建时间吗")
    token_read = models.CharField(max_length=200,verbose_name="暂存token")
    tokens = models.CharField(max_length=200,verbose_name="永久token")

    def __str__(self):
        return self.username

    class Meta:
        ordering = ['-createtime']
        verbose_name = '用户信息'
        verbose_name_plural = '用户信息'
