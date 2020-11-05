import recommend
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *
# Create your views here.

def home(request):
    return render(request, 'home.html')


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

class MovieGenre(ListView):
    model = Movie
    paginate_by = 5

    def get_queryset(self):
        lst=[]
        self.genre = self.kwargs['genre']
        qs1 = Movie.objects.filter(genre1=self.genre)
        qs2 = Movie.objects.filter(genre2=self.genre)
        qs3 = Movie.objects.filter(genre3=self.genre)
        return  qs1.union(qs2,qs3)

    def get_context_data(self, **kwargs):
        context = super(MovieGenre, self).get_context_data(**kwargs)
        context['movie_genre'] = self.genre
        return context
## MACHINE LEARNING PART
class RecommendListView(ListView):
    model = Movie
    template_name = 'recommendations.html'
    context_object_name = 'movies'
    # paginate_by = 6
    def get_queryset(self):
        # user = get_object_or_404(User, username=self.kwargs.get('username'))
        # profile = Profile.objects.get(user=user)
        # history_model = ThroughModel.objects.filter(profile=profile).order_by('-date_viewed')
        # for obj in history_model:
        #     title = obj.movie.title
        self.title = self.kwargs['title']
        print(self.title)
        recommend_list = []
        temp_list = recommend.get_recommendations(self.title)
        recommend_list.extend(temp_list)
        print(recommend_list)
        return Movie.objects.filter(title__in=recommend_list)

    # def get_queryset(self):
    #     # user = get_object_or_404(User, username=self.kwargs.get('username'))
    #     # profile = Profile.objects.get(user=user)
    #     # history_model = ThroughModel.objects.filter(profile=profile).order_by('-date_viewed')
    #     recommend_list = []
    #     # for obj in history_model:
    #     #     title = obj.movie.title
    #     self.title = self.kwargs['title']
    #     print(self.title)

    #     temp_list = recommend.get_recommendations(self.title)
    #     recommend_list.extend(temp_list)
    #     print(recommend_list)
    #     return Movie.objects.filter(title__in=recommend_list).order_by('-imdbrating')
        
    # def get_context_data(self, **kwargs):
    #     context = super(RecommendListView, self).get_context_data(**kwargs)
    #     context['recommends'] = self.title
    #     return context
    