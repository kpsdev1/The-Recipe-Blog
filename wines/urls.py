from . import views
from django.urls import path
from .views import *



urlpatterns = [
    path('', views.WineList.as_view(), name='wines'),
]