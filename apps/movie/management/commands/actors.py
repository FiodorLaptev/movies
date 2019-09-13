from django.core.management.base import BaseCommand
from django.conf import settings
import os
import csv

from apps.movie.models import Movie, Artist, MovieActors


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        movies = Movie.objects.all()
        i = 0
        for movie in movies:
            i += 1
            if movie.actor_1_name:
                actor, created = Artist.objects.get_or_create(
                    # don't search by facebook likes or role because the Artist can
                    # be as a director or an actor in a different movies
                    name=movie.actor_1_name
                )
                MovieActors.objects.create(
                    artist=actor,
                    movie=movie,
                    likes=movie.actor_1_facebook_likes
                ).save()

            if movie.actor_2_name:
                actor, created = Artist.objects.get_or_create(
                    name=movie.actor_2_name
                )
                MovieActors.objects.create(
                    artist=actor,
                    movie=movie,
                    likes=movie.actor_2_facebook_likes
                ).save()

            if movie.actor_3_name:
                actor, created = Artist.objects.get_or_create(
                    name=movie.actor_3_name
                )
                MovieActors.objects.create(
                    artist=actor,
                    movie=movie,
                    likes=movie.actor_3_facebook_likes
                ).save()

