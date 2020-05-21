from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()

    def get_update_url(self):
        return reverse('blog:update-page', args=[str(self.id)])

    def get_delete_url(self):
        return reverse('blog:delete-page', args=[str(self.id)])
