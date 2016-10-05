from rest_framework import serializers

from core.models import Post, Author


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        exclude = ('created', 'author', )


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        exclude = ('created', )


class AuthorPostSerializer(AuthorSerializer):
    post_list = PostSerializer(many=True)
