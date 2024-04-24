from django.contrib.auth.models import Group, User
from app.models import Platform, Game
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "groups"]


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ["url", "name"]


class PlatformSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Platform
        fields = ["id", "name", "created_at", "updated_at"]


class GameSerializer(serializers.HyperlinkedModelSerializer):
    platform = PlatformSerializer()

    class Meta:
        model = Game
        fields = ["id", "title", "year", "platform", "created_at", "updated_at"]
