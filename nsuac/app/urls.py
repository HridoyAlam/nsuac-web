from django.contrib import admin
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
    path('faculty_advisor', views.faculty_advisor, name= "faculty_advisor"),
    path('club_life', views.club_life, name='club_life'),
    path('update', views.update, name='update'),
    path('nfl', views.nfl, name='nfl'),

    path('ncl', views.ncl, name='ncl'),
    path('batch_cricket', views.batch_cricket, name='batch_cricket'),
    path('batch_football', views.batch_football, name='batch_football'),
    path('tryouts', views.tryouts, name='tryouts'),

    path('chess_carrom', views.chess_carrom, name='chess_carrom'),
    path('shuttle_master', views.shuttle_master, name='shuttle_master'),
    path('basketball', views.basketball, name='basketball'),
    path('table_tennis', views.table_tennis, name='table_tennis'),
    path('fff', views.fff, name='fff')
]