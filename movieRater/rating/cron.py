from django.core.mail import mail_admins
from django.db.models import Avg, F

from rating.models import Rating
from rating.serializer import MailSerializer


def notify_admins():
    try:
        print('>>> NOTIFYING ADMINS')
        rating = Rating.objects.values('movie_id').annotate(average_rating=Avg('rating')).annotate(movie_name=
                                                                                                   F('movie__name'))
        serializer = MailSerializer(rating, many=True)
        mail_admins(subject='Movie Ratings', message=serializer.data)
    except Exception as err:
        print('Failed sending mail due the following reason: {}'.format(str(err)))
