from django.db import models


# Create your models here.
class Comment(models.Model):
    name = models.ForeignKey('daydays.UserInfo')
    create_time = models.DateTimeField(auto_now_add=True)
    articlename = models.ForeignKey('ArticlesInfo')
    image = models.ImageField(null=True)
    text = models.TextField()

    def __str__(self):
        return self.name
