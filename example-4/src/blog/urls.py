from django.urls import path
from blog.views import HomePageView, ListPageView, DetailPageView

# enables namespacing
app_name = 'blog'

urlpatterns = [
    path('', HomePageView.as_view(), name='home-page'),
    path('posts/', ListPageView.as_view(), name='list-page'),
    path('<slug:slug>/', DetailPageView.as_view(), name='detail-page')
]
