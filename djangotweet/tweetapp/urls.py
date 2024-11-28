from django.urls import path
from . import views

app_name = 'tweetapp'

urlpatterns = [
    path('listtweet/', views.listtweet, name='listtweet'),
    path('addtweet/', views.addtweet, name='addtweet'),
]
