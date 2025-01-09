from django.shortcuts import render, redirect, get_object_or_404
from . import models
from django.urls import reverse, reverse_lazy
from django import forms
from .forms import AddTweetModelForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.http import JsonResponse
from django.contrib.auth.models import User
from .models import Profile
from django.db.models import Q
from django.contrib.auth import login

# Create your views here.

def listtweet(request):
    all_tweets = models.Tweet.objects.select_related('username').order_by('-date')[:50]
    tweet_dict = {"tweets": all_tweets}
    return render(request, 'tweetapp/listtweet.html', context=tweet_dict)

@login_required(login_url='/accounts/login/')
def addtweet(request):
    if request.method == 'POST':
        message = request.POST.get("message")
        if message and message.strip():  # Boş mesajları kontrol et
            new_tweet = models.Tweet(username=request.user, message=message)
            new_tweet.save()
            return redirect(reverse('tweetapp:home'))  # Ana sayfaya yönlendir
        return redirect(reverse('tweetapp:home'))  # Hata durumunda da ana sayfaya yönlendir
    return redirect(reverse('tweetapp:home'))  # GET isteklerini ana sayfaya yönlendir

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
    
@login_required(login_url='/accounts/login/')
def deletetweet(request, tweet_id):
    tweet = get_object_or_404(models.Tweet, pk=tweet_id)
    if tweet.username == request.user:
        tweet.delete()
    return redirect(reverse('tweetapp:home'))


class SignUpView(CreateView):
    template_name = 'registration/signup.html'
    form_class = UserCreationForm
    
    def form_valid(self, form):
        response = super().form_valid(form)
        # Kullanıcı kaydolduktan sonra otomatik login
        login(self.request, self.object)
        return response

    def get_success_url(self):
        return reverse_lazy('tweetapp:home')

@login_required(login_url='/accounts/login/')
def profile_view(request, username):
    user = get_object_or_404(User, username=username)
    profile = get_object_or_404(Profile, user=user)
    tweets = models.Tweet.objects.filter(username=user).order_by('-date')
    
    is_following = False
    if request.user.is_authenticated:
        is_following = request.user.profile.following.filter(user=user).exists()
    
    context = {
        'profile_user': user,
        'profile': profile,
        'tweets': tweets,
        'is_following': is_following,
        'tweets_count': tweets.count(),
        'following_count': profile.get_following_count(),
        'followers_count': profile.get_followers_count(),
    }
    return render(request, 'tweetapp/profile.html', context)

@login_required(login_url='/accounts/login/')
def edit_profile(request):
    if request.method == 'POST':
        bio = request.POST.get('bio')
        profile_picture = request.FILES.get('profile_picture')
        
        profile = request.user.profile
        if bio:
            profile.bio = bio
        if profile_picture:
            profile.profile_picture = profile_picture
        profile.save()
        
        return redirect('tweetapp:profile', username=request.user.username)
    
    return render(request, 'tweetapp/edit_profile.html', {'profile': request.user.profile})

@login_required(login_url='/accounts/login/')
def follow_unfollow(request, username):
    if request.method == 'POST':
        user_to_follow = get_object_or_404(User, username=username)
        profile = request.user.profile
        
        if profile.following.filter(user=user_to_follow).exists():
            profile.following.remove(user_to_follow.profile)
            action = 'unfollow'
        else:
            profile.following.add(user_to_follow.profile)
            action = 'follow'
            
        return JsonResponse({
            'status': 'success',
            'action': action,
            'followers_count': user_to_follow.profile.get_followers_count()
        })

def search_tweets(request):
    query = request.GET.get('q', '')
    if query:
        tweets = models.Tweet.objects.select_related('username').filter(
            Q(message__icontains=query) |  # Tweet içeriğinde ara
            Q(username__username__icontains=query)  # Kullanıcı adında ara
        ).order_by('-date')
    else:
        tweets = []
    
    context = {
        'tweets': tweets,
        'query': query,
        'results_count': len(tweets) if query else 0
    }
    return render(request, 'tweetapp/search_results.html', context)

@login_required(login_url='/accounts/login/')
def like_tweet(request, tweet_id):
    if request.method == 'POST':
        tweet = get_object_or_404(models.Tweet, id=tweet_id)
        if tweet.likes.filter(id=request.user.id).exists():
            tweet.likes.remove(request.user)
            liked = False
        else:
            tweet.likes.add(request.user)
            liked = True
        
        return JsonResponse({
            'status': 'success',
            'liked': liked,
            'likes_count': tweet.get_likes_count()
        })
    return JsonResponse({'status': 'error'}, status=400)

@login_required(login_url='/accounts/login/')
def reply_tweet(request, tweet_id):
    if request.method == 'POST':
        parent_tweet = get_object_or_404(models.Tweet, id=tweet_id)
        message = request.POST.get('message')
        
        if message and message.strip():
            reply = models.Tweet.objects.create(
                username=request.user,
                message=message,
                parent=parent_tweet
            )
            
            return JsonResponse({
                'status': 'success',
                'username': reply.username.username,
                'message': reply.message,
                'date': reply.date.strftime('%b %d, %Y, %I:%M %p'),
                'replies_count': parent_tweet.get_replies_count()
            })
    return JsonResponse({'status': 'error'}, status=400)

