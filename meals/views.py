from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic, View
from .models import Recipe, Comment
from .forms import CommentForm
from django.http import HttpResponseRedirect

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



def delete_comment(request, comment_id):
    comment = Comment.objects.get(pk=comment_id)
    comment.delete()
    return HttpResponseRedirect(reverse('recipe_details', args=[comment.recipe.slug]))


def edit_comment(request, comment_id):
    comment = Comment.objects.get(pk=comment_id)
    form = CommentForm(request.POST or None, instance=comment)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('recipe_details', args=[comment.recipe.slug]))
    return render(
        request,
        "edit_comment.html",
        {
            "comment": comment,
            "form": form
        },
    )