from django.shortcuts import render
from django.views.generic import ListView, DetailView
from Blog.models import Post
from django.http import JsonResponse
# Create your views for the app Logic here.

class PostList(ListView):
    model = Post

class PostDetail(DetailView):
    model = Post
def likeView(request):
    if request.method == "GET":
        i = request.GET.get('i', None)
        p = Post.objects(id=1)
        p.likes = p.likes + 1
        p.save()
        data = {'i' : p.likes}
        return JsonResponse(data)
    