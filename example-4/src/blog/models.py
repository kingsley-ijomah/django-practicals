from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

STATUS = (
    (0, 'Draft'),
    (1, 'Publish')
)


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts')
    tag = models.ManyToManyField(Tag)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    content = models.TextField()

    def get_update_url(self):
        return reverse('blog:update-page', args=[str(self.id)])

    def get_delete_url(self):
        return reverse('blog:delete-page', args=[str(self.id)])

    def get_details_url(self):
        return reverse('blog:detail-page', args=[str(self.slug)])

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    content = models.TextField()
    active = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.content, self.name)
