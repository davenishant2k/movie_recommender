# Generated by Django 3.0.6 on 2020-10-23 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0004_auto_20201023_1753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='genre2',
            field=models.CharField(blank=True, choices=[('adventure', 'ADVENTURE'), ('fantasy', 'FANTASY'), ('science_fiction', 'SCIENCE FICTION'), ('action', 'ACTION'), ('comedy', 'COMEDY'), ('romance', 'ROMANCE')], max_length=40),
        ),
        migrations.AlterField(
            model_name='movie',
            name='genre3',
            field=models.CharField(blank=True, choices=[('adventure', 'ADVENTURE'), ('fantasy', 'FANTASY'), ('science_fiction', 'SCIENCE FICTION'), ('action', 'ACTION'), ('comedy', 'COMEDY'), ('romance', 'ROMANCE')], max_length=40),
        ),
    ]
