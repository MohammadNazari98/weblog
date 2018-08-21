from django.db import models
from django.conf.global_settings import AUTH_USER_MODEL

DRAFT_STATUS = 1
PUBLISH_STATUS = 2

STATUS_CHOICES = (
    (DRAFT_STATUS, 'Draft'),
    (PUBLISH_STATUS, 'Publish'),
)


class Post(models.Model):
    title = models.CharField(max_length=120, null=False, blank=False)
    content = models.TextField(null=False, blank=False)
    created_time = models.DateTimeField('created time', auto_now_add=True)
    last_modified = models.DateTimeField('updated time', auto_now=True)
    # TODO: publish time
    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICES, default=1)
    author = models.ForeignKey(AUTH_USER_MODEL)
    is_enable = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.author} --> {self.title}'


class Comment(models.Model):
    content = models.TextField(null=False, blank=False)
    created_time = models.DateTimeField('sent time', auto_now_add=True)
    name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    post = models.ForeignKey(Post)
    is_enable = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name} --> {self.post.title}'
