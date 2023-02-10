from django.contrib import admin
from .models import Wine
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
@admin.register(Wine)
class AdminForComment(admin.ModelAdmin):
    """This is for the admin to manage Wines"""
    list_filter = ('date_added', 'type')
    list_display = ('name', 'type', 'posted_by', 'date_added')
    search_fields = ('name', 'type', 'alcohol_precentage')