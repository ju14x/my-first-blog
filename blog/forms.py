from dataclasses import fields
from socket import fromshare # remove from linux hosts since this import is only for windows
from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text')

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text')
