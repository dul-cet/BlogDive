from django.db import models
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth.models import User

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)  
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

#custom model
#возвращает все комментарии, которые были созданы в последние 7 дней.
class RecentCommentManager(models.Manager):
    def recent(self):
        week_ago = timezone.now() - timedelta(days=7)
        return self.filter(created_at__gte=week_ago)
    


class Comment(models.Model):
    text = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)  
    created_at = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()  # стандартный менеджер
    recent_comments = RecentCommentManager()  # кастомный менеджер
    def __str__(self):
          return f'Comment on "{self.post.title}" by {self.author.username}'


class Follow(models.Model):
    follower = models.ForeignKey(User, related_name='following', on_delete=models.CASCADE)
    following = models.ForeignKey(User, related_name='followers', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
          unique_together = ('follower', 'following')

    def __str__(self):
         return f'{self.follower} follows {self.following}'
    
    
    
class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Notification for {self.user.username}: {self.message}'
    

class Project(models.Model):
    name = models.CharField(max_length=100)

class ProjectFollow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.follower} follows {self.project}'
