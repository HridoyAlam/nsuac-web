from django.shortcuts import redirect, render
from .models import Badminton, Basketball, Football, Gallery, Slider, TableTennis,Upcoming_event, Subscribers, Contacts
import json
import requests
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.core.mail import message, send_mail, BadHeaderError
from .forms import contact_form
from app.models import Contacts

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

def subscribers(request):
    if request.method == 'POST':
        subscriber_email = request.POST['subscriber_email']

        ins = Subscribers(subscriber_email = subscriber_email)
        ins.save()
    pass

def contact(request):
    if request.method == 'POST':
        message_name = request.POST['message_name']
        message_email = request.POST['message_email']
        phone = request.POST['phone']
        message = request.POST['message']

        ins = Contacts(message_name = message_name, message_email = message_email, phone = phone, message = message)
        ins.save()
        
        send_mail(
            'Thank you' + message_name,
            message,
            message_email, #from email
            ['athletics.club@northsouth.edu'] #to email address

        )
        return render(request, 'contact.html', {'message_name':message_name})

    else:
        return render(request,'contact.html',{})

def gallery(request):
    images = Gallery.objects.all()
    context = {'images':images}
    return render(request, 'gallery.html', context)


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
    badminton = Badminton.objects.all()
    context = {
        'badminton':badminton
    }
    return render(request, 'team_badminton.html', context)


def team_basketball(request):
    basketball = Basketball.objects.all()
    return render(request, 'team_basketball.html', {'basketball':basketball})


def team_football(request):
    football = Football.objects.all()
    return render(request, 'team_football.html', {'football':football})


def team_table_tennis(request):
    tt = TableTennis.objects.all()
    return render(request, 'team_table_tennis.html', {'tt':tt})


def messages_from(request):
    return render(request, 'messages_from.html',{})