from django.db import models
from django.contrib.auth.models import User
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


class Profile(models.Model):
	Gender_CHOICES  = (
		('Male','Male'),
		('Female','Female'),
	)
	
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(default='default.png',upload_to='profile_pics', blank=True, null=True)
	avatar_thumbnail = ImageSpecField(source='image', processors=[ResizeToFill(400, 400)], format='PNG', options={'quality': 80})
	gender = models.CharField(max_length=6, blank=False, null=False, default='Male', choices=Gender_CHOICES)

	def __str__(self):
		return f'{self.user.username} Profile'