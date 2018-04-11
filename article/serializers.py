from rest_framework import serializers
from .models import ArticlesInfo,TitleInfo

class TitleSerializers(serializers.ModelSerializer):
    class Meta:
        model = TitleInfo
        fields = ('title')
class ArtSerializers(serializers.ModelSerializer):
    class Meta:
        model = ArticlesInfo
        fields = ('aname','intro','gprice','sorts')