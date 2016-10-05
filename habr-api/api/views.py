from rest_framework import generics

from api.serializers import PostSerializer, AuthorSerializer, AuthorPostSerializer
from core.models import Post, Author


class PostList(generics.RetrieveAPIView):
    serializer_class = PostSerializer


class AuthorDetail(generics.RetrieveAPIView):
    serializer_class = AuthorPostSerializer
    queryset = Author.objects.all()


class AuthorList(generics.ListAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()