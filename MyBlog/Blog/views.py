from django.shortcuts import render
from django.views.generic import ListView, DetailView
from Blog.models import Post, Profile
from django.http import JsonResponse
from .forms import Signin
from .forms import Signup
# Create your views for the app Logic here.


def index(request):
    username = None
    blog_list = None
    #comment_form = CommentForm()
    if request.user:
        user = request.user
        blog_list = Blog.objects.order_by('-created_date')
        context = {
            'user': user,
            'blog_list':blog_list, 
            'comment_form': comment_form,
            'Blog': Blog
            }
    return render(request,'Blog/base.html',context)
    
def signin(request):
    form = Signin()
    return render(request, 'Blog/signin.html', context={'form': form})

# def user_login(request):
#     if request.method =='POST':
#         # form = SignupForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(request, username = username, password = password)
#             print(user)
#             if user is not None:
#                 login(request, user)
#                 return redirect(reverse('index'))
#             else:
#                 return HttpResponse('Invalid log In')
def signup(request):
    form = Signup()
    return render(request, 'Blog/signup.html', context={'form': form})
    #
def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            try:
                user_check = User.objects.get(username=username)
                return HttpResponse("User already exists")
            except User.DoesNotExist:

                user = User.objects.create_user(username=username, password=password)
                user.save()
                print(user)
                return redirect(reverse('index'))

class ProfileView(DetailView):
    model = Profile
    
class PostList(ListView):
    model = Post

class PostDetail(DetailView):
    model = Post
def likeView(request):
    if request.method == "GET":
        i = request.GET.get('i', None)
        # p = Post.objects(id=1)
        p = Post.objects.first
        p.likes = p.likes + 1
        p.save()
        data = {'i' : p.likes}
        return JsonResponse(data)

#class ProfileView(DetailView):
    