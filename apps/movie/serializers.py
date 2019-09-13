from rest_framework.serializers import ModelSerializer
from .models import Movie, Artist, Genres, Keywords, MovieActors


class ArtistSerializer(ModelSerializer):
    class Meta:
        model = Artist
        fields = (
            'name',
            'likes',
            'role',
        )


class GenresSerializer(ModelSerializer):
    class Meta:
        model = Genres
        fields = (
            'name',
        )


class KeywordsSerializer(ModelSerializer):
    class Meta:
        model = Keywords
        fields = (
            'name',
        )


class MovieSerializer(ModelSerializer):
    director = ArtistSerializer()
    plot_keywords = KeywordsSerializer(many=True)
    genres = GenresSerializer(many=True)

    class Meta:
        model = Movie
        fields = (
            'movie_title',
            'title_year',
            'movie_imdb_link',
            'color',
            'duration',
            'aspect_ratio',
            'country',
            'language',
            'gross',
            'content_rating',
            'budget',
            'num_critic_for_reviews',
            'num_voted_users',
            'num_user_for_reviews',
            'imdb_score',
            'cast_total_facebook_likes',
            'movie_facebook_likes',
            'facenumber_in_poster',
            # 'actor_1_name',
            # 'actor_1_facebook_likes',
            # 'actor_2_name',
            # 'actor_2_facebook_likes',
            # 'actor_3_name',
            # 'actor_3_facebook_likes',
            'director',
            'plot_keywords',
            'genres',
        )


class MovieActorsSerializer(ModelSerializer):
    class Meta:
        model = MovieActors
        fields = (
            'artist',
            'movie',
            'likes'
        )
