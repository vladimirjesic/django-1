from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, "index.html", status=200)

def about(requst):
    return HttpResponse("This is my about page!", status=500)

def product(request, name):
    return HttpResponse(f"This is {name}")

def user(request, userId):
    return HttpResponse(f"This is a user with ID {userId}")