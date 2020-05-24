from rest_framework import serializers

from rating.models import User, Movie, Rating


class MovieSerializer(serializers.ModelSerializer):

    created_by = serializers.SerializerMethodField()

    def get_created_by(self, obj):
        return "{} {}".format(obj.created_by.first_name, obj.created_by.last_name)

    class Meta:
        model = Movie
        fields = ("id", "name", "created_by")


class RatingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rating
        fields = '__all__'

