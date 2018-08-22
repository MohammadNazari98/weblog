from django.shortcuts import render
from django.views.decorators.http import require_GET
from django.shortcuts import get_object_or_404, get_list_or_404
from django.db.utils import IntegrityError
from .forms import AddNewComment, AddNewLike
from .models import Post


def index(request):
    return render(request, 'blog/index.html')


@require_GET
def posts(request):
    posts = get_list_or_404(Post.published)
    return render(request, 'blog/posts.html', {'posts': posts})


def post(request, year, month, day, title):
    # TODO: using date for filtering post
    post = get_object_or_404(Post.published, title=title)

    if request.method == 'GET':
        comment_form = AddNewComment()
        like_form = AddNewLike()
        return render(request, 'blog/post.html', {'post': post, 'comment_form': comment_form, 'like_form': like_form})

    elif request.method == 'POST':

        if request.POST['source'] == 'like_form':
            like_form = AddNewLike(request.POST)

            if like_form.is_valid():
                new_like = like_form.save(commit=False)
                # TODO: using date for filtering post
                post_title = request.path.split('/')[-2]
                post = Post.published.get(title=post_title)
                try:
                    new_like.post = post
                    new_like.save()
                    result = {'title': 'success', 'body': 'successfully added', 'url': request.path}
                except IntegrityError:
                    result = {'title': 'failed',
                              'body': 'Error: you can only add one like or dislike per post',
                              'url': request.path}
            else:
                result = {'title': 'failed', 'body': 'could not added', 'url': request.path}

            return render(request, 'blog/result.html', result)

        elif request.POST['source'] == 'comment_form':
            comment_form = AddNewComment(request.POST)

            if comment_form.is_valid():
                new_comment = comment_form.save(commit=False)
                # TODO: using date for filtering post
                post_title = request.path.split('/')[-2]
                post = Post.published.get(title=post_title)
                try:
                    new_comment.post = post
                    new_comment.save()
                    result = {'title': 'success', 'body': 'successfully added', 'url': request.path}
                except IntegrityError:
                    result = {'title': 'failed',
                              'body': 'Error: you can only add one comment per post',
                              'url': request.path}
            else:
                result = {'title': 'failed', 'body': 'Error: could not added', 'url': request.path}

            return render(request, 'blog/result.html', result)
