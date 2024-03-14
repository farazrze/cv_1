from django.shortcuts import render
from .models import Intro

def index(request):
    intro = Intro.objects.all()
    context = {'intro':intro}
    return render(request,'index.html',context)

