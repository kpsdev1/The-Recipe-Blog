from . import views
from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('recipes/', views.RecipeList.as_view(), name='recipes'),
    path('<slug:slug>/', views.RecipeDetails.as_view(), name='recipe_details'),

]