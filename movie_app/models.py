from django.db import models
from django.utils.text import slugify
from django.utils import timezone
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
    title = models.CharField(max_length = 100)
    description = models.TextField(max_length = 1000)
    image = models.ImageField(upload_to = 'music')
    cast = models.CharField(max_length = 500)
    genre = models.CharField(choices = GENRE_CHOICES, max_length = 40)
    imdbrating = models.IntegerField(default=0)

    slug = models.SlugField(blank = True, null = True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Music, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
