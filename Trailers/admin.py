from django.contrib import admin
from .models import Trailers, Sector, Category

# Register your models here.
admin.site.register(Trailers)
admin.site.register(Sector)
admin.site.register(Category)
