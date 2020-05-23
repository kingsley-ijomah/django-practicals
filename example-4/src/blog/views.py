from django.shortcuts import render
from django.views import generic
from django.shortcuts import redirect
from django.urls import reverse
from .models import Post
from .forms import CommentForm
from django.views.generic.detail import SingleObjectMixin
from django.views import View


class HomePageView(generic.TemplateView):
    template_name = 'home.html'


class ListPageView(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    paginate_by = 2


class PostDisplay(generic.DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        post = Post.objects.filter(id=self.object.id)
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context


class PostComment(SingleObjectMixin, generic.FormView):
    template_name = 'post_detail.html'
    form_class = CommentForm
    model = Post

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        form = self.get_form()

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = self.object
            comment.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_success_url(self):
        return reverse('blog:detail-page', args=[str(self.object.slug)])


class DetailPageView(View):
    def get(self, request, *args, **kwargs):
        view = PostDisplay.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = PostComment.as_view()
        return view(request, *args, **kwargs)
