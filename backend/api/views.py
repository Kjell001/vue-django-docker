from django.contrib.auth.models import Group, User
from app.models import Platform, Game
from api.serializers import (
    GroupSerializer,
    UserSerializer,
    PlatformSerializer,
    GameSerializer,
)
from rest_framework import permissions, viewsets


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = Group.objects.all().order_by("name")
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class PlatformViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows platforms to be viewed or edited.
    """

    queryset = Platform.objects.all().order_by("name")
    serializer_class = PlatformSerializer


class GameViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows games to be viewed or edited.
    """

    queryset = Game.objects.all().order_by("year")
    serializer_class = GameSerializer
