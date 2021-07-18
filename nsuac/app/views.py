from django.shortcuts import render
from .models import Slider
import json
import requests
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

# Create your views here.
def home(request):
    slider = Slider.objects.all()[0]
    context = {'slider': slider}
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html', {})

def contact(request):
    return render(request, 'contact.html', {})

def eb(request):
    return render(request, 'eb.html', {})

def subeb(request):
    return render(request, 'subeb.html', {})

def hallOfFame(request):
    return render(request, 'hallOfFame.html', {})

def all_events(request):
    return render(request, 'all_events.html', {})

def faculty_advisor(request):
    return render(request, 'faculty_advisor.html', {})

def club_life(request):
    return render(request, 'club_life.html', {})

def update(request):
    return render(request, 'update.html', {})