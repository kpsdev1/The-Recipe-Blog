from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Recipe

def home(request):
    return render(request, 'index.html')

class RecipeList(generic.ListView):
    paginate_by = 6
    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by('-date_added')
    template_name = 'recipes.html'


class RecipeDetails(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)

        return render(
            request,
            "recipe_details.html",
            {
                "recipe": recipe,
            },
        )