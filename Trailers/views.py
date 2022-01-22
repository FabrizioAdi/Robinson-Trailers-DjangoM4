from django.shortcuts import render
from django.http import HttpResponse
from .models import Trailers

def index(request):
    question = Trailers.objects.all()
    return HttpResponse(question)