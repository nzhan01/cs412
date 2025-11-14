# dadjokes/urls.py
# Nicholas Zhang
# nzhan01@bu.edu
# created: 11/10/2025
# models file containing all the urls for the dadjokes app
 
from django.urls import path
from .serializers import * 
from .views import *
 
urlpatterns = [
    # map the URL (empty string) to the view

    path('', RandomDetailView.as_view(), name='home'),
    path('random', RandomDetailView.as_view(), name='random'),
    path('jokes', JokeListView.as_view(), name='joke_list'),
    path('joke/<int:pk>', JokeDetailView.as_view(), name='joke_detail'),
    path('pictures', PictureListView.as_view(), name='picture_list'),
    path('picture/<int:pk>', PictureDetailView.as_view(), name='picture_detail'),
    #API Views
    path('api/jokes/', JokeListAPIView.as_view(), name='joke_list_api'),
    path('api/pictures/', PictureListAPIView.as_view(), name='picture_list_api'),
    path('api/joke/<int:pk>/', JokeDetailAPIView.as_view(), name='joke_detail_api'),
    path('api/picture/<int:pk>/', PictureDetailAPIView.as_view(), name='picture_detail_api'),
    path('api/random/', RandomJokeAPIView.as_view(), name='random_joke_api'),
    path('api/random_picture/', RandomPictureAPIView.as_view(), name='random_picture_api'),
    path('api/', RandomJokeAPIView.as_view(), name='random_joke_api'),



]