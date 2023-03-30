from django.urls import path
from .views import *
from .views import *

urlpatterns = [
	path('', PostListView.as_view(), name='home'),
	path('post/<int:pk>/', post_detail, name='post-detail'),
	path('post/new/', PostCreateView.as_view(), name='post-create'),
	path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
	path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
  path('post-like/<int:pk>', postLike, name="post_like"),
	path('fav/<int:id>/', favourite_post, name='favourite_post'),
	path('last_five_posts/', last_five_posts, name='last_five_posts'),
	path('favourite_posts/', favourite_posts, name='favourite_posts'),
	path('comment/<int:id>', delete_comment, name='delete-comment'),
	path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
	path('show_categories/', show_categories, name='show_categories'),
  path('category/posts/<int:pk>',PostCategoryListView.as_view(), name='posts_by_category'),
	path('category/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
	path('category/new/', CategoryCreateView.as_view(), name='category-create'),
	path('category/<int:pk>/update',CategoryUpdateView.as_view(), name='category-update'),
	path('category/<int:pk>/delete',CategoryDeleteView.as_view(), name='category-delete'),
	path('latest_jobs/', latest_jobs, name='latest_jobs'),
	path('search', search, name='search_post'),
	path('contact/', contact, name='contact'),
	path('subscribe/', subscribe, name='newsletter'),
	path('about/', about, name='about'),
]

# Type of Path Converters
"""
int:numbers
str:string
path:whole urls 
slug:hyphen(-)and(_)underscore_stuff
UUID:universally unique identifer

"""