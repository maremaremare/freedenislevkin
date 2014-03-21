# -*- coding: utf-8 -*-

from django.db import models
from embed_video.fields import EmbedVideoField

# Create your models here.


class News_link(models.Model):
    date = models.DateField()
    title = models.CharField(max_length=120)
    source = models.CharField(max_length=50)
    url = models.URLField()

    class Meta:
        verbose_name = ('Ссылка на статью')
        verbose_name_plural = ('Ссылки на статьи')

    def __unicode__(self):
        return self.title + ' - ' + self.source


class Photo(models.Model):

    image = models.ImageField(upload_to='photos/')

    class Meta:
        verbose_name = ('Фотография')
        verbose_name_plural = ('Фотографии')

    def __unicode__(self):
        pass


class Video(models.Model):

    video = EmbedVideoField()

    class Meta:
        verbose_name = ('Video')
        verbose_name_plural = ('Videos')

    def __unicode__(self):
        pass


class News_category(models.Model):

    title = models.CharField(max_length=50)
    slug = models.SlugField()

    class Meta:
        verbose_name = ('Категория событий')
        verbose_name_plural = ('Категории событий')

    def __unicode__(self):
        self.title


class News_post(models.Model):

    title = models.CharField(max_length=100)
    text = models.TextField()
    photos = models.ManyToManyField(Photo, null=True, blank=True)
    category = models.ForeignKey(News_category, null=True, blank=True)
    date = models.DateField(auto_now=True)

    class Meta:
        verbose_name = ('Событие')
        verbose_name_plural = ('События')

    def __unicode__(self):
        return self.title
