from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
import time
# Create your views here.


def home(request):
    ''' function to respond to the home request'''


    response_text = f''' 
    <html>
    <h1> Hello World! </h1>
    <p> The current time is {time.ctime()}. </p>
    </html>
    '''

    return HttpResponse(response_text)


def home_page(request):
    ''' function to respond to the home request'''
    
    template_name = 'hw/home.html'
    return render(request, template_name)