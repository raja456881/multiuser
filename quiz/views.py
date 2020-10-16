from django.shortcuts import render

from .models import *
# Create your views here.

def quiz(request):
    return render(request,'quiz.html')