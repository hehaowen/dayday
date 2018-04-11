from rest_framework import serializers
from daydays.models import UserInfo

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ('username','mail','password','shou','address')

