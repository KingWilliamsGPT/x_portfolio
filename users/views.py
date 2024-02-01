from django.shortcuts import render, get_object_or_404
from django.views import generic

from . import models


def index(request):
     return render(request, 'index.html')



class UserProfileView(generic.DetailView):
     model = models.UserProfile
     template_name = 'users/user_profile.html'
     context_object_name = 'profile'


class CustomJs(generic.DetailView):
     model = models.UserProfile
     context_object_name = 'profile'
     template_name='users/custom.js'
     content_type='text/javascript; charset="utf-8"'
