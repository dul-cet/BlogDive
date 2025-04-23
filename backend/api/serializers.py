from rest_framework import serializers
from .models import Notification, Post, Comment, ProjectFollow, Notification, Follow
from django.contrib.auth.models import User

class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Post
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)  # поле только для чтения: поле author будет заполняться текущим пользователем
    class Meta:
        model = Comment
        fields = ['id', 'text', 'text', 'created_at','author']

class FollowSerializer(serializers.ModelSerializer):
    follower = serializers.StringRelatedField(read_only=True)
    following = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = Follow
        fields = ['follower', 'following', 'created_at']
        
class SimpleNotificationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['message', 'is_read', 'created_at']

class ProjectFollowSerializer(serializers.ModelSerializer):
    follower = serializers.StringRelatedField(read_only=True)
    project = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = ProjectFollow
        fields = ['follower', 'project', 'created_at']
