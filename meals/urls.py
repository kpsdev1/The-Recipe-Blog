from . import views
from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('recipes/', views.RecipeList.as_view(), name='recipes'),
    path('add_recipe/', views.create_recipe, name='add_recipe'),
    path('<slug:slug>/', views.RecipeDetails.as_view(), name='recipe_details'),
    path('delete_recipe/<recipe_id>', views.delete_recipe, name='delete_recipe'),
    path('edit_recipe/<recipe_id>', views.edit_recipe, name='edit_recipe'),
    path('delete_comment/<comment_id>', views.delete_comment, name='delete_comment'),
    path('edit_comment/<comment_id>', views.edit_comment, name='edit_comment'),
    path('like/<slug:slug>', views.RecipeLike.as_view(), name='recipe_like'),

]