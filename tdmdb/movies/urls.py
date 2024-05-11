from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('genres/', views.GenreListView.as_view(), name='genre-list'),
    path('movies/', views.MovieListView.as_view(), name='movie-list'),
    path('movies/<int:pk>/', views.MovieDetailView.as_view(), name='movie-detail'),
    path('movies/<int:pk>/rate/', views.movie_rate, name='movie-rate'),
    path('actors/', views.ActorListView.as_view(), name='actor-list'),
    path('actors/<int:pk>/', views.ActorDetailView.as_view(), name='actor-detail'),
    path('movies/create/', views.MovieCreateView.as_view(), name='movie-create'),
    path('movies/<int:pk>/update/', views.MovieUpdateView.as_view(), name='movie-update'),
    path('movies/<int:pk>/delete/', views.MovieDeleteView.as_view(), name='movie-delete'),
]