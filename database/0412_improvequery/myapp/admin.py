from django.contrib import admin
from .models import PetSitter, Pet

admin.site.register(Pet)
admin.site.register(PetSitter)