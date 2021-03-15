from django.db import models
from django.contrib.auth.models import User

MAX_TWEET_LENGTH = 280


class Tweet(models.Model):
    content = models.CharField(max_length=MAX_TWEET_LENGTH, verbose_name="Tweet")
    creation_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.author} on {self.creation_date} tweeted {self.content[:10]}"


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField()

