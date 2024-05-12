from django.contrib import admin
from .models import Genre, Movie, Actor

# Register your models here.
@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
	list_display = ('name',)

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
	list_display = ('title', 'release_date', 'avg_rating')
	filter_horizontal = ('genres',)

@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
	list_display = ('first_name', 'last_name')
	filter_horizontal = ('movies',)