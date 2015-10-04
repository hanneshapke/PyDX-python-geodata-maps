import tweepy
from . import (consumer_key, consumer_secret,
               access_token, access_token_secret)
from .models import CallLocation, CallType


def get_twitter_api():
    """ Create twitter API object """
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    return tweepy.API(auth)


def get_twitter_feed(username, since_id=None, update_count=20):
    """ Retrieves the twitter messages for a given username """
    return get_twitter_api().user_timeline(
        screen_name=username,
        count=update_count,
        since_id=since_id)


def parse_twitter_status(status):
    """ Parse a twitter status object into a dict which can be push into
    a Django model object """
    msg = status.text
    address = msg[msg.find('at ') + 3:msg.find('OR [') + 2]
    return {
        'status_id': status.id,
        'timestamp': status.created_at,
        'call_type': CallType.objects.get_or_create(
            name=msg[0:msg.find('at ')])[0],
        'address': address if address else 'Portland, OR'
    }


def set_call_locations(username, since_id=None):
    """ save latest downloaded status updates """
    # get last entry
    last_entry = CallLocation.objects.first()
    # get latest twitter status updates
    if hasattr(last_entry, 'status_id'):
        status_id = last_entry.status_id
    else:
        status_id = None
    try:

        count = 0
        twitter_msgs = get_twitter_feed(username, status_id)
        for msg in twitter_msgs:
            # save new incidences since last update
            obj = CallLocation(**parse_twitter_status(msg))
            obj.save()
            count += 1
        message = "Added %s new calls to the emergency call register" % count
        print(message)
        return message, 200

    except tweepy.TweepError:
        return "Something went really wrong", 500

    except tweepy.RateLimitError:
        return "Exceeded twitter limit", 500
