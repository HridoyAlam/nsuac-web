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



def faq(request):
    return render(request, 'faq.html', {})


def contact(request):
    return render(request, 'contact.html', {})


def gallery(request):
    return render(request, 'gallery.html', {})


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

def event_nfl(request):
    return render(request, 'event_nfl.html', {})

def event_ncl(request):
    return render(request, 'event_ncl.html', {})

def event_batch_cricket(request):
    return render(request, 'event_batch_cricket.html', {})

def event_batch_football(request):
    return render(request, 'event_batch_football.html', {})

def event_tryouts(request):
    return render(request, 'event_tryouts.html', {})

### indoor events

def event_chess_carrom(request):
    return render(request, 'event_chess_carrom.html', {})

def event_shuttle_master(request):
    return render(request, 'event_shuttle_master.html', {})

def event_basketball(request):
    return render(request, 'event_basketball.html', {})

def event_table_tennis(request):
    return render(request, 'event_table_tennis.html', {})

def event_fff(request):
    return render(request, 'event_fff.html', {})


def activity_one(request):
    return render(request, 'activity_one.html', {})

def activity_two(request):
    return render(request, 'activity_two.html', {})

def activity_three(request):
    return render(request, 'activity_three.html', {})

def activity_four(request):
    return render(request, 'activity_four.html', {})


# teams 
def team_cricket(request):
    return render(request, 'team_cricket.html', {})


def team_badminton(request):
    return render(request, 'team_badminton.html', {})


def team_basketball(request):
    return render(request, 'team_basketball.html', {})


def team_football(request):
    return render(request, 'team_football.html', {})


def team_table_tennis(request):
    return render(request, 'team_table_tennis.html', {})
