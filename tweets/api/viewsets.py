from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from ..models import Tweet
from .serializers import TweetSerializer
from likes.api.mixin import LikedMixin


class TweetViewSet(LikedMixin, viewsets.ModelViewSet):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer
    permission_classes = (IsAuthenticated,)

