from django.urls import path, include
from .views import *

app_name = 'movie'

urlpatterns = [
    path('', MovieList.as_view(), name = 'movie_list'),
    path('genre/<str:genre>', MovieGenre.as_view(), name ='movie_genre'),
    path('<slug:slug>', MovieDetail.as_view(), name = 'movie_detail'),
    path('recommend/<str:username>/<str:title>', RecommendListView.as_view(), name = 'movie_recommend'),
    path('my_recommendations/<str:username>',MyRecommendView.as_view(),name='my_recommendations'),
    path('my_liked/<str:username>',MyLikedView.as_view(),name='my_liked'),
]
