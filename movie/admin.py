from django.contrib import admin
from .models import Movie, Actor

#
# @admin.action(description='Change genre to SciFi')
# def change_genre(modeladmin, request, queryset):
#     queryset.update(genre='SciFi')
#
#
# class MovieAdmin(admin.ModelAdmin):
#     list_display = ('title', 'actors', 'genre')
#     actions = [change_genre]


admin.site.register(Movie)
admin.site.register(Actor)
