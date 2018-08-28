from django.contrib import admin
from .models import Post, Comment, Like


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"url": ("title",)}

    # return all posts even Drafts
    def get_queryset(self, request):
        return Post.objects.all()


admin.site.register(Comment)
admin.site.register(Like)
