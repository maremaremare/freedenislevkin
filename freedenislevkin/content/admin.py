from django.contrib import admin
from .models import News_link, Photo, Video, News_category, News_post
# Register your models here.
admin.site.register(News_link)
admin.site.register(News_post)
admin.site.register(News_category)
admin.site.register(Photo)
admin.site.register(Video)
