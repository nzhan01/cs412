from django.shortcuts import render
from .models import Joke, Picture
from django.views.generic import DetailView, ListView, TemplateView
import random
# Create your views here.

class RandomDetailView(TemplateView):
    '''view for displaying a random dad joke'''
    model = Joke
    template_name = 'dadjokes/random.html'
    context_object_name = 'joke'

    '''
     def get_object(self, queryset=None):
        override get_object to return a random joke
        
        jokes = Joke.objects.all()
        return random.choice(jokes)
    '''
   
    def get_context_data(self):
        '''get a random joke and a random picture and add to context'''
        context = super().get_context_data()
        jokes = Joke.objects.all()
        pictures = Picture.objects.all()
        context['joke'] = random.choice(jokes)
        context['picture'] = random.choice(pictures)
        print(context)
        return context
       



class JokeListView(ListView):
    '''view for showing all jokes'''
    model = Joke
    template_name = 'dadjokes/all_jokes.html'
    context_object_name = 'jokes'

    def get_queryset(self):
        '''override get_queryset to return all jokes ordered by timestamp'''
        #return Joke.objects.all().order_by('-timestamp')
        results = super().get_queryset().order_by('-timestamp')
        return results
    
class PictureListView(ListView):
    '''view for showing all pictures'''
    model = Picture
    template_name = 'dadjokes/all_pictures.html'
    context_object_name = 'pictures'
    def get_queryset(self):
        '''override get_queryset to return all pictures ordered by timestamp'''
        results = super().get_queryset().order_by('-timestamp')
        return results
    
class PictureDetailView(DetailView):
    '''view for displaying a picture detail using the primary key'''
    model = Picture
    template_name = 'dadjokes/show_picture.html'
    context_object_name = 'picture'

    def get_object(self, queryset=None):
        '''override get_object to return a picture by primary key'''
        pk = self.kwargs.get('pk')
        picture = Picture.objects.get(pk=pk)
        return picture
    

class JokeDetailView(DetailView):
    '''view for displaying a joke detail using the primary key'''
    model = Joke
    template_name = 'dadjokes/show_joke.html'
    context_object_name = 'joke'

    def get_object(self, queryset=None):
        '''override get_object to return a joke by primary key'''
        pk = self.kwargs.get('pk')
        joke = Joke.objects.get(pk=pk)
        return joke
    
