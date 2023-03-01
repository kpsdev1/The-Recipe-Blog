from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.views import generic, View
from .models import Recipe, Comment
from .forms import CommentForm, RecipeForm
from django.http import HttpResponseRedirect
from django.utils.text import slugify


def home(request):
    """ Returns the home page"""
    return render(request, 'index.html')


class RecipeList(generic.ListView):
    """Renders a list of all recipes and only dislays 6 per page"""
    paginate_by = 6
    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by('-date_added')
    template_name = 'recipes.html'


class RecipeDetails(View):
    """
    View to show the recipe detail page
    which displays all the recipe details
    """
    def get(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comments.order_by("date_added")
        liked = False
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "recipe_details.html",
            {
                "recipe": recipe,
                "comments": comments,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comments.order_by("date_added")
        liked = False
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.recipe = recipe
            comment.save()
            messages.success(request, 'Your Comment has been Posted')
        else:
            comment_form = CommentForm()

        return render(
            request,
            "recipe_details.html",
            {
                "recipe": recipe,
                "comments": comments,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )


def create_recipe(request):
    """This is the view that allows users add a recipe"""
    form = RecipeForm()
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            event.author = request.user
            event.slug = slugify(event.title)
            event.status = 1
            event.save()
            messages.success(request, 'Your recipe was added successfully')
            return redirect('recipes')

    context = {'form': form}
    return render(request, 'add_recipe.html', context)


def delete_recipe(request, recipe_id):
    """This is the view that allows users delete their recipe"""
    recipe = Recipe.objects.get(pk=recipe_id)
    recipe.delete()
    messages.success(request, 'Recipe was Deleted successfully')
    return redirect('recipes')


def edit_recipe(request, recipe_id):
    """This is the view that allows users update their recipe"""
    recipe = Recipe.objects.get(pk=recipe_id)
    form = RecipeForm(
        request.POST or None, request.FILES or None, instance=recipe)
    if form.is_valid():
        form.save()
        messages.success(request, 'Recipe was updated successful')
        return HttpResponseRedirect(
            reverse('recipe_details', args=[recipe.slug]))
    return render(
        request,
        "edit_recipe.html",
        {
            "recipe": recipe,
            "form": form
        },
    )


def delete_comment(request, comment_id):
    """This is the view that allows users delete their Comment"""
    comment = Comment.objects.get(pk=comment_id)
    comment.delete()
    messages.success(request, 'Comment was deleted successfully')
    return HttpResponseRedirect(
        reverse('recipe_details', args=[comment.recipe.slug]))


def edit_comment(request, comment_id):
    """This is the view that allows users edit their Comment"""
    comment = Comment.objects.get(pk=comment_id)
    form = CommentForm(request.POST or None, instance=comment)
    if form.is_valid():
        form.save()
        messages.success(request, 'Comment was updated successful')
        return HttpResponseRedirect(
            reverse('recipe_details', args=[comment.recipe.slug]))
    return render(
        request,
        "edit_comment.html",
        {
            "comment": comment,
            "form": form
        },
    )


class RecipeLike(View):
    """This is the class view to like and unlike a recipe"""
    def post(self, request, slug):
        recipe = get_object_or_404(Recipe, slug=slug)

        if recipe.likes.filter(id=request.user.id).exists():
            recipe.likes.remove(request.user)
        else:
            recipe.likes.add(request.user)
        return HttpResponseRedirect(reverse('recipe_details', args=[slug]))
