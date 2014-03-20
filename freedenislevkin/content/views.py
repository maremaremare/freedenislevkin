# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView
from .models import News_link


class PressListView(ListView):
    model = News_link
    template_name = "press.html"
