from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
	path('movies/', views.movie_list, name='movie-list'),
	path('movies/<int:movie_id>/', views.movie_detail, name='movie-detail'),
	path('actors/', views.actor_list, name='actor-list'),
	path('actors/<int:actor_id>/', views.actor_detail, name='actor-detail'),
	path('genres/', views.genre_list, name='genre-list'),
	path('genres/<int:genre_id>/', views.genre_detail, name='genre-detail'),
	path('api/', views.MovieListCreateView.as_view(), name='movie-list-create'),
	path('api/<int:pk>/', views.MovieDetailView.as_view(), name='movie-detail'),
]