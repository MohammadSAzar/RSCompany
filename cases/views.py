from django.shortcuts import render
from django.views.generic import ListView

def homepage_shower(request):
    return render(request, 'home.html')


