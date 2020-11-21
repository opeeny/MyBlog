from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

#For every user created, they get a default profile picture I.E default.png
#To avoid going to the admin page create a profile for every user, DJANGO-SIGNAL, to get post-save signal
@receiver(post_save, sender = User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        profile.objects.create(user = instance)

#create user profile that saves our profile every time a user is created
@receiver(post_save, sender = User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()