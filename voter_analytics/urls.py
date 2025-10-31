# voter_analytics/urls.py
# Nicholas Zhang
# nzhan01@bu.edu
# created: 10/31/2025
# models file containing all the urls for the voter_analytics app
 
from django.urls import path
from . import views 
 
urlpatterns = [
    # map the URL (empty string) to the view
	path(r'', views.ResultsListView.as_view(), name='voters'),
    path(r'voters', views.ResultsListView.as_view(), name='voter_list'),
    path(r'voter/<int:pk>', views.ResultDetailView.as_view(), name='voter_detail'),
    path(r'graphs', views.GraphsView.as_view(), name='graphs'),
]