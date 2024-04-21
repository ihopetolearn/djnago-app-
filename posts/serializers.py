from rest_framework import serializers

from .models import Post


class PostSerializer1(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id','title','text','is_enabled','email']


class PostSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id','title','text','is_enabled','email']
