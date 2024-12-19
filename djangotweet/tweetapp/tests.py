from django.test import TestCase
from django.contrib.auth.models import User
from tweetapp.models import Tweet

class TweetTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        Tweet.objects.create(username=self.user, message='Test tweet')

    def test_tweet_creation(self):
        tweet = Tweet.objects.get(message='Test tweet')
        self.assertEqual(tweet.username.username, 'testuser')
        self.assertEqual(tweet.message, 'Test tweet')
