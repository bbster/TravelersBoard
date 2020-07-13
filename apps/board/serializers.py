from rest_framework import serializers

from apps.board.models import Board, Comment, Post


class BoardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Board
        fields = (
            'unique_title',
            'creator',
        )


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = (
            'board',
            'title',
            'content',
            'creator',
            'create_date',
            'modify_date',
        )


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = (
            'post',
            'content',
            'creator',
            'create_date',
            'parent',
        )
