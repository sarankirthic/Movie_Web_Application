from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
	class Meta:
		model = Movie
		fields = ['title', 'description', 'release_date', 'runtime', 'genres', 'poster']