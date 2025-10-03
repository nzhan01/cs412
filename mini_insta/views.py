# file: mini_insta/views.py
# Nicholas Zhang
# nzhan01@bu.edu
# created: 9/25/2025
# models file containing all the views for the mini_insta app


from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Profile, Post, Photo
from .forms import CreatePostForm
from django.urls import reverse

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


class CreatePostView(CreateView):
    '''a view to create a new post'''
    model = Post
    form_class = CreatePostForm
    template_name = 'mini_insta/create_post_form.html'

    
    
    def get_context_data(self):
        '''Return the dictionary of context variables for use in the template.'''
 
 
        # calling the superclass method
        context = super().get_context_data()
 
 
        # find/add the article to the context data
        # retrieve the PK from the URL pattern
        pk = self.kwargs['pk']
        profile = Profile.objects.get(pk=pk)
 
 
        # add this article into the context dictionary:
        context['profile'] = profile
        context['is_create_post'] = True
        return context

    def form_valid(self, form):
        '''This method handles the form submission and saves the 
        new object to the Django database.
        We need to add the foreign key (of the Profile) to the post
        object before saving it to the database.
        '''
        
        # retrieve the PK from the URL pattern
        pk = self.kwargs['pk']
        profile = Profile.objects.get(pk=pk)
        form.instance.profile = profile # set the FK

        response = super().form_valid(form)# call the superclass method to save the Post


        image_url = self.request.POST.get("image_url")
        if image_url:  # only save if provided
            Photo.objects.create(
                post=self.object,     # self.object = the saved Post
                image_url=image_url,
                
            )
 
        return response
    

    