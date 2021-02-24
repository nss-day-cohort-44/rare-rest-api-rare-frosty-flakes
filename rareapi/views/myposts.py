from rareapi.views.post import PostSerializer
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rareapi.models import Post, RareUser

class MyPosts(ViewSet):
    
    def list(self, request):

        rare_user = RareUser.objects.get(user=request.quth.user)
        posts = Post.objects.filter(posts__user = rare_user)

        posts = PostSerializer(
            posts, many=True, context={'request': request}
        )
        # rare_user = RareUserSerializer(
        #     rare_user, many=False, context={'request': request}
        # )
        my_posts = {}
        my_posts["posts"] = posts.data

class UserSerializer(serializers.ModelSerializer):
    """JSON serializer for gamer's related Django user"""
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username')




