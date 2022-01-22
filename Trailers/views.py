from django.shortcuts import render
from django.http import HttpResponse
from .models import Trailers

def index(request):
    question = Trailers.objects.all()
    return HttpResponse(question)

# one = Trailers.objects.all(pk=2) pk-primary key
# return HttpResponse(one)

# filter ------ cat = Trailers.objects.filter(category=2)
# return HttpResponse(cat)