from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse_lazy
from django.views.generic import TemplateView, UpdateView
from .models import Tweet, UserProfile
from twitter.forms import TwitterForm, UpdateUserForm
from django.http import HttpResponse
from django.views.generic import CreateView, UpdateView


class MainPage(View):

    def get(self, request):
        form= TwitterForm()
        ctx= {"form": form,
              "tweets": Tweet.objects.all()}
        return render(request, "main.html", ctx)

    def post(self, request):
        form = TwitterForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data['content']
            user = self.request.user
            new_tweet = Tweet.objects.create(content=content, author=user)
            new_tweet.save()
            return reverse_lazy('main')
        else:
            return HttpResponse("Nie dodano tweeta!")


class UpdateUserProfile(UpdateView): #fixme
    def get(self, request):
        form = UpdateUserForm()
        user = self.request.user
        ctx = {"form": form,
               "user": user}
        return render(request, "userprofile_form.html", ctx)

    def post(self, request):
        form = UpdateUserForm(request.POST, request.FILES)
        user = self.request.user
        if form.is_valid():
            avatar = request.FILES['avatar']
            userprofile = UserProfile.objects.filter(user=user)
            if userprofile is not None:
                UserProfile.objects.update(avatar=avatar, user=user)
            else:
                new_userprofile = UserProfile.objects.create(avatar=avatar, user=user)
                new_userprofile.save()
            return reverse_lazy('main')
        else:
            return HttpResponse("Nie udało się dodać avatara!")


class UserProfileView(View):
    def get(self, request):
        user = self.request.user
        ctx = {"user": user}
        return render(request, "userprofile.html", ctx)