# Generated by Django 3.1.3 on 2020-11-07 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0009_myrecommender_liked_movie'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='box_office',
            field=models.FloatField(default=0),
        ),
    ]