from django.contrib import admin
from .models import Post, Comment, Like


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass


admin.site.register(Comment)
admin.site.register(Like)
