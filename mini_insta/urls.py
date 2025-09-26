
# file: mini_insta/urls.py
# Nicholas Zhang
# nzhan01@bu.edu
# created: 9/25/2025
# models file containing all the urls for the mini_insta app

from django.urls import path

from .views import ProfileListView, ProfileDetailView
urlpatterns =[
    path('', ProfileListView.as_view(), name='show_all_profiles'),
    path('profile/<int:pk>', ProfileDetailView.as_view(), name='show_profile'),
]
