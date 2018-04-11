from rest_framework import serializers

from others.models import OthersInfo


class OtherSerializer(serializers.ModelSerializer):
    class Meta:
        model = OthersInfo
        fields = ('user','article','count')