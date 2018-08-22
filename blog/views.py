from django.shortcuts import render
from .models import Post, Comment, Like
from django.views.decorators.http import require_GET
from django.views.decorators.csrf import csrf_exempt
from django.http.response import HttpResponse


def index(request):
    return render(request, 'blog/index.html')


@require_GET
def posts(request):
    return render(request, 'blog/posts.html')


@require_GET
def post(request, year, month, day, title):
    return HttpResponse('OK, that regex was correct year: {}, month: {}, day: {}, title: {}'
                        .format(year, month, day, title))
