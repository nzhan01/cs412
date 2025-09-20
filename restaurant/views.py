# file: restaurant/views.py
# Nicholas Zhang
# nzhan01@bu.edu
# created: 9/16/2025
# views file containing all the relevent context varaiables for the restaurant app
 

from django.shortcuts import render
from django.http import HttpResponse
import time, random

specials =[
    ("firecracker soup",5),
    ("fish on a stick", 6),
    ("diablo reaper chicken",8),
    ("dragon breath pasta",10),
]

menu_items = [
    ("spicy tuna roll",12),
    ("hot wings",7),
    ("jalapeno poppers",6),
    ("spicy beef stew",9),
    ("cajun fries",4),
]


# Create your views here.
def main(request):
    ''' function to respond to the main page request'''

    template_name = 'restaurant/main.html'
    context ={
        "time": time.ctime(), }
    return render(request, template_name, context)


def order(request):
    ''' function to respond to the order request'''
    template_name = 'restaurant/order.html'
    chosen_special = random.choice(specials)

    context= {
        "time": time.ctime(),   
        "special" : chosen_special[0],
        "special_price": chosen_special[1],
        }
    return render(request, template_name, context)


def confirmation(request):
    ''' function to respond to the confirmation request and display the ordered items'''
    template_name = 'restaurant/confirmation.html'

    if request.POST:
        print(request.POST)
        name = request.POST['name']
        instructions = request.POST['instructions']
        phone= request.POST['phone']
        email= request.POST['email']
        buffer= random.randint(30,60)*60
        order_time = time.time()+ buffer
        order=[]                            #list of ordered items
        total=0

        #iterate through menu items and specials to see what was ordered
        for item in menu_items:
            if item[0] in request.POST:
                ordered_item = item[0]
                if ordered_item == "cajun fries":
                    if "extra_spicy" in request.POST:
                        ordered_item += " (extra spicy)"
                    if "cheese" in request.POST:
                        ordered_item += " (with cheese)"
                    if "extra_crispy" in request.POST:
                        ordered_item += " (extra_crispy)"
                    
                total += item[1]
                order.append(ordered_item)

        #iterate through specials to see if it was ordered
        for item in specials:
            if item[0] in request.POST:
                total += item[1]
                order.append(item[0])


        


        context={
            'total': total,
            'order': order,
            'name': name,
            'instructions': instructions,
            'phone': phone,
            'email': email, 
            'ready_time' : time.ctime(order_time),
            "time": time.ctime(),
            

        
    }
    return render(request,template_name=template_name, context=context)