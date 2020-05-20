from django.urls import path
from .views import list_post, create_post, update_post, delete_post

urlpatterns = [
    path('', list_post, name='list-post'),
    path('posts/new/', create_post, name='create-post'),
    path('posts/update/<id>', update_post, name='update-post'),
    path('posts/delete/<id>', delete_post, name='delete-post')
]
