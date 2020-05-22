from django.shortcuts import render
from django.views import generic
from django.shortcuts import redirect
from django.urls import reverse_lazy
from .models import Post


class HomePageView(generic.TemplateView):
    template_name = 'home.html'


class ListPageView(generic.ListView):
    model = Post
