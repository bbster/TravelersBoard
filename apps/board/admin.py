from django.contrib import admin
from .models import Board, Post, Comment


class BoardAdmin(admin.ModelAdmin):
    fields = ['unique_title']
    list_display = ['id', 'unique_title', 'create_date', 'modify_date']


class PostAdmin(admin.ModelAdmin):
    fields = ['board', 'title', 'content', 'tag', 'creator', 'status']
    list_display = ['id', 'board', 'title', 'content', 'tag', 'creator', 'create_date', 'modify_date', 'status']


class CommentAdmin(admin.ModelAdmin):
    fields = ['post', 'content', 'parent', 'creator', 'status']
    list_display = ['id', 'post', 'content', 'creator', 'parent', 'create_date', 'status']


admin.site.register(Board, BoardAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
