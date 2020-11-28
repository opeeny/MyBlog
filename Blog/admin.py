from django.contrib import admin
from Blog.models import Post
from .models import Profile

# Register your models here.
admin.site.register(Post)
admin.site.register(Profile)
