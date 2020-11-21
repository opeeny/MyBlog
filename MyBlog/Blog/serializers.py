from rest_framework import serializers
from . import models

class PostSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default = serializers.CurrentUserDefault())
    class Meta:
        model = models.Post
        fields = ('id', 'title', 'author', 'description', 'timestamp', 'img', 'likes') #takes a tuple of choices
        #fields = '__all__'
