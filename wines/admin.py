from django.contrib import admin
from .models import Wine
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
@admin.register(Wine)
class AdminForComment(admin.ModelAdmin):
    """This is for the admin to manage Wines"""
    list_filter = ('date_added', 'approved')
    list_display = ('name', 'type', 'posted_by', 'date_added', 'approved')
    search_fields = ('name', 'type', 'alcohol_precentage')

    def approve_wines(self, request, queryset):
        queryset.update(approved=True)