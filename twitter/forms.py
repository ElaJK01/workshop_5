from django import forms
from django.forms import ModelForm
from .models import Tweet


class TwitterForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['content']

