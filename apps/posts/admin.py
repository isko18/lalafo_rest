from django.contrib import admin
from apps.posts.models import Post, FavoritePost

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "description", "price", "category", "is_active"]

@admin.register(FavoritePost)
class FavoritePostDmin(admin.ModelAdmin):
    list_display = ['user', 'post']
    list_per_page = 20

