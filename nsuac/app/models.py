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