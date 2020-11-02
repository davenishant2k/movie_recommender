from django.urls import path, include
from .views import *

app_name = 'movie'

urlpatterns = [
    # path('', MusicList.as_view(), name = 'music_list'),
    # path('year/<int:year>', MusicYear.as_view(), name = 'music_year'),
    # path('search/', MusicSearch.as_view(), name = 'music_search'),
    # path('language/<str:lang>', MusicLanguage.as_view(), name = 'music_language'),
    path('genre/<str:genre>', MovieGenre.as_view(), name = 'movie_genre'),
    path('<slug:slug>', MovieDetail.as_view(), name = 'movie_detail'),
]
