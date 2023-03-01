from .models import Comment, Recipe
from django import forms
from django_summernote.widgets import SummernoteWidget


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('info',)


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('title', 'image', 'description',
                  'ingredients', 'cooking_instructions')
        widgets = {
            'description': SummernoteWidget(),
            'ingredients': SummernoteWidget(),
            'cooking_instructions': SummernoteWidget(),
        }
