from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, HttpRequest
import time, random
# Create your views here.

quotes=[
        "I'm just a little kid from Akron.",
        "Volleyball, I could be pretty good. After a few practices I could be that striker, or whatever they call it.",
        "I don't read books much.",
        ]
images=[
    "https://render.fineartamerica.com/images/rendered/search/print/10.5/14/break/images/artworkimages/medium/2/the-chosen-one-st-vincent-st-mary-high-lebron-james-february-18-2002-sports-illustrated-cover.jpg",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRxLZ3CaWcQmlhcPRbtBg0OXymHerFn1MY2BQ&s",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQzn6Ke7Ku7OxgJAWC99OvGViXFCmAQlM2Frg&s",
]




def quote_page(request):
    ''' function to respond to the home request'''
    
    # must include the full path to the templates and include
    # any subdirectories
    template_name = 'quotes/quote.html'
    context ={
         "time": time.ctime(),   
        "quote" : random.choice(quotes),
        "image": random.choice(images),
    }
    return render(request, template_name, context)


def about(request):
    ''' function to respond to the about request'''
    
    # must include the full path to the templates and include
    # any subdirectories
    template_name = 'quotes/about.html'
    context ={
        "time": time.ctime(),   
        "lebron_champ" : "https://legacymedia.sportsplatform.io/img/images/photos/003/783/263/hi-res-1e10b5824491fd50203d18e12f74ba02_crop_north.jpg?1546259509&w=630&h=420",
    }
    return render(request, template_name, context)

def show_all(request):
    ''' function to respond to the show_all request'''
    
    template_name = 'quotes/show_all.html'
    context ={
        "time": time.ctime(),   
        "quotes": quotes,
        "images": images,
    }
    return render(request, template_name, context)