from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.urls import reverse

WINE_CHOICES = (
    ('choose', 'Choose'),
    ('red', 'Red Wine'),
    ('white', 'White Wine'),
    ('rose', 'Rose Wine'),
    ('sparkling', 'Sparkling Wine'),
)


class Wine(models.Model):
    name = models.CharField(max_length=150, blank=False)
    image = CloudinaryField('image', blank=False)
    type = models.CharField(max_length=14, choices=WINE_CHOICES, default='choose', blank=False)
    alcohol_precentage = models.IntegerField(blank=False)
    country_of_origin = models.CharField(max_length=50, blank=False)
    date_added = models.DateTimeField(auto_now_add=True)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="wines")
    


    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('wine_details', args=[str(self.id)])