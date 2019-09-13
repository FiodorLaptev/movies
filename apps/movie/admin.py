from django.contrib import admin
from .models import Keywords, Genres, Movie, Artist, MovieActors

admin.site.register(MovieActors)
admin.site.register(Keywords)
admin.site.register(Artist)
admin.site.register(Genres)
admin.site.register(Movie)
