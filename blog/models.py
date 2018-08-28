from datetime import datetime
from django.db import models
from weblog.settings import AUTH_USER_MODEL
from django.core.exceptions import ValidationError


class PublishedPostsManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(
            is_enable=True, status=Post.PUBLISH_STATUS, publish_date__lte=datetime.now().date()).order_by(
            '-publish_date', '-last_modified')


class Post(models.Model):
    DRAFT_STATUS = 1
    PUBLISH_STATUS = 2

    STATUS_CHOICES = (
        (DRAFT_STATUS, 'Draft'),
        (PUBLISH_STATUS, 'Publish'),
    )

    title = models.CharField(max_length=120)
    url = models.SlugField(max_length=120, db_index=True, allow_unicode=True, default='')
    content = models.TextField()
    created_time = models.DateTimeField('created time', auto_now_add=True)
    last_modified = models.DateTimeField('updated time', auto_now=True)
    publish_date = models.DateField('publish date', null=True)
    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICES, default=1)
    author = models.ForeignKey(AUTH_USER_MODEL)
    is_enable = models.BooleanField(default=True)

    published = PublishedPostsManager()
    objects = models.Manager()

    def __str__(self):
        return f'{self.author} --> {self.title}'

    def clean(self):
        if self.status == Post.DRAFT_STATUS and self.publish_date is not None:
            raise ValidationError('Draft posts can\'t have publish date.')
        if self.status == Post.PUBLISH_STATUS and self.publish_date is None:
            raise ValidationError('Publication posts should have publish date.')

    def count_of_likes(self):
        return self.likes.filter(is_like=True).count()

    def count_of_dislikes(self):
        return self.likes.filter(is_like=False).count()


class ActivesCommentsManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_enable=True).order_by('-created_time')


class Comment(models.Model):
    content = models.TextField()
    created_time = models.DateTimeField('sent time', auto_now_add=True)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    post = models.ForeignKey(Post, related_name='comments')
    is_enable = models.BooleanField(default=True)

    actives = ActivesCommentsManager()
    objects = models.Manager()

    class Meta:
        unique_together = ('post', 'email')

    def __str__(self):
        return f'{self.name} --> {self.post.title}'


class Like(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    is_like = models.BooleanField(default=True)
    post = models.ForeignKey(Post, related_name='likes')

    class Meta:
        unique_together = ('post', 'email')

    def __str__(self):
        return f'{self.name} --> {self.post.title}'
