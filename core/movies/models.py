from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Genre(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name


class Movie(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField(blank=True, null=True)
	release_date = models.DateField()
	genres = models.ManyToManyField(Genre, related_name='movies')
	avg_rating = models.FloatField(
		validators=[MinValueValidator(0.0), MaxValueValidator(5.0)],
		default=0.0
	)
	poster = models.ImageField(upload_to="posters", null=True, blank=True)

	def __str__(self):
		return self.title


class Actor(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	movies = models.ManyToManyField(Movie, related_name='actors')

	def __str__(self):
		return f"{self.first_name} {self.last_name}"