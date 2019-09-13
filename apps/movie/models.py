from django.db import models


class Keywords(models.Model):
    # If separate plot keywords to another related model Django ORM will create "movie_plot_keywords" table with
    # relations. And after that I will get most popular plot keywords by django model aggregation:
    # https://docs.djangoproject.com/en/2.2/topics/db/aggregation/
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Genres(models.Model):
    # If separate genres to another related model Django ORM will create "movie_genres" table with relations
    # And after that I will get most popular genre by django model aggregation:
    # https://docs.djangoproject.com/en/2.2/topics/db/aggregation/
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Artist(models.Model):
    # Artist need to separate movie.directors_name and movie.actors_{n}_name for greater convenience.
    director = 'd'
    actor = 'a'
    TYPE = (
        (director, 'Director'),
        (actor, 'Actor'),
    )

    name = models.CharField(max_length=255)
    likes = models.PositiveIntegerField(null=True, blank=True)
    role = models.CharField(max_length=2, choices=TYPE, default=actor)

    def __str__(self):
        return self.name


class Movie(models.Model):
    movie_title = models.TextField(unique=True, null=True, blank=True)
    title_year = models.IntegerField(null=True, blank=True)
    movie_imdb_link = models.URLField(null=True, blank=True)

    color = models.TextField(null=True, blank=True)
    duration = models.PositiveIntegerField(null=True, blank=True)
    aspect_ratio = models.FloatField(null=True, blank=True)

    country = models.CharField(max_length=255, null=True, blank=True)
    language = models.CharField(max_length=255, null=True, blank=True)
    gross = models.PositiveIntegerField(null=True, blank=True)
    content_rating = models.CharField(max_length=50, null=True, blank=True)
    budget = models.IntegerField(null=True, blank=True)

    num_critic_for_reviews = models.PositiveIntegerField(null=True, blank=True)
    num_voted_users = models.PositiveIntegerField(null=True, blank=True)
    num_user_for_reviews = models.PositiveIntegerField(null=True, blank=True)
    imdb_score = models.FloatField(null=True, blank=True)
    cast_total_facebook_likes = models.PositiveIntegerField(null=True, blank=True)
    movie_facebook_likes = models.IntegerField(null=True, blank=True)
    facenumber_in_poster = models.IntegerField(null=True, blank=True)

    # Related fields
    director = models.ForeignKey(Artist, null=True, blank=True, related_name='director', on_delete=models.DO_NOTHING)
    plot_keywords = models.ManyToManyField(Keywords)
    genres = models.ManyToManyField(Genres)

    class Meta:
        # Default order by imdb_score because imdb is one of the most popular
        # movie websites
        ordering = ['-imdb_score']

    def __str__(self):
        return self.movie_title


class MovieActors(models.Model):
    # Because many actors have different amount of likes in different movies I decided to separate this relation
    # in different model

    # Actor
    artist = models.ForeignKey(Artist, on_delete=models.DO_NOTHING)
    # Movie
    movie = models.ForeignKey(Movie, on_delete=models.DO_NOTHING)
    # his likes ( in started data set there where actor_{n}_facebook_likes field )
    likes = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.artist.name
