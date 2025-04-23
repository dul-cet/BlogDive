from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Follow, Notification, Post, Comment, Project, ProjectFollow
from .serializers import FollowSerializer, PostSerializer, CommentSerializer, ProjectFollowSerializer, SimpleNotificationsSerializer
from rest_framework.views import APIView
from .models import Post
from .serializers import PostSerializer
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
    
#class-based view for creting post
class PostCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        post = Post.objects.create(
            title=request.data['title'], 
            content=request.data['content'],
            category_id=request.data['category'],  
            author=request.user
        )
        serializer = PostSerializer(post)
        return Response(serializer.data, status=status.HTTP_201_CREATED)




# Function-Based View for Listing Posts
@api_view(['GET'])
def post_list(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

# Class-Based View for a single Post
class PostDetail(APIView):
    def get(self, request, pk):
        try:
            post = Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def put(self, request, pk):
        post = Post.objects.get(pk=pk)

        if post.author != request.user:
            return Response({'detail': 'You are not the author of the post'}, status=status.HTTP_403_FORBIDDEN)

        serializer = PostSerializer(post, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        post = Post.objects.get(pk=pk)
        if post.author != request.user:
            return Response({'detail': 'You are not the author of the post'}, status=status.HTTP_403_FORBIDDEN)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Class-Based View for Listing Comments on a Post
class CommentList(APIView):
    def get(self, request, post_id):
        comments = Comment.objects.filter(post_id=post_id)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)


# Function-Based View for Creating a Comment
@api_view(['POST'])
def create_comment(request, post_id):
    if not request.user.is_authenticated:
        return Response({"detail": "Authentication credentials were not provided."}, status=status.HTTP_401_UNAUTHORIZED)
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        return Response({"detail": "Post not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(post=post, author=request.user)  # автор комментарии сохраняется

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#удалить и редактировать свои комментарии
class CommentDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            return None

    def put(self, request, pk):
        comment = self.get_object(pk)
        if comment is None:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if comment.author != request.user:
            return Response({'detail': 'You can only edit your own comment'}, status=status.HTTP_403_FORBIDDEN)

        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        comment = self.get_object(pk)
        if comment is None:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if comment.author != request.user:
            return Response({'detail': 'You can only delete your own comment'}, status=status.HTTP_403_FORBIDDEN)

        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




# Функциональный View для создания подписки (Follow)
@api_view(['POST'])
def create_follow(request):
    if not request.user.is_authenticated:
        return Response({"detail": "Authentication credentials were not provided."}, status=status.HTTP_401_UNAUTHORIZED)
    
    following_user_id = request.data.get('following_id')
    try:
        following_user = User.objects.get(id=following_user_id)
    except User.DoesNotExist:
        return Response({"detail": "User not found."}, status=status.HTTP_404_NOT_FOUND)

    if following_user == request.user:
        return Response({"detail": "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)

    follow, created = Follow.objects.get_or_create(follower=request.user, following=following_user)
    if created:
        return Response(FollowSerializer(follow).data, status=status.HTTP_201_CREATED)
    return Response({"detail": "Already following."}, status=status.HTTP_400_BAD_REQUEST)

# Функциональный View для получения уведомлений
@api_view(['GET'])
def get_notifications(request):
    if not request.user.is_authenticated:
        return Response({"detail": "Authentication credentials were not provided."}, status=status.HTTP_401_UNAUTHORIZED)
    
    notifications = Notification.objects.filter(user=request.user)
    serializer = SimpleNotificationsSerializer(notifications, many=True)
    return Response(serializer.data)

# Функциональный View для создания уведомлений
@api_view(['POST'])
def create_notification(request):
    if not request.user.is_authenticated:
        return Response({"detail": "Authentication credentials were not provided."}, status=status.HTTP_401_UNAUTHORIZED)
    
    message = request.data.get('message')
    notification = Notification.objects.create(user=request.user, message=message)
    return Response(SimpleNotificationsSerializer(notification).data, status=status.HTTP_201_CREATED)

# Функциональный View для подписки на проект
@api_view(['POST'])
def create_project_follow(request):
    if not request.user.is_authenticated:
        return Response({"detail": "Authentication credentials were not provided."}, status=status.HTTP_401_UNAUTHORIZED)
    
    project_id = request.data.get('project_id')
    try:
        project = Project.objects.get(id=project_id)
    except Project.DoesNotExist:
        return Response({"detail": "Project not found."}, status=status.HTTP_404_NOT_FOUND)

    project_follow, created = ProjectFollow.objects.get_or_create(follower=request.user, project=project)
    if created:
        return Response(ProjectFollowSerializer(project_follow).data, status=status.HTTP_201_CREATED)
    return Response({"detail": "Already following this project."}, status=status.HTTP_400_BAD_REQUEST)





# Login (obtain token)
# URL: /api/token/login/
class LoginView(APIView):
    def post(self, request):
        return obtain_auth_token(request)

# Logout (delete token)
# URL: /api/token/logout/
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        request.user.auth_token.delete()  # Delete token from database
        return Response(status=status.HTTP_200_OK)
