from rest_framework import generics

from api.serializers import PostSerializer, AuthorSerializer
from core.models import Post, Author


class PostList(generics.ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class AuthorList(generics.ListAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()