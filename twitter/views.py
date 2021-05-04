from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.urls import reverse_lazy
from django.views.generic import TemplateView, UpdateView
from .models import Tweet, UserProfile
from twitter.forms import TwitterForm, UpdateUserForm
from django.http import HttpResponse
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.models import User


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
            return redirect('main')
        else:
            return HttpResponse("Nie dodano tweeta!")


class UpdateUserProfile(View): #fixme
    def get(self, request, pk):
        form = UpdateUserForm()
        user = get_object_or_404(User,pk=pk)
        ctx = {"form": form,
               "user": user}
        return render(request, "userprofile_form.html", ctx)

    def post(self, request, pk):
        form = UpdateUserForm(request.POST, request.FILES)
        user = get_object_or_404(User, pk=pk)
        if form.is_valid():
            avatar = request.FILES['avatar']
            userprofile = UserProfile.objects.filter(user=user)
            if userprofile is not None:
                UserProfile.objects.update(avatar=avatar, user=user)
            else:
                new_userprofile = UserProfile.objects.create(avatar=avatar, user=user)
                new_userprofile.save()
            return redirect('main')
        else:
            return HttpResponse("Nie udało się dodać avatara!")


class UserProfileView(View):
    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        ctx = {"user": user}
        return render(request, "userprofile.html", ctx)