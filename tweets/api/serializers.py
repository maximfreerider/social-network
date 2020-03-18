from rest_framework import serializers
from ..models import Tweet
from likes import services as like_services
from django.contrib.auth.models import User


class TweetSerializer(serializers.ModelSerializer):
    is_fan = serializers.SerializerMethodField()

    class Meta:
        model = Tweet
        fields = (
            'id',
            'body',
            'total_likes',
            'is_fan'
        )

    def get_is_fan(self, obj) -> bool:
        """проверяю лайкнул ли 'request.user' твит ('obj') """
        user = self.context.get('request').user
        return like_services.is_fan(obj, user)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'password'
        )

    def save(self):
        user = User(username=self.validated_data['username'],
                    password=self.validated_data['password'])
        user.save()
        return user
