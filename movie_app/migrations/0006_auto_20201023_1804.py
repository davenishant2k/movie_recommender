# Generated by Django 3.0.6 on 2020-10-23 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0005_auto_20201023_1756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='imdbrating',
            field=models.FloatField(default=0),
        ),
    ]