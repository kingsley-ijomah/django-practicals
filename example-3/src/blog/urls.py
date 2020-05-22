from django.urls import path
from blog.views import HomePageView, ListPageView

# enables namespacing
app_name = 'blog'

urlpatterns = [
    path('', HomePageView.as_view(), name='home-page'),
    path('posts/', ListPageView.as_view(), name='list-page')
]
