from rest_framework import serializers

from rating.models import Movie, Rating


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


class MailSerializer(serializers.Serializer):
    movie_id = serializers.CharField()
    movie_name = serializers.CharField()
    average_rating = serializers.DecimalField(max_digits=3, decimal_places=2)
