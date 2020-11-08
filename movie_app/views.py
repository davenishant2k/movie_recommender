import recommend
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *
from django.contrib.auth import login, authenticate
from .forms import *
# Create your views here.

class MovieList(ListView):
    model = Movie
    paginate_by = 5

class HomeView(ListView):
    model = Movie
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['top_rated'] = Movie.objects.all().order_by('-imdbrating')
        context['year_of_release'] = Movie.objects.all().order_by('-year_of_release')
        context['box_office'] = Movie.objects.all().order_by('-box_office')
        return context

class MovieSearch(ListView):
    model = Movie
    paginate_by = 5

    def get_queryset(self):
        query = self.request.GET.get('query')
        if query:
            object_list = self.model.objects.filter(title__icontains=query)
        else:
            object_list = self.model.objects.none()
        return object_list

def login(request):
    return render(request, 'movie_app/login.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')

    else:
        form = UserRegisterForm()
    return render(request, 'movie_app/register.html', {'form': form})

class MovieDetail(DetailView):
    model = Movie

    def get_object(self):
        object = super(MovieDetail, self).get_object()
        return object

    def get_context_data(self, **kwargs):
        context = super(MovieDetail, self).get_context_data(**kwargs)
        context['related_movie'] = Movie.objects.filter(
            genre1=self.get_object().genre1)
        context['genre'] = self.get_object().genre1                             
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
    model = Movie,MyRecommender
    template_name = 'movie_app/recommendations.html'
    context_object_name = 'movies'
    # paginate_by = 6
    def get_queryset(self):
        
        self.title = self.kwargs['title']
        self.username = self.kwargs['username']
        # print(self.title)
        # print(self.username)
        recommend_list = []
        temp_list = recommend.get_recommendations(self.title)
        recommend_list.extend(temp_list)
        #print(recommend_list)
        r = MyRecommender(user_name=self.username, movie_name=recommend_list, liked_movie=self.title)
        r.save()
        return Movie.objects.filter(title__in=recommend_list)


class MyRecommendView(ListView):
    model = MyRecommender
    template_name = 'movie_app/myrecommmender_list.html'
    context_object_name = 'movies'
    #paginate_by = 5

    def get_queryset(self):
        lst=[]
        self.username = self.kwargs['username']
        qs1 = MyRecommender.objects.filter(user_name=self.username)
        for p in qs1:
            for x in p.movie_name:
                lst.append(x)
        print(lst)
        return Movie.objects.filter(title__in=lst)

class MyLikedView(ListView):
    model = MyRecommender
    template_name = 'movie_app/myliked_list.html'
    context_object_name = 'movies'
    #paginate_by = 5

    def get_queryset(self):
        lst=[]
        self.username = self.kwargs['username']
        qs1 = MyRecommender.objects.filter(user_name=self.username)
        for p in qs1:
            lst.append(p.liked_movie)
        print(lst)
        return Movie.objects.filter(title__in=lst)

def contact(request):
    return render(request, 'contact.html')

def about_us(request):
    return render(request, 'about_us.html')