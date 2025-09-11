from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
import time, random
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
    
    # must include the full path to the templates and include
    # any subdirectories
    template_name = 'hw/home.html'
    context ={
        "time": time.ctime(),   
        "letter1": chr(random.randint(65, 90)),
        "letter2": chr(random.randint(65, 90)),
        "number" : random.randint(1, 10),
    }
    return render(request, template_name, context)

def about(request):
    ''' function to respond to the about request'''
    
    # must include the full path to the templates and include
    # any subdirectories
    template_name = 'hw/about.html'
    context ={
        "time": time.ctime(),   
        "letter1": chr(random.randint(65, 90)),
        "letter2": chr(random.randint(65, 90)),
        "number" : random.randint(1, 10),
    }
    return render(request, template_name, context)