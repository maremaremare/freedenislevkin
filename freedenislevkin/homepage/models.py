# -*- coding: utf-8 -*-
from django.db import models
from solo.models import SingletonModel
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


class Slider(models.Model):

    text = models.CharField(unique=False, max_length=200)
    photo = models.ImageField(upload_to='homepage/slider/')
    # photo_full = ImageSpecField(source='photo',
    #                                   processors=[ResizeToFill(100, 50)],
    #                                   format='JPEG',
    #                                   options={'quality': 60})
    photo_thumb = ImageSpecField(source='photo',
                                 processors=[ResizeToFill(130, 54)],
                                 format='JPEG',
                                 options={'quality': 60})

    class Meta:
        verbose_name = ('Элемент слайдера')
        verbose_name_plural = ('Элементы слайдера')

    def __unicode__(self):
        return self.text


class SmallBoxPhoto(models.Model):

    title = models.CharField(null=True, max_length=50)
    photo = models.ImageField(upload_to='homepage/')
    photo_thumb = ImageSpecField(source='photo',
                                 processors=[ResizeToFill(285, 152)],
                                 format='JPEG',
                                 options={'quality': 60})

    class Meta:
        verbose_name = ('Фотография для главной страницы')
        verbose_name_plural = ('Фотографии для главной страницы')

    def __unicode__(self):
        return self.title


class Homepage(SingletonModel):

    textbox1 = models.CharField(max_length=300, null=True)
    textbox2 = models.CharField(max_length=300, null=True)
    textbox3 = models.CharField(max_length=300, null=True)

    photo1 = models.ForeignKey(SmallBoxPhoto, related_name='photo1', null=True)
    photo2 = models.ForeignKey(SmallBoxPhoto, related_name='photo2', null=True)
    photo3 = models.ForeignKey(SmallBoxPhoto, related_name='photo3', null=True)

    show_big_textbox = models.BooleanField(default=True)
    big_texbox_title = models.CharField(max_length=50, blank=True, null=True)
    big_textbox = models.TextField(blank=True, null=True)

    slider = models.ManyToManyField(Slider, null=True)

    show_news = models.BooleanField(default=True)

    class Meta:
        verbose_name = ('Главная страница')
        verbose_name_plural = ('Главная страница')
