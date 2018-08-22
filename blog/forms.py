from django import forms
from blog.models import Comment, Like


class AddNewComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'content')


class AddNewLike(forms.ModelForm):
    class Meta:
        model = Like
        fields = ('name', 'email', 'is_like')
