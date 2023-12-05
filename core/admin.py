from django.contrib import admin

# Register your models here.

from .models import Category, Transcript, Video

admin.site.register(Category)
admin.site.register(Transcript)
admin.site.register(Video)


