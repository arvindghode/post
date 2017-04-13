from django.db.models import Q
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status, decorators
from rest_framework.permissions import IsAuthenticated

class PostViewSet(ModelViewSet):
    """
        API endpoint for viewing and creating posts.
    """
    queryset = Post.objects.all().order_by('-created')
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated,)

class CommentViewSet(ModelViewSet):
    """
        API endpoint for viewing and creating posts.
    """
    queryset = Comment.objects.all().order_by('-created')
    serializer_class = CommentSerializer
