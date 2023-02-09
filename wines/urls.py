from . import views
from django.urls import path
from .views import *



urlpatterns = [
    path('', views.WineList.as_view(), name='wines'),
    path('add_wine/', views.add_wine, name='add_wine'),
]