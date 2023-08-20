from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from myappone.models import Movie

# Create your views here.

# def movie_list(request):
#     movies = Movie.objects.all()
#     return HttpResponse(movies.values())

#--------------------------------------------

def movie_list(request):
    movies = Movie.objects.all()

    data = {
        'movies':list(movies.values())
    }

    return JsonResponse(data)

#--------------------------------------------

def movie_details(request, pk):
    movie = Movie.objects.get(pk=pk)

    data = {
        'movie':movie.name,
        'description':movie.description,
        'active':movie.activate
    }

    return JsonResponse(data)