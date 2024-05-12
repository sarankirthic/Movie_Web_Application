from django.shortcuts import render
from .models import Genre, Movie, Actor
from .serializers import MovieSerializer
from rest_framework import generics

# Create your views here.
def movie_list(request):
	movies = Movie.objects.all()
	context = {'movies': movies}
	return render(request, 'movies/movie_list.html', context)

def movie_detail(request, movie_id):
	movie = get_object_or_404(Movie, pk=movie_id)
	context = {'movie': movie}
	return render(request, 'movies/movie_detail.html', context)

def actor_list(request):
	actors = Actor.objects.all()
	context = {'actors': actors}
	return render(request, 'movies/actor_list.html', context)

def actor_detail(request, actor_id):
	actor = get_object_or_404(Actor, pk=actor_id)
	context = {'actor': actor}
	return render(request, 'movies/actor_detail.html', context)

def genre_list(request):
	genres = Genre.objects.all()
	context = {'genres': genres}
	return render(request, 'movies/genre_list.html', context)

def genre_detail(request, genre_id):
	genre = get_object_or_404(Genre, pk=genre_id)
	movies = genre.movies.all()
	context = {'genre': genre, 'movies': movies}
	return render(request, 'movies/genre_detail.html', context)\

# for API
class MovieListCreateView(generics.ListCreateAPIView):
	queryset = Movie.objects.all()
	serializer_class = MovieSerializer

class MovieDetailView(generics.RetrieveAPIView):
	queryset = Movie.objects.all()
	serializer_class = MovieSerializer