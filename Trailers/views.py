from django.shortcuts import render
from django.http import HttpResponse
from .models import Trailers, Category

def index (request):
    categories = Category.objects.all()
    data = {'categories' : categories}
    return render(request, 'index.html', data)

def category (request, id):
    category_user = Category.objects.get(pk=id)
    category_trailer = Trailers.objects.filter(category = category_user)
    categories = Category.objects.all()
    data = {'category_user' : category_user,
            'category_trailer' : category_trailer,
            'categories' : categories
    }

    return render(request, 'category_trailer.html', data)
   
def trailer (request, id):
    trailer_user = Trailers.objects.get(pk=id)
    categories = Category.objects.all()
    data = {'trailer_user' : trailer_user, 'categories' : categories }
    return render(request, 'trailer.html', data)

    return HttpResponse(full)

# one = Trailers.objects.all(pk=2) pk-primary key
# return HttpResponse(one)

# filter ------ cat = Trailers.objects.filter(category=2)
# return HttpResponse(cat)