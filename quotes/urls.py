# file: quotes/urls.py

from django.urls import path
from django.conf import settings
from . import views

# URL patterns specific to the hw app:
urlpatterns = [
    #path(r'', views.home, name ="home"),
    path(r'', views.quote_page, name ="home_page"),
    path(r'about', views.about, name ="about_page"),
    path(r'quote', views.quote_page, name ="quote_page"),
    path(r'show_all', views.show_all, name ="show_all_page"),
    

]