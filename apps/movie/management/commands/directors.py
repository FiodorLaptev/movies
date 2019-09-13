from django.core.management.base import BaseCommand
from django.conf import settings
import os
import csv

from apps.movie.models import Movie, Genres, Keywords, Artist


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        movies = Movie.objects.all()
        i = 0
        for movie in movies:
            i += 1
            if movie.director_name:
                director, created = Artist.objects.get_or_create(
                    name=movie.director_name,
                    likes=movie.director_facebook_likes,
                    role='d'
                )
                movie.director = director
                movie.save()
