from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('list/', views.movie_list, name='movie_list'),
    path('create/',views.movie_create, name='create'),

]