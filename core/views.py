from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, "index.html")

def about(requst):
    return HttpResponse("This is my about page!")
