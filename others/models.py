from django.db import models


# Create your models here.
class OthersInfo(models.Model):
    user = models.ForeignKey('daydays.UserInfo')
    article = models.ForeignKey('article.ArticlesInfo')
    count = models.IntegerField()

    def __str__(self):
        return self.count

    class Meta:
        verbose_name = '购物车'
        verbose_name_plural = '购物车'
