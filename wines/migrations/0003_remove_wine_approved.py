# Generated by Django 3.2.16 on 2023-02-10 16:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wines', '0002_wine_approved'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wine',
            name='approved',
        ),
    ]