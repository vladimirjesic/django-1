from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

products = {
    "Macbook Air 2025": {
        "price": 2000,
        "description": "This is Macbook Air 2025"
    },
    "iPhone 17 Pro": {
        "price": 1499,
        "description": "Apple's latest flagship smartphone"
    },
    "Samsung Galaxy S26": {
        "price": 1399,
        "description": "Premium Android smartphone with advanced camera"
    },
    "Dell XPS 15": {
        "price": 1800,
        "description": "Powerful laptop for work and entertainment"
    },
    "Sony WH-1000XM6": {
        "price": 450,
        "description": "Wireless noise-cancelling headphones"
    },
    "iPad Pro M5": {
        "price": 1200,
        "description": "High-performance tablet for professionals"
    }
}

def home(request):

    context = {
        "products": products
    }
    return render(request, "index.html", context)

def about(requst):
    return HttpResponse("This is my about page!", status=500)

def product(request, name):
    product = products.get(name)
    context = {
        "product_info": product
    }
    if product:
        return render(request, "product.html", context)
    else:
        return HttpResponseNotFound(f"Product {name} doesn't exist!")


def user(request, userId):
    return HttpResponse(f"This is a user with ID {userId}")