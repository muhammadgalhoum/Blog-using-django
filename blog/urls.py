from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView
)
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('search', views.search, name='search_post'),
    path('contact/', views.contact, name='contact'),
    path('subscribe/', views.subscribe, name='newsletter'),
    path('about/', views.about, name='blog-about'),
]

# Type of Path Converters
"""
int:numbers
str:string
path:whole urls 
slug:hyphen(-)and(_)underscore_stuff
UUID:universally unique identifer

"""