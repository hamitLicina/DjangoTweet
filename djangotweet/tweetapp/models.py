from django.db import models
from django.contrib.auth.models import User

class Tweet(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tweets', null=True)
    message = models.CharField(max_length=280)
    date = models.DateTimeField(auto_now_add=True, db_index=True)
    likes = models.ManyToManyField(User, related_name='liked_tweets', blank=True)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies')
    
    class Meta:
        ordering = ['-date']
        indexes = [
            models.Index(fields=['-date']),
        ]

    def __str__(self):
        return f"{self.username.username}: {self.message[:50]}"
    
    def get_likes_count(self):
        return self.likes.count()
    
    def get_replies_count(self):
        return self.replies.count()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=160, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', default='profile_pics/default.png')
    following = models.ManyToManyField('self', symmetrical=False, related_name='followers', blank=True)
    
    def __str__(self):
        return f"{self.user.username}'s profile"
    
    def get_following_count(self):
        return self.following.count()
    
    def get_followers_count(self):
        return self.followers.count()

