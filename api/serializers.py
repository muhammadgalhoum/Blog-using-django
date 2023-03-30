from rest_framework import serializers
from blog.models import *


class CategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = Category
    fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
  class Meta:
    model = Post
    fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Comment
    fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):
  class Meta:
    model = Contact
    fields = '__all__'


class NewsletterSerializer(serializers.ModelSerializer):
  class Meta:
    model = Newsletter
    fields = '__all__'