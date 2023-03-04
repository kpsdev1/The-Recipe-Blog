from .models import Wine
from django import forms


class WineForm(forms.ModelForm):
    """Wine Form"""
    class Meta:
        model = Wine
        fields = ('name', 'image', 'type',
                  'alcohol_precentage', 'country_of_origin')
