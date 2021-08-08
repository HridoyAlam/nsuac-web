from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about.html', views.about, name="about"),
    path('contact.html', views.contact, name="contact"),
    path('faq.html', views.faq, name="faq"),
    path('gallery.html', views.gallery, name="gallery"),

    path('eb.html', views.eb, name="eb"),
    path('subeb.html', views.subeb, name="subeb"),
    path('hallOfFame.html', views.hallOfFame, name="hallOfFame"),
    path('faculty_advisor', views.faculty_advisor, name= "faculty_advisor"),

    path('all_events', views.all_events, name="all_events"),
    path('club_life', views.club_life, name='club_life'),
    path('update', views.update, name='update'),
    
    path('event_nfl', views.event_nfl, name='event_nfl'),
    path('event_ncl', views.event_ncl, name='event_ncl'),
    path('event_batch_cricket', views.event_batch_cricket, name='event_batch_cricket'),
    path('event_batch_football', views.event_batch_football, name='event_batch_football'),
    path('event_tryouts', views.event_tryouts, name='event_tryouts'),

    path('event_chess_carrom', views.event_chess_carrom, name='event_chess_carrom'),
    path('event_shuttle_master', views.event_shuttle_master, name='event_shuttle_master'),
    path('event_basketball', views.event_basketball, name='event_basketball'),
    path('event_table_tennis', views.event_table_tennis, name='event_table_tennis'),
    path('event_fff', views.event_fff, name='event_fff')
]