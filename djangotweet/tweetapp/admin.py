from django.contrib import admin
from .models import *
from tweetapp.models import Tweet

class TweetAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Nickname Group", {"fields": ["nickname"]}),
        ("Message Group", {"fields": ["message"]}),
        ("Date Group", {"fields": ["date"]}),
    ]
    # fields = ['message', 'nickname']
# Register your models here.
admin.site.register(Tweet, TweetAdmin)