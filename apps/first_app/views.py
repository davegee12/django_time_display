from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime

def index(request):
    context = {
        "time": strftime("%y-%m-%d %H:%M %p", gmtime())
    }
    return render(request, "first_app/index.html", context)

def time(request):
    context = {
        "time": strftime("%y-%m-%d %H:%M %p", gmtime())
    }
    return render(request, "first_app/index.html", context)