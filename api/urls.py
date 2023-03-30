from django.urls import path
from .views import *


urlpatterns = [
  path('category-list/', categoryList, name='api-category-list'),
  path('category-detail/<int:pk>', categoryDetail, name='api-category-detail'),
  path('category-create/', categoryCreate, name='api-category-create'),
  path('category-update/<int:pk>', categoryUpdate, name='api-category-update'),
  path('category-delete/<int:pk>', categoryDelete, name='api-category-delete'),
  
  path('post-list/', postList, name='api-post-list'),
  path('post-detail/<int:pk>', postDetail, name='api-post-detail'),
  path('post-create/', postCreate, name='api-post-create'),
  path('post-update/<int:pk>', postUpdate, name='api-post-update'),
  path('post-delete/<int:pk>', postDelete, name='api-post-delete'),
  
  path('comment-list/', commentList, name='api-comment-list'),
  path('comment-detail/<int:pk>', commentDetail, name='api-comment-detail'),
  path('comment-create/', commentCreate, name='api-comment-create'),
  path('comment-update/<int:pk>', commentUpdate, name='api-comment-update'),
  path('comment-delete/<int:pk>', commentDelete, name='api-comment-delete'),
  
  path('contact-list/', contactList, name='api-contact-list'),
  path('contact-detail/<int:pk>', contactDetail, name='api-contact-detail'),
  path('contact-create/', contactCreate, name='api-contact-create'),
  path('contact-update/<int:pk>', contactUpdate, name='api-contact-update'),
  path('contact-delete/<int:pk>', contactDelete, name='api-contact-delete'),
  
  path('newsletter-list/', newslettertList, name='api-newsletter-list'),
  path('newsletter-detail/<int:pk>', newsletterDetail, name='api-newsletter-detail'),
  path('newsletter-create/', newsletterCreate, name='api-newsletter-create'),
  path('newsletter-update/<int:pk>', newsletterUpdate, name='api-newsletter-update'),
  path('newsletter-delete/<int:pk>', newsletterDelete, name='api-newsletter-delete'),
]
