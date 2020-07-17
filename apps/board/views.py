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

    def destroy(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)
        # post.status = 'removed'
        # print(post)
        serializer = PostSerializer(post, data={'status': 'removed'})
        print(serializer)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            print(serializer.data)
            return Response({"msg": "삭제 실패"}, status=status.HTTP_400_BAD_REQUEST)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.filter(~Q(status="removed"), parent=None).order_by('-create_date')
    serializer_class = CommentSerializer

    def destroy(self, request, *args, **kwargs):
        pass
