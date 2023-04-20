from django.contrib.auth.models import User
from django.db import models
from django_countries.fields import CountryField


class BaseModel(models.Model):
    objects = models.Manager()

    class Meta:
        abstract = True


class Actor(BaseModel):
    name = models.CharField(max_length=100, blank=False)
    surname = models.CharField(max_length=100, blank=False)
    date_of_birth = models.DateField(blank=False)
    country = CountryField(blank=True)

    def __str__(self):
        return f"{self.name} {self.surname}"


GENRE = [
    ('Comedy', 'Comedy'),
    ('Action', 'Action'),
    ('Horror', 'Horror'),
    ('Fantasy', 'Fantasy'),
    ('Romance', 'Romance'),
    ('Drama', 'Drama'),
    ('SciFi', 'SciFi'),
    ('Documentary', 'Documentary'),
]


class Movie(BaseModel):
    title = models.CharField(max_length=100, blank=False)
    actors = models.ManyToManyField(Actor)
    country = CountryField(blank=True)
    genre = models.CharField(choices=GENRE, max_length=50)
    date_uploaded = models.DateField(blank=False)

    def __str__(self):
        return f"{self.title}"


class MovieReview(models.Model):
    movie = models.ForeignKey('movie', on_delete=models.SET_NULL, null=True, blank=True)
    reviewer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    content = models.TextField("Your Review", max_length=2000)

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = 'Comments'
        ordering = ['-date_created']

    def __str__(self):
        return f"{self.content}"

