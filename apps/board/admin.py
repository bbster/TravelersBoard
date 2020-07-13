from django.contrib import admin
from .models import Board, Post, Comment


class BoardAdmin(admin.ModelAdmin):
    fields = ['unique_title']
    list_display = ['unique_title', 'create_date', 'modify_date']


class PostAdmin(admin.ModelAdmin):
    fields = ['board', 'title', 'content', 'creator']
    list_display = ['board', 'title', 'content', 'creator', 'create_date', 'modify_date']


class CommentAdmin(admin.ModelAdmin):
    fields = ['post', 'content', 'parent', 'creator']
    list_display = ['post', 'content', 'creator', 'parent', 'create_date']


admin.site.register(Board, BoardAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
