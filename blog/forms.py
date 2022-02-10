from dataclasses import fields
from socket import fromshare # remove from linux hosts since this import is only for windows
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text')
