from django.utils.html import format_html
from django.contrib import admin
from .models import Slider,Upcoming_event, Subscribers, Contacts, Gallery
from .models import *
# Register your models here.
admin.site.register(Slider)
admin.site.register(Upcoming_event)
admin.site.register(Subscribers)
admin.site.register(Contacts)
admin.site.register(Badminton)
admin.site.register(Basketball)
admin.site.register(Football)
admin.site.register(TableTennis)
admin.site.register(Cricket)
class GalleryAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" width="auto" height="200px" />'.format(obj.image.url))

    image_tag.short_description = 'Image Preview'
    # list_display = ['image_tag']-> This will show image in your dashboard instead of First Image, Second Image and Third Image
    readonly_fields = ['image_tag']
admin.site.register(Gallery, GalleryAdmin)
