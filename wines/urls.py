from . import views
from django.urls import path
from .views import *


urlpatterns = [
    path(
        '<int:pk>/delete_wine/', WineDeleteView.as_view(), name='delete_wine'
        ),
    path('<int:pk>/edit_wine/', WineUpdateView.as_view(), name='edit_wine'),
    path('add_wine/', WineCreateView.as_view(), name='add_wine'),
    path('<int:pk>/', WineDetailView.as_view(), name='wine_details'),
    path('', views.WineList.as_view(), name='wines'),
]
