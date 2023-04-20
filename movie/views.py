from django.shortcuts import render
from .models import Movie
from .forms import MovieReviewForm
from django.shortcuts import get_object_or_404


def movies(request):
    all_movies = Movie.objects.all()
    context = {
        'movies': all_movies,
    }
    return render(request=request, template_name='movies/movies.html', context=context)


def review(request, movie_id):
    if request.method == "POST":
        form = MovieReviewForm(request.POST)
        if form.is_valid():
            form.save()
    one_movie = get_object_or_404(Movie, pk=movie_id)
    context = {
        'one_movie': one_movie,
        'form': MovieReviewForm(),
    }
    return render(request, "movies/movie.html", context)
