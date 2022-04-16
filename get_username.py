import tweepy
import tweepy.models

def get_username(api: tweepy.API, reply_tweet: tweepy.models.Status):
    parent_tweet_id = reply_tweet.in_reply_to_status_id
    parent_tweet = api.get_status(parent_tweet_id)
    parent_user = parent_tweet.user
    return parent_user