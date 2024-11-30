from django.shortcuts import render
from . import models

# Create your views here.

def listtweet(request):
    all_tweets = models.Tweet.objects.all()
    tweet_dict = {"tweets": all_tweets}
    return render(request, 'tweetapp/listtweet.html', context=tweet_dict)

def addtweet(request):
    if request.POST:
        nickname = request.POST["nickname"]
        message = request.POST["message"]
        new_tweet = models.Tweet(nickname=nickname, message=message)
        new_tweet.save()
    return render(request, 'tweetapp/addtweet.html')

def profile(request):
    return render(request, 'tweetapp/profile.html')
