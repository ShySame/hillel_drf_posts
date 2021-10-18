from django.contrib.auth import get_user_model

from rest_framework import serializers

from .models import Comment, Post

User = get_user_model()


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'last_name', 'email']


class PostSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=True)
    date_create = serializers.DateField(read_only=True)
    author = serializers.CharField(read_only=True)
    text = serializers.CharField(required=True)

    class Meta:
        model = Post
        fields = ['id', 'url', 'title', 'date_create', 'author', 'text']


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    message = serializers.CharField(required=True)
    date_create = serializers.DateTimeField(read_only=True)
    author = serializers.CharField(read_only=True)
    class Meta:
        model = Comment
        fields = ['id', 'url', 'message', 'date_create', 'author', 'post',]
