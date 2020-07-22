from django.contrib.auth.decorators import login_required
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
        post = self.get_object()
        user = request.user
        if post.creator == user:
            post.remove()
            return Response({"msg": "삭제 되었습니다."}, status=status.HTTP_200_OK)
        else:
            return Response({"msg": "게시글 작성자가 아닙니다."}, status=status.HTTP_400_BAD_REQUEST)

    def like(self, request, *args, **kwargs):
        user = request.user
        post = self.get_object()
        post_obj = Post.objects.get(pk=post.id)

        if post_obj.post_likes.filter(id=user.id).exist():
            post_obj.post_likes.remove(user)
        else:
            post_obj.post_likes.add(user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.filter(parent=None).exclude(status="removed").order_by('-create_date')
    serializer_class = CommentSerializer

    def destroy(self, request, pk, *args, **kwargs):
        user = request.user
        comment = self.get_object()
        if comment.creator == user:
            comment.remove()
            return Response({"msg": "삭제 되었습니다"}, status=status.HTTP_200_OK)
        else:
            return Response({"msg": "댓글 작성자가 아닙니다."}, status=status.HTTP_400_BAD_REQUEST)

    def like(self, request, *args, **kwargs):
        user = request.user
        comment = self.get_object()
        comment_obj = Comment.objects.get(pk=comment.id)

        if comment_obj.comment_likes.filter(id=user.id).exist():
            comment_obj.comment_likes.remove(user)
        else:
            comment_obj.comment_likes.add(user)
