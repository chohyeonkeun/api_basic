from rest_framework import serializers

from .models import Tweet

# 유저 목록에 출력될 형식
class TweetListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = '__all__'

class TweetSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = ['text', 'author']