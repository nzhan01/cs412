# file: mini_insta/views.py
# Nicholas Zhang
# nzhan01@bu.edu
# created: 9/25/2025
# models file containing all the views for the mini_insta app


from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Profile, Post

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

class PostDetailView(DetailView):
    '''display a single post'''
    model = Post
    template_name = 'mini_insta/show_post.html'
    context_object_name = 'post' # should be singular