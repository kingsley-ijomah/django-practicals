from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm


def list_post(request):
    posts = Post.objects.all()
    return render(request, 'index.html', context={'posts': posts})


def create_post(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        title = form.cleaned_data['title']
        content = form.cleaned_data['content']
        Post.objects.create(title=title, content=content)
        return redirect('list-post')

    return render(request, 'new.html', context={'form': form})


def update_post(request, id):
    post = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, initial={
        'title': post.title, 'content': post.content})

    if request.method == 'POST':
        if form.is_valid():
            post.title = form.cleaned_data['title']
            post.content = form.cleaned_data['content']
            post.save()
        return redirect('list-post')

    return render(request, 'update.html', context={'form': form})


def delete_post(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect('list-post')
