from django.http import JsonResponse
from django.db.models import Count, Avg
from rest_framework import generics
from rest_framework.permissions import AllowAny

from .models import Movie, Genres, Keywords, Artist, MovieActors
from .serializers import MovieSerializer, GenresSerializer, ArtistSerializer, KeywordsSerializer, MovieActorsSerializer


def top_genres(request):
    # Getting most popular genre by Django model aggregation
    genres = Genres.objects.annotate(movies=Count('movie'))
    # serialize data
    data = GenresSerializer(genres, many=True)
    # Return JsonResponse
    return JsonResponse({
        'genres': data.data[:10]
    })


def top_directors(request):
    directors_avg_movie_rating = []
    # Loop through all directors
    for director in Artist.objects.filter(role='d'):
        # Loop through all director movies
        avg = Movie.objects.filter(director=director).aggregate(
            # Getting average values from different scores, likes and number of critics, users, reviews
            Avg('imdb_score'),
            Avg('movie_facebook_likes'),
            Avg('num_critic_for_reviews'),
            Avg('num_voted_users'),
            Avg('num_user_for_reviews'),
        )
        obj = {
            'director': director.name,
            # Here can be a lot formulas for getting top list by combinations of different values,
            # But for now it's just average value of all data. Movie as it self contain different opinions from
            # different people, so there the right way will be compare movies in different sores, instead of trying to
            # combine them all together. But I still think that the overall significance of various indicators can still
            # give the average cultural importance of films.
            'movies_score': (avg['imdb_score__avg'] + avg['movie_facebook_likes__avg'] + avg[
                'num_critic_for_reviews__avg'] + avg['num_voted_users__avg'] + avg['num_user_for_reviews__avg']) / 5

        }
        # add director in total list
        directors_avg_movie_rating.append(obj)

    return JsonResponse({
        # return directors list, sort them by 'movie_score', reverse it to start from biggest value
        # and limit by 10 items
        'directors': sorted(directors_avg_movie_rating, key=lambda i: i['movies_score'], reverse=True)[:10]
    })


def top_actors(request):
    result = []
    amr = MovieActors.objects.all()
    actors = Artist.objects.filter(role='a')

    for actor in actors:
        all_actors_movies = amr.filter(artist=actor)
        # getting average value of actor likes in movies
        actor_movies_actor_likes = all_actors_movies.aggregate(Avg('likes'))['likes__avg']
        total_actor_movies_score = 0
        for m in all_actors_movies:
            # getting total actors movie "score" ( simple the average value of different scores )
            total_actor_movies_score += (m.movie.num_critic_for_reviews + m.movie.num_voted_users
                                         + m.movie.num_user_for_reviews + m.movie.imdb_score
                                         + m.movie.cast_total_facebook_likes + m.movie.movie_facebook_likes
                                         + m.movie.facenumber_in_poster) / 7
        obj = {
            'actor': actor.name,
            # sum the actors likes and his movies total scores
            'actor_score': actor_movies_actor_likes + total_actor_movies_score,
        }
        result.append(obj)

    return JsonResponse({
        # return directors list, sort them by 'movie_score', reverse it to start from biggest value
        # and limit by 10 items
        'actors': sorted(result, key=lambda i: i['actor_score'], reverse=True)[:10]
    })


# Standard Django Rest Framework class based views to handle models
class MoviesList(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = MovieSerializer


class GenresList(generics.ListCreateAPIView):
    queryset = Genres.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = GenresSerializer


class KeywordsList(generics.ListCreateAPIView):
    queryset = Keywords.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = KeywordsSerializer


class DirectorsList(generics.ListCreateAPIView):
    queryset = Artist.objects.filter(role='d')
    permission_classes = (AllowAny,)
    serializer_class = ArtistSerializer
