from django.urls import path
from Blog.views import PostList, PostDetail, likeView, Profile
from . import views

app_name = "Blog"
urlpatterns = [
    path('', PostList.as_view(), name='post-list'),
    path('signin/', views.signin, name="signin"),
    # path('user_login/', views.user_login, name="user_login"),
    path('signup/', views.signup, name="signup"),
    path('user_signup/', views.user_signup, name="user_signup"),
    path('prof/', Profile, name = 'profile'),
    path('detail/<int:pk>/', PostDetail.as_view(), name='post-detail'),
    path('ajax/likes/', likeView, name='like')
]