from django import forms
from django.forms import ModelForm
from .models import Tweet, UserProfile


class TwitterForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['content']


class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['avatar']

