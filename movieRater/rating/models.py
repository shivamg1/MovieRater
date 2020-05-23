from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import CASCADE, SET_NULL


class User(AbstractUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class Movie(models.Model):
    name = models.CharField(max_length=250)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="movie_user", on_delete=CASCADE)


class Rating(models.Model):
    RATING_CHOICES = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5)
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="rating_user", on_delete=CASCADE)
    movie = models.ForeignKey(Movie, related_name="rating_movie", on_delete=CASCADE)
    rating = models.IntegerField(choices=RATING_CHOICES)

    class Meta:
        unique_together = ("user", "movie",)
