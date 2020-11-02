from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *
# Create your views here.

def home(request):
    return render(request, 'home.html')

class MovieGenre(ListView):
    model = Movie
    paginate_by = 5

    def get_queryset(self):
        self.genre = self.kwargs['genre']
        return Movie.objects.filter(genre1=self.genre)

    def get_context_data(self, **kwargs):
        context = super(MovieGenre, self).get_context_data(**kwargs)
        context['movie_genre'] = self.genre
        return context

class MovieDetail(DetailView):
    model = Movie

    def get_object(self):
        object = super(MovieDetail, self).get_object()
        return object

    def get_context_data(self, **kwargs):
        context = super(MovieDetail, self).get_context_data(**kwargs)
        context['related_movie'] = Movie.objects.filter(
            genre1=self.get_object().genre1)
        return context