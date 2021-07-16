from django.urls import path,include
from .import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about.html', views.about, name="about"),
    path('contact.html', views.contact, name="contact"),
    path('eb.html', views.eb, name="eb"),
    path('subeb.html', views.subeb, name="subeb"),
    path('hallOfFame.html', views.hallOfFame, name="hallOfFame"),
    path('all_events', views.all_events, name="all_events"),
    path('faculty_advisor', views.faculty_advisor, name= "faculty_advisor")
]