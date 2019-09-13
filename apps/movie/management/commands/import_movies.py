from django.core.management.base import BaseCommand
from django.conf import settings
import os
import csv

from apps.movie.models import Movie, Genres, Keywords, Artist, MovieActors


class Command(BaseCommand):
    csv_data = os.path.join(settings.BASE_DIR, 'movie_metadata.csv')

    def has_value(self, value):
        if len(value) > 0:
            return value
        else:
            return 0

    def handle(self, *args, **kwargs):
        with open(self.csv_data, encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            i = 0
            for row in reader:
                i += 1

                try:
                    m = Movie.objects.get(movie_title=row['movie_title'])
                except Movie.DoesNotExist:
                    m = None

                if m is None:
                    movie = Movie.objects.create(
                        movie_title=row['movie_title'],
                        color=row['color'],
                        num_critic_for_reviews=self.has_value(row['num_critic_for_reviews']),
                        duration=self.has_value(row['duration']),
                        gross=self.has_value(row['gross']),
                        num_voted_users=self.has_value(row['num_voted_users']),
                        cast_total_facebook_likes=self.has_value(row['cast_total_facebook_likes']),
                        facenumber_in_poster=self.has_value(row['facenumber_in_poster']),
                        movie_imdb_link=row['movie_imdb_link'],
                        num_user_for_reviews=self.has_value(row['num_user_for_reviews']),
                        language=row['language'],
                        country=row['country'],
                        content_rating=self.has_value(row['content_rating']),
                        budget=self.has_value(row['budget']),
                        title_year=self.has_value(row['title_year']),
                        imdb_score=self.has_value(row['imdb_score']),
                        aspect_ratio=self.has_value(row['aspect_ratio']),
                        movie_facebook_likes=self.has_value(row['movie_facebook_likes'])

                        # director_name=row['director_name'],
                        # director_facebook_likes=self.has_value(row['director_facebook_likes']),
                        # actor_1_name=row['actor_1_name'],
                        # actor_1_facebook_likes=self.has_value(row['actor_1_facebook_likes']),
                        # actor_2_name=row['actor_2_name'],
                        # actor_2_facebook_likes=self.has_value(row['actor_2_facebook_likes']),
                        # actor_3_name=row['actor_3_name'],
                        # actor_3_facebook_likes=self.has_value(row['actor_3_facebook_likes']),

                    )

                    director, created = Artist.objects.get_or_create(
                        name=row['director_name'],
                        likes=row['director_facebook_likes'],
                        role='d'
                    )
                    movie.director = director

                    if row['actor_1_name']:
                        actor, created = Artist.objects.get_or_create(
                            # Important:
                            # don't search by role because the Artist can
                            # be as a director or an actor in a different movies
                            # don't use facebook likes because it is his likes in the Movie ( not total likes )
                            name=row['actor_1_name']
                        )
                        MovieActors.objects.create(
                            artist=actor,
                            movie=movie,
                            likes=row['actor_1_facebook_likes']
                        ).save()

                    if row['actor_2_name']:
                        actor, created = Artist.objects.get_or_create(
                            name=row['actor_2_name']
                        )
                        MovieActors.objects.create(
                            artist=actor,
                            movie=movie,
                            likes=row['actor_2_facebook_likes']
                        ).save()

                    if row['actor_3_name']:
                        actor, created = Artist.objects.get_or_create(
                            name=row['actor_3_name']
                        )
                        MovieActors.objects.create(
                            artist=actor,
                            movie=movie,
                            likes=row['actor_3_facebook_likes']
                        ).save()

                    genres = row['genres'].split('|')
                    for genre in genres:
                        if len(genre) > 0:
                            item, created = Genres.objects.get_or_create(name=genre)
                            movie.genres.add(item)

                    plot_keywords = row['plot_keywords'].split('|')
                    for keyword in plot_keywords:
                        if len(keyword) > 0:
                            item, created = Keywords.objects.get_or_create(name=keyword)
                            movie.plot_keywords.add(item)

                    movie.save()
