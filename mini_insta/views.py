# file: mini_insta/views.py
# Nicholas Zhang
# nzhan01@bu.edu
# created: 9/25/2025
# models file containing all the views for the mini_insta app


from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Profile, Post, Photo
from .forms import CreatePostForm, UpdateProfileForm
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin ## NEW
from django.contrib.auth.forms import UserCreationForm ## NEW
from django.contrib.auth.models import User ## NEW
from django.contrib.auth import login # NEW

# Create your views here.
class MiniInstaLoginRequiredMixin(LoginRequiredMixin):
    """Custom mixin that redirects to the mini_insta login page."""

    def get_login_url(self):
        """Return the URL for the app's custom login view."""
        return reverse('login')
    def get_profile(self):
        """Return the Profile object for the currently logged-in user."""
        return Profile.objects.get(user=self.request.user)

class LogoutConfirmationView(TemplateView):
    template_name = 'mini_insta/logged_out.html'


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

    
class MyProfileDetailView(MiniInstaLoginRequiredMixin, DetailView):
    '''display a single profile'''
    model = Profile
    template_name = 'mini_insta/show_profile.html'
    context_object_name = 'profile' # should be singular

    def get_object(self):
        """Return the Profile for the currently logged-in user."""
        return Profile.objects.get(user=self.request.user)
    
    def get_context_data(self, **kwargs):
        """Add profile to context (optional but useful for template)."""
        context = super().get_context_data(**kwargs)
        context['profile'] = self.get_object()
        return context

class PostDetailView(DetailView):
    '''display a single post'''
    model = Post
    template_name = 'mini_insta/show_post.html'
    context_object_name = 'post' # should be singular


class CreatePostView(MiniInstaLoginRequiredMixin, CreateView):
    '''a view to create a new post'''
    model = Post
    form_class = CreatePostForm
    template_name = 'mini_insta/create_post_form.html'

    
    
    def get_context_data(self):
        '''Return the dictionary of context variables for use in the template.'''
 
 
        # calling the superclass method
        context = super().get_context_data()
 
 
        # retrieve the PK from the URL pattern
        #pk = self.kwargs['pk']
        #profile = Profile.objects.get(pk=pk)
        profile = Profile.objects.get(user=self.request.user)
 
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
        #pk = self.kwargs['pk']
        #profile = Profile.objects.get(pk=pk)
        profile = Profile.objects.get(user=self.request.user)

        form.instance.profile = profile # set the FK

        response = super().form_valid(form)# call the superclass method to save the Post

        files = self.request.FILES.getlist('image_file')

        for f in files:
            Photo.objects.create(
                post=self.object,
                image_file=f,
            )
 
        return response
    
    
 
 
    

class UpdateProfileView(MiniInstaLoginRequiredMixin, UpdateView):
    ''' view to update a profile'''

    model = Profile
    form_class = UpdateProfileForm
    template_name = 'mini_insta/update_profile_form.html'

    def get_object(self):
        """Return the Profile for the currently logged-in user."""
        return Profile.objects.get(user=self.request.user)
    
    def get_context_data(self, **kwargs):
        """Add profile to context (optional but useful for template)."""
        context = super().get_context_data(**kwargs)
        context['profile'] = self.get_object()
        return context
    

class DeletePostView(MiniInstaLoginRequiredMixin, DeleteView):
    '''view to delete a post'''
    model = Post
    template_name = 'mini_insta/delete_post_form.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
 
 
        # find/add the post to the context data
        # retrieve the PK from the URL pattern
        pk = self.kwargs['pk']
        post = Post.objects.get(pk=pk)
        profile = Post.objects.get(pk=pk).profile
        
        
 
 
        # add this post into the context dictionary:
        context['post'] = post
        context['profile'] = profile
        return context
    

    def get_success_url(self):
        '''after deleting the post, redirect to the profile page'''
        pk = self.object.profile.pk
        return reverse('show_profile', kwargs={'pk': pk})
    

class UpdatePostView(MiniInstaLoginRequiredMixin, UpdateView):
    ''' view to update a post'''

    model = Post
    form_class = CreatePostForm
    template_name = 'mini_insta/update_post_form.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
 
 
        # find/add the post to the context data
        # retrieve the PK from the URL pattern
        pk = self.kwargs['pk']
        post = Post.objects.get(pk=pk)
        profile = Post.objects.get(pk=pk).profile


 
 
        # add this post into the context dictionary:
        context['post'] = post
        context['profile'] = profile

        return context
    

    def get_success_url(self):
        '''after updating the post, redirect to the profile page'''
        pk = self.kwargs['pk']
        return reverse('show_post', kwargs={'pk': pk})
    

class ShowFollowersDetailView(DetailView):
    '''display the followers for a single profile'''
    model = Profile
    template_name = 'mini_insta/show_followers.html'
    context_object_name = 'profile' 

    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
 
 
        pk = self.kwargs['pk']
        profile = Profile.objects.get(pk=pk)
 
        context['profile'] = profile
        #context['followers'] = profile.get_followers()
        return context


class ShowFollowingDetailView(DetailView):
    '''display the following for a single profile'''
    model = Profile
    template_name = 'mini_insta/show_following.html'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
 
 
        pk = self.kwargs['pk']
        profile = Profile.objects.get(pk=pk)
 
        context['profile'] = profile
        return context
    
class PostFeedListView(MiniInstaLoginRequiredMixin, ListView):
    '''display all the posts from profiles this profile follows'''
    model = Profile
    template_name = 'mini_insta/show_feed.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #pk = self.kwargs['pk']
        #profile = Profile.objects.get(pk=pk)
        profile = Profile.objects.get(user=self.request.user)

        context['profile'] = profile
        context['posts'] = profile.get_post_feed()
        return context
    
class SearchView(MiniInstaLoginRequiredMixin, ListView):
    '''display search results for keywords'''
    model = Post
    template_name = 'mini_insta/search_results.html'

    def dispatch(self, request, *args, **kwargs):
        '''override dispatch to get the search query from the request'''
        #self.profile = Profile.objects.get(pk=kwargs['pk'])
        self.profile = Profile.objects.get(user=self.request.user)
        
        if 'query' in self.request.GET :
            self.query = self.request.GET['query']

        else:
            return render(request, 'mini_insta/search.html', {'profile': self.profile})
        
        return super().dispatch(request, *args, **kwargs)
    
    def get_queryset(self):
        '''override get_queryset to filter profiles based on the search query'''
        post_results =  Post.objects.filter(caption__contains=self.query) 
        return post_results


    def get_context_data(self, **kwargs):
        '''get the context data for the search results'''
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('query')
        posts = self.get_queryset()
        profiles = (Profile.objects.filter(display_name__icontains=query) | Profile.objects.filter(username__icontains=query)| Profile.objects.filter(bio_text__icontains=query)).distinct()

        context['query'] = query
        context['profiles'] = profiles
        context['posts'] = posts
        context['profile'] = self.profile
        return context
    

class ProfileAccessMixin(LoginRequiredMixin):
    """helper to get the logged-in user's Profile."""
    
    def get_profile(self):
        """Return the Profile object for the currently logged-in user."""
        return Profile.objects.get(user=self.request.user)
