from django.urls import path
from blog.views import HomePageView, CreatePostView, UpdatePostView, ListPageView, DeletePostView

# enables namespacing
app_name = 'blog'

urlpatterns = [
    path('', HomePageView.as_view(), name='home-page'),
    path('posts/', ListPageView.as_view(), name='list-page'),
    path('posts/new/', CreatePostView.as_view(), name='create-page'),
    path('posts/update/<pk>/', UpdatePostView.as_view(), name='update-page'),
    path('posts/delete/<pk>/', DeletePostView.as_view(), name='delete-page')
]
