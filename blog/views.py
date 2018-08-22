from django.shortcuts import render
from .models import Post, Comment, Like
from django.views.decorators.http import require_GET
from django.views.decorators.csrf import csrf_exempt
from django.http.response import HttpResponse
import datetime
from django.shortcuts import get_object_or_404, get_list_or_404


def index(request):
    return render(request, 'blog/index.html')


@require_GET
def posts(request):
    posts = get_list_or_404(Post.published)
    return render(request, 'blog/posts.html', {'posts': posts})


@csrf_exempt
def post(request, year, month, day, title):
    post = get_object_or_404(Post.published, title=title)

    if request.method == 'GET':
        return render(request, 'blog/post.html', {'post': post})
    elif request.method == 'POST':
        pass
