from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


class Category(models.Model):
	name = models.CharField(max_length=100, unique=True,null=False, blank=False)
	catrgory_author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
  
	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('posts_by_category', args=[self.name])

	def get_absolute_url(self):
		return reverse('category-detail', kwargs={'pk': self.pk})


class Post(models.Model):
	title = models.CharField(max_length=100, null=False, blank=False)
	content = models.TextField(null=False, blank=False)
	date_posted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	image = models.ImageField(upload_to='posts_pic',null=True,blank=True)
	image_thumbnail = ImageSpecField(source='image', processors=[ResizeToFill(560, 350)], format='PNG', options={'quality': 80})
	category = models.ForeignKey(Category, null=False, blank=False, on_delete=models.CASCADE)
	favourite = models.ManyToManyField(User, related_name="favourite")
	likes = models.ManyToManyField(User, related_name="post_like")
  
	def __str__(self):
		return self.title
  
	def total_likes(self):
		return self.likes.count()

	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk': self.pk})


class Comment(models.Model):
	post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	content = models.TextField(null=False, blank=False)
	comment_date = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		return f'{self.user.username} comments on {self.post.title} post.'



class Contact(models.Model):
	name = models.CharField(max_length=50,null=False, blank=False)
	email = models.EmailField(max_length=50,null=False, blank=False)
	message = models.TextField(null=False, blank=False)
	contact_date = models.DateTimeField(default=timezone.now)

	
	def __str__(self):
		return f'Message from {self.name}'


class Newsletter(models.Model):
	email = models.EmailField(max_length=50,null=False, blank=False)
	subscribe_date = models.DateTimeField(default=timezone.now)
	
	def __str__(self):
		return self.email
	
	def clean_email(self):
		email = self.cleaned_data.get('email')
		return email