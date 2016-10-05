from rest_framework import serializers

from core.models import Post, Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        exclude = ('created', )


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        exclude = ('created', 'author', )