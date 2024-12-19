from django import forms
from .models import Tweet

class AddTweetModelForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['message']  # Ensure this matches the fields in the Tweet model
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