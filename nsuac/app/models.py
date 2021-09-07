
from django.db import models
from django.contrib import admin
from django.db.models.base import Model
from django.db.models.fields import AutoField
# Create your models here.
class Slider(models.Model):
    slider_id = models.AutoField
    slide_image = models.ImageField(upload_to ='app/images', default = "")
    slide_title = models.CharField(max_length=30)
    slide_details=models.CharField(max_length=60)

    def __str__(self):
        return self.slide_title

class Upcoming_event(models.Model):
    up_event_id = models.AutoField
    up_event_date = models.DateField()
    up_event_title = models.CharField(max_length=30)
    up_event_details = models.CharField(max_length=50)
    up_event_image = models.ImageField(upload_to = 'app/images',default = "")

    def __str__(self) -> str:
        return self.up_event_title


## news later subscription
class Subscribers(models.Model):
    
    subscriber_email = models.EmailField(unique=True)

    def __str__(self):
        return self.subscriber_email

class Contacts(models.Model):
    message_name = models.CharField(max_length=30)
    message_email = models.EmailField()
    phone =  models.CharField(max_length=11)
    message = models.CharField(max_length=150)

    def __str__(self):
        return self.message_name


class Gallery(models.Model):
    class Meta:
        verbose_name_plural = "Gallery"
        
    gallery_image_id = models.AutoField
    gallery_image = models.ImageField()

class Badminton(models.Model):
    bad_id = models.AutoField
    bad_name = models.CharField(max_length=30)
    bad_batch = models.IntegerField()
    bad_major = models.CharField(max_length=4)
    bad_image = models.ImageField()

    def __str__(self):
        return self.bad_name

class Cricket(models.Model):
    cri_id = models.AutoField
    cri_name = models.CharField(max_length=30)
    cri_batch = models.IntegerField()
    cri_major = models.CharField(max_length=4)
    cri_image = models.ImageField()

    def __str__(self):
        return self.cri_name


class Basketball(models.Model):
    bas_id = models.AutoField
    bas_name =  models.CharField(max_length=30)
    bas_batch = models.IntegerField()
    bas_major = models.CharField(max_length=4)
    bas_image = models.ImageField()

    def __str__(self):
        return self.bas_name

class Football(models.Model):
    foot_id = models.AutoField
    foot_name = models.CharField(max_length=30)
    foot_batch = models.IntegerField()
    foot_major = models.CharField(max_length=4)
    foot_image = models.ImageField()

    def __str__(self):
        return self.foot_name

class TableTennis(models.Model):
    tt_id = models.AutoField
    tt_name = models.CharField(max_length=30)
    tt_batch = models.IntegerField()
    tt_major = models.CharField(max_length=4)
    tt_image = models.ImageField()

    def __str__(self):
        return self.tt_name

class SubEb(models.Model):
    s_id = models.AutoField
    s_name = models.CharField(max_length=30)
    s_batch = models.IntegerField()
    s_major = models.CharField(max_length=4)
    s_image = models.ImageField()

    def __str__(self):
        return self.s_name

class Blog(models.Model):
    b_id = models.AutoField
    b_link = models.URLField()
    b_date = models.DateField()

    
#python manage.py makemigrations
#python manage.py migrate
# python manage.py runserver