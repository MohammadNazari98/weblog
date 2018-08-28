from django.shortcuts import render
from django.views.decorators.http import require_GET
from django.contrib.auth import authenticate, login
from django.shortcuts import get_object_or_404, get_list_or_404
from django.db.utils import IntegrityError
from django.views import View

from .forms import AddNewComment, AddNewLike, Login
from .models import Post


def index(request):
    return render(request, 'blog/index.html')


class LoginView(View):
    def get(self, request):
        login_form = Login()
        return render(request, 'blog/login.html', {'login_form': login_form})

    def post(self, request):
        login_form = Login(request.POST)

        if login_form.is_valid():
            cleaned_data = login_form.cleaned_data

            user = authenticate(username=cleaned_data['username'], password=cleaned_data['password'])
            if user is not None:
                login(request, user)
                result = {'title': 'success', 'body': 'you successfully login', 'url': request.path}
            else:
                result = {'title': 'failed', 'body': 'can\'t login :((', 'url': request.path}

            return render(request, 'blog/result.html', result)


@require_GET
def posts(request):
    posts = Post.published.all()
    return render(request, 'blog/posts.html', {'posts': posts})


def post(request, year, month, day, url):
    year, month, day = int(year), int(month), int(day)
    post = get_object_or_404(Post.published, url=url, publish_date__year=year, publish_date__month=month,
                             publish_date__day=day)

    if request.method == 'GET':
        comment_form = AddNewComment()
        like_form = AddNewLike()
        return render(request, 'blog/post.html', {'post': post, 'comment_form': comment_form, 'like_form': like_form})

    elif request.method == 'POST':

        if request.POST['source'] == 'like_form':
            like_form = AddNewLike(request.POST)

            if like_form.is_valid():
                new_like = like_form.save(commit=False)

                current_url = request.path.split('/')
                year, month, day = current_url[1], current_url[2], current_url[3]
                post_title = current_url[-2]

                post = Post.published.get(url=post_title, publish_date__year=year, publish_date__month=month,
                                          publish_date__day=day)
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

                current_url = request.path.split('/')
                year, month, day = current_url[1], current_url[2], current_url[3]
                post_title = current_url[-2]

                post = Post.published.get(url=post_title, publish_date__year=year, publish_date__month=month,
                                          publish_date__day=day)
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
