from django.db.models.signals import post_save,pre_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


@receiver(pre_save, sender=Profile)
def set_profile_image(sender, instance, *args, **kwargs):

    # Obtain the gender of the just created user
    gender = Profile.objects.all().last().gender

    # Check for the gender and assign the file
    if gender == 'Male' and instance.image == 'default.png':
        instance.image = 'default_m.png'
    elif gender == 'Female' and instance.image == 'default.png':
        instance.image = 'default_f.png'


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
    
    