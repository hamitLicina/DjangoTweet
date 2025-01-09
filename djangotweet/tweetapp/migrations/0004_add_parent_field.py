from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    dependencies = [
        ('tweetapp', '0003_profile_alter_tweet_options_tweet_likes_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='parent',
            field=models.ForeignKey('self', null=True, blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies'),
        ),
    ] 