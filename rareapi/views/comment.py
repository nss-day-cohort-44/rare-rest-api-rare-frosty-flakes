""" 
Created By: Danny McCracken
Date: 2/22/21
Subject: Defines server response for each comment
"""

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.http import HttpResponseServerError
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rareapi.models import Comment, RareUser
import datetime

class Comments(ViewSet):

    def create(self, request):
        """Handle POST operations for comments

        Returns:
            Response -- JSON serialized comment instance
        """

        author = RareUser.objects.get(user=request.auth.user)

        post = Post.objects.get(pk=request.data["postId"])

        comment = Comment()
        comment.post_id= post
        comment.author_id= author
        comment.content = request.data["content"]
        comment.created_on = datetime.datetime.now()

        try:
            comment.save()
            serializer = CommentSerializer(comment, context={'request': request})
            return Response(serializer.data)
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single comment

        Returns:
            Response -- JSON serialized comment instance
        """
        try:
            comment = Comment.objects.get(pk=pk)
            serializer = CommentSerializer(comment, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def update(self, request, pk=None):
        """Handle PUT requests for a comment

        Returns:
            Response -- Empty body with 204 status code
        """
        author = RareUser.objects.get(user=request.auth.user)

        post = Post.objects.get(pk=request.data["postId"])

        comment = Comment.objects.get(pk=pk)
        comment.post_id= post
        comment.author_id= author
        comment.content = request.data["content"]
        comment.created_on = datetime.datetime.now()

        comment.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        """Handle DELETE requests for a single comment

        Returns:
            Response -- 200, 404, or 500 status code
        """
        try:
            comment = Comment.objects.get(pk=pk)
            comment.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Comment.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request):
        """Handle GET requests to comment resource

        Returns:
            Response -- JSON serialized list of comments
        """
        # Get all commentsfrom the database
        comments = Comment.objects.all()

        # Support filtering comments by type
        #    http://localhost:8000/comments?post=1
        #
        # That URL will retrieve all a post's comments
        post_id = self.request.query_params.get('post', None)
        if post_id is not None:
            comments = comments.filter(post__id=post_id)

        serializer = CommentSerializer(
            comments, many=True, context={'request': request})
        return Response(serializer.data)

# class CommentUserSerializer(serializers.ModelSerializer):
#     """JSON serializer for event organizer's related Django user"""
#     class Meta:
#         model = User
#         fields = ['username']

# class CommentRareUserSerializer(serializers.ModelSerializer):
#     """JSON serializer for event organizer"""
#     user = CommentUserSerializer(many=False)

#     class Meta:
#         model = RareUser
#         fields = ['user']

# class PostSerializer(serializers.ModelSerializer):
#     """JSON serializer for posts"""
    
#     class Meta:
#         model = Post
#         fields = ('id',)

class CommentSerializer(serializers.ModelSerializer):
    """JSON serializer for comments"""
    class Meta:
        model = Comment
        fields = ('id', 'post_id', 'author_id', 'content', 'created_on')
        depth = 1