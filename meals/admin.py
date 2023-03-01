from django.contrib import admin
from .models import Recipe, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Recipe)
class AdminForRecipe(SummernoteModelAdmin):
    """This is for the admin to manage recipes"""
    list_filter = ('status', 'date_added')
    list_display = ('title', 'slug', 'author', 'date_added')
    search_fields = ['title', 'description', 'author']
    prepopulated_fields = {'slug': ('title',)}
    summernote_fieds = ('ingredients', 'cooking_instructions')


@admin.register(Comment)
class AdminForComment(admin.ModelAdmin):
    """This is for the admin to manage Comments"""
    list_filter = ('date_added',)
    list_display = ('name', 'info', 'date_added')
    search_fields = ('name', 'email', 'info')
