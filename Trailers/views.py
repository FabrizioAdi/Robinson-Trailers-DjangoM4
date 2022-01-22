from django.shortcuts import render
from django.http import HttpResponse
from .models import Trailers, Category

def index (request):
    question = Trailers.objects.all()
    return HttpResponse(question)

def category (request, id):
    category_user = Category.objects.get(pk=id)
    return HttpResponse(category_user)

def trailer (request, id):
    trailer_user = Trailers.objects.get(pk=id)
    full = "<h1>" + str(trailer_user) + "</h1>" + \
           "<p>" + str(trailer_user.excerpt) + "</p>" + \
           "<p>" + str(trailer_user.price) + "</p>"

    return HttpResponse(full)

# one = Trailers.objects.all(pk=2) pk-primary key
# return HttpResponse(one)

# filter ------ cat = Trailers.objects.filter(category=2)
# return HttpResponse(cat)