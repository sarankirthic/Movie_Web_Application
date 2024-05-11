from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Genre, Movie, Actor
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.
class GenreListView(ListView):
	model = Genre
	template_name = "movies/genre_list.html"
	context_object_name = "genre"


class MovieListView(ListView):
	model = Movie
	template_name = "movies/movie_list.html"
	context_object_name = "movies"


class MovieDetailView(DetailView):
	model = Movie
	template_name = "movies/movie_detail.html"
	context_object_name = "movie"


@login_required
def movie_rate(request, pk):
	movie = get_object_or_404(Movie, pk=pk)
	if request.method == "POST":
		rating = request.POST.get("rating")
		if rating:
			movie.ratings = rating
			movie.save()

	return render(request, 'movies/movie_rate.html', {'movie', movie})


class ActorListView(ListView):
	model = Actor
	template_name = "movies/actor_list.html"
	context_object_name = "actors"


class ActorDetailView(DetailView):
	model = Actor
	template_name = "movies/actor_list.html"
	context_object_name = 'actors'


class MovieCreateView(LoginRequiredMixin, CreateView):
	model = Movie
	fields = ['title', 'description', 'year', 'runtime', 'genres', 'poster']
	template_name = "movies/movie_form.html"
	success_url = reverse_lazy("movie-list")


class MovieUpdateView(LoginRequiredMixin, UpdateView):
	model = Movie
	fields = ['title', 'description' 'year', 'runtime', 'genres', 'poster']
	template_name = "movies/movie_form.html"
	success_url = reverse_lazy('movie-list')
	

class MovieDeleteView(LoginRequiredMixin, DeleteView):
	model = Movie
	template_name = "movies/movie_confirm_delete.html"
	success_url = reverse_lazy("movie-list")
