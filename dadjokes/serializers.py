#dadjokes/serializers.py
# convert django data models to a text-representation such as JSON or XML that can be sent over http
from rest_framework import serializers
from .models import *
from django.urls import reverse
import random
from rest_framework.response import Response

class JokeSerializer(serializers.ModelSerializer):
    '''serializer for Joke model
        specifiy which model/fields to send in the API'''
    class Meta:
        model = Joke
        fields = [ 'id','text', 'name', 'timestamp']

    #add methods to customize the CRUD operations if needed
    def get_success_url(self):
        return reverse('show_joke', kwargs={'pk': self.object.pk})

    def create(self, validated_data):
        '''ovverride the suprclas method that handles object creation. 
            create and return a new Joke object'''
        #create a new Joke object using the validated data

        #joke = Joke(**validated_data)
        #add/attach any other data/relationships here if needed
        #save the data to the database
        #joke.save()

        #simpler way to create the object and autosave to the database
        joke = Joke.objects.create(**validated_data)

        
        #return the new joke object instance
        return joke

class PictureSerializer(serializers.ModelSerializer):
    '''serializer for Picture model
        specifiy which model/fields to send in the API'''
    class Meta:
        model = Picture
        fields = [ 'id','image_url', 'name', 'timestamp']
    def get_success_url(self):
        return reverse('show_picture', kwargs={'pk': self.object.pk})

    def create(self, validated_data):
        '''ovverride the suprclas method that handles object creation. 
            create and return a new Picture object'''
        #create a new Picture object using the validated data
        picture = Picture.objects.create(**validated_data)

        
        #return the new picture object instance
        return picture

##########################################################################################
#REST API 
from rest_framework import generics
from .serializers import *

class JokeListAPIView(generics.ListCreateAPIView):
    '''API view to retrieve list of jokes or create a new joke'''
    queryset = Joke.objects.all().order_by('-timestamp')
    serializer_class = JokeSerializer

class PictureListAPIView(generics.ListCreateAPIView):
    '''API view to retrieve list of pictures or create a new picture'''
    queryset = Picture.objects.all().order_by('-timestamp')
    serializer_class = PictureSerializer

class JokeDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    '''API view to retrieve, update, or delete a joke by primary key'''
    queryset =Joke.objects.all()
    serializer_class = JokeSerializer

class PictureDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    '''API view to retrieve, update, or delete a picture by primary key'''
    queryset =Picture.objects.all()
    serializer_class = PictureSerializer

class RandomJokeAPIView(generics.RetrieveAPIView):
    '''API view to retrieve a random  joke'''
    

    def get(self, request, *args, **kwargs):
        joke = random.choice(Joke.objects.all())
        joke_data = JokeSerializer(joke).data
        return Response(joke_data)
    
class RandomPictureAPIView(generics.RetrieveAPIView):
    '''API view to retrieve a random picture'''

    def get(self, request, *args, **kwargs):
        picture = random.choice(Picture.objects.all())
        picture_data = PictureSerializer(picture).data
        
        return Response(picture_data)