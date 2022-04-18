from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill, ResizeToFill


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='posts_pic',null=True,blank=True)
    image_thumbnail = ImageSpecField(source='image', processors=[ResizeToFill(560, 350)], format='PNG', options={'quality': 80})


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
    

class Contact(models.Model):
    name=models.CharField(max_length=50,null=False, blank=False)
    email=models.EmailField(max_length=50,null=False, blank=False)
    message=models.TextField(null=False, blank=False)
    
    def __str__(self):
        return f'Message from {self.name}'
    
class Newsletter(models.Model):
    email=models.EmailField(max_length=50,null=False, blank=False)
    subscribe_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.email
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        
        return email
