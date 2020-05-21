from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    title = forms.CharField(max_length=150)
    content = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Post
