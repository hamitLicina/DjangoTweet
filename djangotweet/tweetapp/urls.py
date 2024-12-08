from django.urls import path
from . import views

app_name = 'tweetapp'

urlpatterns = [
    path('listtweet/', views.listtweet, name='listtweet'),
    path('addtweet/', views.addtweet, name='addtweet'),
    path('profile/', views.profile, name='profile'),
    path('addtweetbyform', views.addtweetbyform, name='addtweetbyform'),
    path('addtweetbymodelform', views.addtweetbymodelform, name='addtweetbymodelform'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('deletetweet/<int:tweet_id>', views.deletetweet, name='deletetweet'),
]
