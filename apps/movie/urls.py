from django.urls import path
from . import views

urlpatterns = [
    path('top/genres/', views.top_genres, name="top-genres"),
    path('top/directors/', views.top_directors, name="top-directors"),
    path('top/actors/', views.top_actors, name="top-actors"),

    # API
    path('api/v1/movies/', views.MoviesList.as_view()),
    path('api/v1/directors/', views.DirectorsList.as_view()),
    path('api/v1/genres/', views.GenresList.as_view()),
    path('api/v1/keywords/', views.KeywordsList.as_view())
]
