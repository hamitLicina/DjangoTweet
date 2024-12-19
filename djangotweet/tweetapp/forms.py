from django import forms
from django.forms import ModelForm
from tweetapp.models import Tweet

class AddTweetModelForm(ModelForm):
    class Meta:
        model = Tweet
        fields = ['username', 'message']
        labels = {
            'username': 'Nickname',
            'message': 'Tweet'
        }
        widgets = {
            'message': forms.Textarea(attrs={'rows': 4, 'cols': 50})
        }
        help_texts = {
            'message': 'Max 140 characters'
        }