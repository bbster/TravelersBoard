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
            'id',
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
            'id',
            'post',
            'content',
            'creator',
            'create_date',
            'parent',
        )

    def get_parent(self, instance):
        serializer = self.__class__(instance.parent, many=True)
        serializer.bind('', self)
        return serializer.data


class CommentSerializer(serializers.ModelSerializer):
    childs = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = (
            'id',
            'post',
            'content',
            'creator',
            'create_date',
            'parent',
            'childs',
        )

    def get_childs(self, instance):
        # recursive
        serializer = self.__class__(instance.childs, many=True)
        serializer.bind('', self)
        return serializer.data
