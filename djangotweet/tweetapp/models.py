from django.db import models

# Create your models here.

class Tweet(models.Model):
    nickname = models.CharField(max_length=20)
    message = models.CharField(max_length=140)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Tweet Nick: {self.nickname} - Tweet Message: {self.message} - Date: {self.date}"
    
    