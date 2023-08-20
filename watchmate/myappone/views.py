from django.shortcuts import render
from django.http import HttpResponse
from myappone.models import Movie

# Create your views here.

def movie_list(request):
    movies = Movie.objects.all()
    return HttpResponse(movies.values())