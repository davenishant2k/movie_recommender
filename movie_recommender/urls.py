"""movie_recommender URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from movie_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', HomeView.as_view(), name = 'home'),
    path('movie/', include('movie_app.urls', namespace='movie')),
    path('register/', register, name = 'register'),
    path('accounts/', include('allauth.urls')),
    path('contact/', contact, name = 'contact'),
    path('add_admin/', AddMovie_admin, name='add_admin'),
    path('add_movie_submission/', add_movie_submission, name='add_movie_submission'),
    path('about_us/', about_us, name = 'about_us'),
    path('', auth_views.LoginView.as_view(template_name = 'movie_app/login.html'), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'movie_app/logout.html'), name = 'logout'),
]
urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
