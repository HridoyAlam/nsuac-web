from django.shortcuts import render
from .models import Slider,Upcoming_event
import json
import requests
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

# Create your views here.
def home(request):
    slider = Slider.objects.all()[0]
    up_event = Upcoming_event.objects.all()[0]
    context = {'slider': slider,
                'up_event':up_event
                }
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

### outdoor events

def nfl(request):
    return render(request, 'nfl.html', {})

def ncl(request):
    return render(request, 'ncl.html', {})

def batch_cricket(request):
    return render(request, 'batch_cricket.html', {})

def batch_football(request):
    return render(request, 'batch_football.html', {})

def tryouts(request):
    return render(request, 'tryouts.html', {})

### indoor events

def chess_carrom(request):
    return render(request, 'chess_carrom.html', {})

def shuttle_master(request):
    return render(request, 'shuttle_master.html', {})

def basketball(request):
    return render(request, 'basketball.html', {})

def table_tennis(request):
    return render(request, 'table_tennis.html', {})

def fff(request):
    return render(request, 'fff.html', {})
