from django.contrib import admin

from .models import Comment, Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "title",
        "post_body",
        "user_type",
        "created_at",
        "updated_at"
    ]
    search_fields = ["title"]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "post",
        "user_type",
        "comment_body",
        "created_at",
        "updated_at",
    ]
    search_fields = ["post"]
