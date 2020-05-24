from django.contrib.auth import authenticate
from django.db.models import Q
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from rating.models import User, Movie, Rating
from rating.serializer import MovieSerializer, RatingSerializer


class Signup(GenericAPIView):

    permission_classes = (AllowAny,)

    def post(self, request):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not first_name or not last_name or not email or not password:
            return Response("Required data not provided", 400)
        try:
            user = User.objects.create_user(email=email, password=password, first_name=first_name, last_name=last_name)
            return Response("Following user created {}".format(user.first_name), 200)
        except Exception as err:
            return Response("Following error occured while user creation: {}".format(str(err)), 400)


class Login(GenericAPIView):

    permission_classes = (AllowAny,)

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        if not email or not password:
            return Response("Required data not provided", 400)
        try:
            user = authenticate(email=email, password=password)
            token = RefreshToken.for_user(user)
            response = {
                'access': str(token.access_token),
                'refresh': str(token)
            }
            return Response(response, 200)
        except Exception as err:
            return Response("Following error occured while login: {}".format(str(err)), 400)


class MovieOperations(GenericAPIView):

    def post(self, request):
        name = request.POST.get('name')
        if not name:
            return Response("No argument found", 400)
        try:
            movie = Movie(name=name, created_by=request.user)
            movie.save()
            return Response("Movie added successfully", 200)
        except Exception as err:
            return Response("Following error occured while adding movie: {}".format(str(err)), 400)

    def get(self, request):
        movies = Movie.objects.all()
        ret_data = MovieSerializer(movies, many=True)
        return Response(ret_data.data, 200)


class RatingOperations(GenericAPIView):

    def post(self, request):
        rating = request.POST.get('rating')
        movie_id = request.POST.get('movie_id')
        if not rating or not movie_id:
            return Response("Required params not provided", 400)
        try:
            # movie = Movie.objects.get(~Q(created_by_id=request.user.id), id=movie_id)
            ser_data = dict()
            ser_data['user'] = request.user.id
            ser_data['movie'] = int(movie_id)
            ser_data['rating'] = rating
            serializer = RatingSerializer(data=ser_data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response("Rating added successfully", 200)
        except Exception as err:
            return Response("Following error occurred while adding rating: {}".format(str(err)), 400)
