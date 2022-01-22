from django.shortcuts import render
from django.http import HttpResponse
from .models import Trailers, Category

def index(request):
    question = Category.objects.all()
    return HttpResponse(question)

def category(request, id):
    category_user = Category.objects.get(pk=id)
    return HttpResponse(category_user.name)

# one = Trailers.objects.all(pk=2) pk-primary key
# return HttpResponse(one)

# filter ------ cat = Trailers.objects.filter(category=2)
# return HttpResponse(cat)