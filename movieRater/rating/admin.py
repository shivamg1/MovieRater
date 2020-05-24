from django.contrib import admin

from rating.models import User, Rating, Movie


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name')

    class Meta:
        models = User


admin.site.register(User, UserAdmin)


class RatingAdmin(admin.ModelAdmin):
    list_display = ("rating", "movie", "user")

    class Meta:
        models = Rating


admin.site.register(Rating, RatingAdmin)


class MovieAdmin(admin.ModelAdmin):
    list_display = ("name",)

    class Meta:
        models = Movie


admin.site.register(Movie, MovieAdmin)
