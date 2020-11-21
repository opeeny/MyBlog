from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 100)
    # author = models.ForeignKey(User, on_delete = models.CASCADE)
    author = models.CharField(max_length = 100)
    description = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)
    post_image = models.ImageField(upload_to='uploads/')
    likes = models.IntegerField(default=0)
  
    def __str__(self):
        return self.title #this returns the title of the blog post

class Profile(models.Model):
    user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'uploads', default = "default.png")
    description= models.TextField(blank=True, max_length=100)
    first_name = models.CharField(max_length=64)
    
    def __str__(self):
        return f'{self.user.username} Profile'

#Owned Model
class OwnedModel(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)

    class Meta:
        abstract = True
class Post(OwnedModel):
    title = models.CharField(max_length=100)