from django.shortcuts import render
from django.contrib import messages
from django.views import generic, View
from django.views.generic import ListView
from .models import Wine

class WineList(ListView):
    model = Wine
    template_name = 'wines.html'
