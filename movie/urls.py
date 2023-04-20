from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.movies, name="movies"),
    path("<int:movie_id>/", views.review, name="movie_movie"),

    path('accounts/', include('django.contrib.auth.urls')),

]