from django.shortcuts import render, redirect
from . import models
from django.urls import reverse, reverse_lazy
from django import forms
from .forms import AddTweetModelForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView

# Create your views here.

def listtweet(request):
    all_tweets = models.Tweet.objects.all()
    tweet_dict = {"tweets": all_tweets}
    return render(request, 'tweetapp/listtweet.html', context=tweet_dict)

@login_required(login_url='/login')
def addtweet(request):
    if request.POST:
        message = request.POST["message"]
        new_tweet = models.Tweet(username=request.user, message=message)
        new_tweet.save()
        return redirect(reverse('tweetapp:listtweet'))
    else:
        return render(request, 'tweetapp/addtweet.html')    

def profile(request):
    return render(request, 'tweetapp/profile.html')

def addtweetbyform(request):
    if request.method == 'POST':
        form = AddTweetModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('tweetapp:listtweet'))
        else:
            print("Error in form!")
            return render(request, 'tweetapp/addtweetbyform.html', context={'form': form})
    else:
        form = AddTweetModelForm()
        return render(request, 'tweetapp/addtweetbyform.html', context={'form': form})

def addtweetbymodelform(request):
    if request.method == 'POST':
        form = AddTweetModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('tweetapp:listtweet'))
        else:
            print("Error in form!")
            return render(request, 'tweetapp/addtweetbymodelform.html', context={'form': form})
    else:
        form = AddTweetModelForm()
        return render(request, 'tweetapp/addtweetbymodelform.html', context={'form': form})
    
@login_required(login_url='/login')
def deletetweet(request, tweet_id):
    tweet = models.Tweet.objects.get(pk=tweet_id)
    if request.method == 'POST':
        tweet.delete()
        return redirect(reverse('tweetapp:listtweet'))


class SignUpView(CreateView):
    template_name = 'registration/signup.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')

