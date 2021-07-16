from django.shortcuts import render
#from .models import service
# Create your views here.
def home(request):
    return render(request, 'home.html', {})

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