from django.shortcuts import render
from django.views import generic
from django.shortcuts import redirect
from django.urls import reverse_lazy
from .models import Post


class HomePageView(generic.TemplateView):
    template_name = 'home.html'


class ListPageView(generic.ListView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CreatePostView(generic.CreateView):
    # template used: post_form.html
    model = Post
    fields = ['title', 'content']
    success_url = reverse_lazy('blog:list-page')


class UpdatePostView(generic.UpdateView):
    # template used: post_form.html
    model = Post
    fields = ['title', 'content']
    success_url = reverse_lazy('blog:list-page')


class DeletePostView(generic.DeleteView):
    model = Post
    success_url = reverse_lazy('blog:list-page')
