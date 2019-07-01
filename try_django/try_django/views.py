from django.http import HttpResponse

from django.shortcuts import render

def home_page(request):
    my_title = "Hello There..."
    return render(request, "hello_world.html", {"title": my_title})
    #return HttpResponse("<h1> Hello World! </h1>")

def about_page(request):
    return render(request, "about.html", {"title": "About us..."})
    #return HttpResponse("<h1> About </h1>")

def contact_page(request):
    return render(request, "contact.html", {"title": "Contact us.."})
    #return HttpResponse("<h1> Contact Us </h1>")