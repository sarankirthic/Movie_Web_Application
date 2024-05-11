from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Genre(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name

class Movie(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField()
	year = models.DateField()
	runtime = models.DurationField()
	ratings = models.DecimalField(max_digits=3, decimal_places=1, validators=[MinValueValidator(1), MaxValueValidator(5)], null=True, blank=True)
	genres = models.ManyToManyField(Genre, related_name="movies")
	poster = models.ImageField(upload_to="posters", null=True, blank=True)

	def __str__(self):
		return self.title

class Actor(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	dob = models.DateField(null=True, blank=True)
	movies = models.ManyToManyField(Movie, related_name="actors")

	def __str__(self):
		return f"(self.first_name) (self.last_name)"
