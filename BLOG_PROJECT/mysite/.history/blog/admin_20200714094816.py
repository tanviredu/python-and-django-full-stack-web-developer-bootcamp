from django.contrib import admin
from .models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title' 'author', 'created_date')
    list_filter = ('author', 'created_date')
    search_fields = ('author', 'created_date')
    date_hierarchy = 'created_date'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'author', 'created_date')
    list_filter = ('id', 'post', 'author', 'created_date')
    search_fields = ('id', 'post', 'author', 'approved_comment')
    date_hierarchy = 'created_date'
