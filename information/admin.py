from django.contrib import admin
from .models import Intro

class Introcom(admin.ModelAdmin):
    search_fields=['name','age','phone']

admin.site.register(Intro,Introcom)