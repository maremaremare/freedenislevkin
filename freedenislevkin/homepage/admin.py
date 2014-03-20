from django.contrib import admin

# Register your models here.
from django.contrib import admin
from solo.admin import SingletonModelAdmin
from .models import Homepage, Slider, SmallBoxPhoto

admin.site.register(Homepage, SingletonModelAdmin)
admin.site.register(Slider)
admin.site.register (SmallBoxPhoto)