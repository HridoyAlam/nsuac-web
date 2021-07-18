from django.db import models
from django.contrib import admin
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