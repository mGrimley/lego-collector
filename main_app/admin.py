from django.contrib import admin
from .models import Lego, Building, Builder 

# Register your models here.

admin.site.register(Lego)
admin.site.register(Building)
admin.site.register(Builder)