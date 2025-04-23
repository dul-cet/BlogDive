
from django.contrib import admin
from django.urls import path, include
from api.views import CommentList, LoginView, LogoutView, PostCreateView, PostDetail, create_comment, post_list, CommentDetail
from rest_framework.authtoken.views import obtain_auth_token
from django.http import HttpResponse



def home(request):
    return HttpResponse("Welcome to BlogDive!")
urlpatterns = [
 
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('logout/', LogoutView.as_view(), name='logout'),

   
    path('create-post/', PostCreateView.as_view(), name='create_post'),

    path('posts/', post_list, name='post-list'),
    path('posts/<int:pk>/', PostDetail.as_view(), name='post-detail'),
    path('posts/<int:post_id>/comments/', CommentList.as_view(), name='comment-list'),
    path('posts/<int:post_id>/comment-create/', create_comment, name='comment-create'),
    path('comments/<int:pk>/', CommentDetail.as_view(), name='comment-detail'),

     # DRF's built-in token-based login view 
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('', home, name='home'),
]
