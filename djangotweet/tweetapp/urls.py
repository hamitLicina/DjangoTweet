from django.urls import path
from . import views

app_name = 'tweetapp'

urlpatterns = [
    path('', views.listtweet, name='home'),
    path('listtweet/', views.listtweet, name='listtweet'),
    path('addtweet/', views.addtweet, name='addtweet'),
    path('profile/', views.profile, name='profile'),
    path('addtweetbyform', views.addtweetbyform, name='addtweetbyform'),
    path('addtweetbymodelform', views.addtweetbymodelform, name='addtweetbymodelform'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('deletetweet/<int:tweet_id>', views.deletetweet, name='deletetweet'),
    path('profile/<str:username>/', views.profile_view, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('follow/<str:username>/', views.follow_unfollow, name='follow_unfollow'),
    path('search/', views.search_tweets, name='search'),
    path('like/<int:tweet_id>/', views.like_tweet, name='like_tweet'),
    path('reply/<int:tweet_id>/', views.reply_tweet, name='reply_tweet'),
]
