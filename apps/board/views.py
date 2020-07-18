from django.db.models import Q
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from apps.board.models import Board, Comment, Post
from apps.board.serializers import BoardSerializer, CommentSerializer, PostSerializer


class BoardViewSet(viewsets.ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['GET'], url_path='posts')
    def posts(self, request, pk):
        board = get_object_or_404(Board, unique_title=pk)
        board_posts = board.posts.all()
        serializer = PostSerializer(board_posts, many=True)
        return Response(serializer.data)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.exclude(status="removed").order_by('-create_date')
    serializer_class = PostSerializer

    def destroy(self, request, *args, **kwargs):
        post = self.get_object()
        post.status = 'removed'
        post.save()

        post_comments = post.comments.all()
        for objects in post_comments:
            objects.status = 'removed'
            objects.save()

        return Response(status=status.HTTP_200_OK)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.filter(~Q(status="removed"), parent=None).order_by('-create_date')
    serializer_class = CommentSerializer

    def destroy(self, request, *args, **kwargs):
        comment = self.get_object()
        comment.status = 'removed'
        comment.save()
