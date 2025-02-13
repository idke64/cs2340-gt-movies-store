from django.contrib import admin
from .models import Movie, Review

<<<<<<< HEAD
class MovieAdmin(admin.ModelAdmin):
    ordering = ['name']
    search_fields = ['name']
admin.site.register(Movie, MovieAdmin)
admin.site.register(Review)
=======
from .models import Movie
class MovieAdmin(admin.ModelAdmin):
    ordering = ['name']
    search_fields = ['name']
admin.site.register(Movie, MovieAdmin)
>>>>>>> 81323c8307e9938b336bdafd15e7d71f830a5bfd
