from django import forms
from django.forms import ModelForm
from tweetapp.models import Tweet

class AddTweetForm(forms.Form):
    nickname_input = forms.CharField(label='Nickname', max_length=50)
    message_input = forms.CharField(label='Tweet', max_length=140, widget=forms.Textarea(attrs={'rows': 4, 'cols': 50}))

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