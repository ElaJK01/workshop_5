from django.shortcuts import render
from django.views import View
from django.urls import reverse_lazy
from django.views.generic import TemplateView, UpdateView
from .models import Tweet, UserProfile
from twitter.forms import TwitterForm
from django.http import HttpResponse


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
            return reverse_lazy('main.html')
        else:
            return HttpResponse("Nie dodano tweeta!")


class UpdateUserProfile(UpdateView):
    model = UserProfile
    fields = '__all__'
    success_url = reverse_lazy('main')