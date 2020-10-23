# Generated by Django 3.0.6 on 2020-10-23 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0003_auto_20201023_1728'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='genre',
            new_name='genre1',
        ),
        migrations.AddField(
            model_name='movie',
            name='genre2',
            field=models.CharField(choices=[('adventure', 'ADVENTURE'), ('fantasy', 'FANTASY'), ('science_fiction', 'SCIENCE FICTION'), ('action', 'ACTION'), ('comedy', 'COMEDY'), ('romance', 'ROMANCE')], default=None, max_length=40),
        ),
        migrations.AddField(
            model_name='movie',
            name='genre3',
            field=models.CharField(choices=[('adventure', 'ADVENTURE'), ('fantasy', 'FANTASY'), ('science_fiction', 'SCIENCE FICTION'), ('action', 'ACTION'), ('comedy', 'COMEDY'), ('romance', 'ROMANCE')], default=None, max_length=40),
        ),
    ]