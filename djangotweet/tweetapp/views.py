from django.shortcuts import render, redirect
from . import models
from django.urls import reverse
from django import forms
from . import forms

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
        return redirect(reverse('tweetapp:listtweet'))
    else:
        return render(request, 'tweetapp/addtweet.html')    

def profile(request):
    return render(request, 'tweetapp/profile.html')

def addtweetbyform(request):
    if request.method == 'POST':
        form = forms.AddTweetForm(request.POST)
        if form.is_valid():
            nickname = form.cleaned_data['nickname']
            message = form.cleaned_data['message']
            new_tweet = models.Tweet(nickname=nickname, message=message)
            new_tweet.save()
            return redirect(reverse('tweetapp:listtweet'))
        else:
            print("Error in form!")
            return render(request, 'tweetapp/addtweetbyform.html', context={'form': form})
        
