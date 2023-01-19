from django import forms
from django.core.exceptions import ValidationError
from .models import *


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'name_news',
            'text_news',
            'author',
            'category'
        ]

