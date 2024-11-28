from django.shortcuts import render

# Create your views here.

def listtweet(request):
    return render(request, 'tweets/listtweet.html')

def addtweet(request):
    return render(request, 'tweets/addtweet.html')
