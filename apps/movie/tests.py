from django.test import TestCase

from .models import Movie, Keywords, Genres, Artist


class Movies(TestCase):

    # Keyword model creation test
    def keyword_create(self, name="keyword"):
        return Keywords.objects.create(name=name)

    def test_keyword_create(self):
        kw = self.keyword_create()
        self.assertTrue(isinstance(kw, Keywords))
        self.assertEqual(kw.__str__(), kw.name)

    # Genre model creation test
    def genre_create(self, name="Test genre"):
        return Genres.objects.create(name=name)

    def test_genre_create(self):
        ge = self.genre_create()
        self.assertTrue(isinstance(ge, Genres))
        self.assertEqual(ge.__str__(), ge.name)

    def artist_create(self, name="John Doe", likes=125, role="d"):
        return Artist.objects.create(name=name, likes=likes, role=role)

    def test_artist_create(self):
        ge = self.artist_create()
        self.assertTrue(isinstance(ge, Artist))

    # Movie model creation test
    def movie_create(self):
        keyword = self.keyword_create()
        genre = self.genre_create()
        director = self.artist_create()

        movie = Movie.objects.create(
            movie_title="Movie Test Title",
            title_year="2019",
            movie_imdb_link="http://imdb.com/link",
            color="Color",
            duration=125,
            aspect_ratio=12.5,
            country="UK",
            language="english",
            gross=50000,
            content_rating=50000,
            budget=50000,
            num_critic_for_reviews=123,
            num_voted_users=123,
            num_user_for_reviews=123,
            imdb_score=5.5,
            cast_total_facebook_likes=12,
            movie_facebook_likes=12,
            facenumber_in_poster=12,
            actor_1_name="John Doe",
            actor_1_facebook_likes=125,
            actor_2_name="John Doe",
            actor_2_facebook_likes=125,
            actor_3_name="John Doe",
            actor_3_facebook_likes=125,
        )
        movie.director = director
        movie.genres.add(genre)
        movie.plot_keywords.add(keyword)
        return movie

    def test_movie_create(self):
        ge = self.movie_create()
        self.assertTrue(isinstance(ge, Movie))
