from django.contrib import admin
from .models import Category, Post, Comment

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'date_posted']
    list_filter = ['date_posted', 'categories']
    search_fields = ['title', 'content']
    filter_horizontal = ['categories']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['post', 'author', 'date_posted']
    list_filter = ['date_posted']
    search_fields = ['content', 'author__username', 'post__title']