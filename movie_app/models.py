from django.db import models
from django.utils.text import slugify
from django.utils import timezone
from django_mysql.models import ListCharField
from django.db.models import CharField
from datetime import date
# Create your models here.

GENRE_CHOICES = (
    ('adventure', 'ADVENTURE'),
    ('fantasy', 'FANTASY'),
    ('science_fiction', 'SCIENCE FICTION'),
    ('action', 'ACTION'),
    ('comedy', 'COMEDY'),
    ('romance', 'ROMANCE'),
)

class Movie(models.Model):
    title = models.CharField(max_length = 100, unique=True)
    description = models.TextField(max_length = 1000)
    image = models.ImageField(upload_to = 'movie')
    cast = models.CharField(max_length = 500)
    genre1 = models.CharField(choices = GENRE_CHOICES, max_length = 40)
    genre2 = models.CharField(choices = GENRE_CHOICES, max_length = 40,blank=True)
    genre3 = models.CharField(choices = GENRE_CHOICES, max_length = 40,blank=True)
    imdbrating = models.FloatField(default=0)
    box_office = models.FloatField(default=0)
    year_of_release = models.DateField(default=date.today)

    slug = models.SlugField(blank = True, null = True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Movie, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class MyRecommender(models.Model):
        movie_name = ListCharField(base_field=CharField(max_length=100),max_length=(6*100))
        user_name =  models.CharField(max_length = 100)
        liked_movie = models.CharField(max_length = 100)


class Comment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return "Comment {} by {}".format(self.body, self.name)
