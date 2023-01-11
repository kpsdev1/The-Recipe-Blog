from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Recipe, Comment

def home(request):
    return render(request, 'index.html')

class RecipeList(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by('-date_added')
    template_name = 'recipes.html'
    