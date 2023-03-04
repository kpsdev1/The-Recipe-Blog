from .models import Comment, Recipe
from django import forms
from django_summernote.widgets import SummernoteWidget


class CommentForm(forms.ModelForm):
    """Comment Form"""
    class Meta:
        model = Comment
        fields = ('info',)


class RecipeForm(forms.ModelForm):
    """Recipe Form"""
    class Meta:
        model = Recipe
        fields = ('title', 'image', 'description',
                  'ingredients', 'cooking_instructions')
        widgets = {
            'description': SummernoteWidget(),
            'ingredients': SummernoteWidget(),
            'cooking_instructions': SummernoteWidget(),
        }
