# file: quotes/urls.py
# Nicholas Zhang
# nzhan01@bu.edu
# created: 9/9/2025
# urls file containing all the path names for the quotes app

from django.urls import path
from django.conf import settings
from . import views



#URL patterns specific to the restaurant app:
urlpatterns =[
    path(r'', views.main, name='main'),
    path(r'order', views.order, name='order'),
    path(r'confirmation', views.confirmation, name='confirmation'),
]