from rest_framework import viewsets
from .models import Post
from .serializers import PostSerializer

class PostViewset(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer