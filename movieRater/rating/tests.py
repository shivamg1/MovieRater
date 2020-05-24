from urllib.parse import urlencode

from django.test import TestCase
from rest_framework.test import APIClient
from movieRater.settings import BASE_DIR


class SignUpTest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.data = {
            'first_name': "sample",
            'last_name': "user",
            'email': 'sample@user.com',
            'password': 'sample@user.com'
        }

    def test_valid_signup(self):
        signup_data = urlencode(self.data)
        response = self.client.post('/signup', data=signup_data, content_type='application/x-www-form-urlencoded')
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.data, 'Following user created {}'.format(self.data['first_name']))

    def test_existing_email(self):
        signup_data = urlencode(self.data)
        response = self.client.post('/signup', data=signup_data, content_type='application/x-www-form-urlencoded')

        # Signing up with same email again
        response = self.client.post('/signup', data=signup_data, content_type='application/x-www-form-urlencoded')
        self.assertEquals(response.status_code, 400)

    def test_incomplete_data(self):
        self.data.pop('email')      # removing email from the request
        signup_data = urlencode(self.data)
        response = self.client.post('/signup', data=signup_data, content_type='application/x-www-form-urlencoded')
        self.assertEquals(response.status_code, 400)
        self.assertEquals(response.data, 'Required data not provided')


class LoginTest(TestCase):
    fixtures = [BASE_DIR + '/fixtures/data.json']

    def setup(self):
        self.client = APIClient()

    def test_valid_login(self):
        login_data = {
            'email': 'jon@doe.com',
            'password': 'jon@doe.com'
        }
        login_data = urlencode(login_data)
        response = self.client.post('/login', data=login_data, content_type='application/x-www-form-urlencoded')
        self.assertEquals(response.status_code, 200)

    def test_invalid_login(self):
        login_data = {
            'email': 'incorrect@incorrect.com',
            'password': 'incorrect@incorrect.com'
        }
        login_data = urlencode(login_data)
        response = self.client.post('/login', data=login_data, content_type='application/x-www-form-urlencoded')
        self.assertEquals(response.status_code, 400)


class BaseTestCase(TestCase):
    fixtures = [BASE_DIR + '/fixtures/data.json']

    def setUp(self):
        self.client = APIClient()
        self.header = {
            'HTTP_AUTHORIZATION': 'Bearer {}'.format(self.login()),
            'Content-Type': 'application/json'
        }

    def login(self):
        login_data = {
            'email': 'jon@doe.com',
            'password': 'jon@doe.com'
        }
        login_data = urlencode(login_data)
        response = self.client.post('/login', data=login_data, content_type='application/x-www-form-urlencoded')
        return response.data['access']


class MovieTest(BaseTestCase):

    def test_add_movie(self):
        movie_data = {'name': 'Batman'}
        movie_data = urlencode(movie_data)
        response = self.client.post('/movie', data=movie_data, content_type='application/x-www-form-urlencoded',
                                    **self.header)
        self.assertEquals(response.data['name'], 'Batman')

    def test_add_movie_with_invalid_data(self):
        movie_data = {'name': ''}
        movie_data = urlencode(movie_data)
        response = self.client.post('/movie', data=movie_data, content_type='application/x-www-form-urlencoded',
                                    **self.header)
        self.assertEquals(response.status_code, 400)

    def test_list_of_movies(self):
        response = self.client.get('/movie', **self.header)
        self.assertEquals(len(response.data), 1)  # as 1 movie is present in the fixture
        movie_data = {'name': 'Batman'}
        movie_data = urlencode(movie_data)
        self.client.post('/movie', data=movie_data, content_type='application/x-www-form-urlencoded', **self.header)
        response = self.client.get('/movie', **self.header)
        self.assertEquals(len(response.data), 2)  # a new movie is added


class RatingTest(BaseTestCase):

    def test_add_rating(self):
        data = {
            'rating': '3',
            'movie_id': 1
        }
        data = urlencode(data)
        response = self.client.post('/rate', data=data, content_type='application/x-www-form-urlencoded',
                                    **self.header)
        self.assertEquals(response.status_code, 200)

    def test_rating_twice(self):
        data = {
            'rating': '3',
            'movie_id': 1
        }
        data = urlencode(data)
        self.client.post('/rate', data=data, content_type='application/x-www-form-urlencoded', **self.header)

        # rating same movie again
        response = self.client.post('/rate', data=data, content_type='application/x-www-form-urlencoded',
                                    **self.header)
        self.assertEquals(response.status_code, 400)

    def test_rate_with_invalid_rating(self):
        data = {
            'rating': '10',
            'movie_id': 1
        }
        data = urlencode(data)
        response = self.client.post('/rate', data=data, content_type='application/x-www-form-urlencoded',
                                    **self.header)
        self.assertEquals(response.status_code, 400)

    def test_rate_own_movie(self):
        movie_data = {'name': 'Batman'}
        movie_data = urlencode(movie_data)
        # Creating a new movie
        response = self.client.post('/movie', data=movie_data, content_type='application/x-www-form-urlencoded',
                                    **self.header)
        movie_id = response.data['id']
        data = {
            'rating': '4',
            'movie_id': movie_id
        }
        data = urlencode(data)
        # Rating your own movie
        response = self.client.post('/rate', data=data, content_type='application/x-www-form-urlencoded',
                                    **self.header)
        self.assertEquals(response.status_code, 400)
