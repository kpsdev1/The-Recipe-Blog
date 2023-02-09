# Generated by Django 3.2.16 on 2023-02-09 19:27

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Wine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('type', models.CharField(choices=[('choose', 'Choose'), ('red', 'Red Wine'), ('white', 'White Wine'), ('rose', 'Rose Wine'), ('sparkling', 'Sparkling Wine')], default='choose', max_length=14)),
                ('alcohol_precentage', models.IntegerField()),
                ('country_of_origin', models.CharField(max_length=50)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('posted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wines', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date_added'],
            },
        ),
    ]