from django.contrib import admin

from .models import Post, Category, Comment, Like


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'author',
        'category',
        'published',
        'views',
        'created_at',
    )

    list_filter = (
        'published',
        'category',
        'created_at',
    )

    search_fields = (
        'title',
        'content',
        'author__username',
    )
    prepopulated_fields = {
        'slug': ('title',)
    }


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'post',
        'user',
        'text',
        'created_at',
    )

    list_filter = (
        'created_at',
    )

    search_fields = (
        'text',
        'user__username',
        'post__title',
    )


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = (
        'post',
        'user',
        'created_at',
    )

    list_filter = (
        'created_at',
    )

    search_fields = (
        'user__username',
        'post__title',
    )