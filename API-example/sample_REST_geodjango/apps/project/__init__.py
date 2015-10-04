from os import environ
from django.core.exceptions import ImproperlyConfigured

consumer_key = environ.get('TWITTER_CONSUMER_KEY', None)
consumer_secret = environ.get('TWITTER_CONSUMER_SECRET', None)
access_token_secret = environ.get('TWITTER_OAUTH_SECRET', None)
access_token = environ.get('TWITTER_OAUTH_TOKEN', None)

if (not consumer_secret or not consumer_key
        or not access_token or not access_token_secret):
    raise ImproperlyConfigured(
        'Twitter credentials are missing. Please set env variables.')
