
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Profile
import random
# Create your views here.

class ProfileListView(ListView):
    '''define a view to show all profiles'''

    model= Profile
    template_name = 'mini_insta/show_all_profiles.html'
    context_object_name = 'profiles' # should be plural

class ProfileDetailView(DetailView):
    '''display a single profile'''
    model = Profile
    template_name = 'mini_insta/show_profile.html'
    context_object_name = 'profile' # should be singular