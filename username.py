import tweepy
import tweepy.models

def get_username(api: tweepy.API, reply_tweet: tweepy.models.Status):
    parent_tweet_id = reply_tweet.in_reply_to_status_id

    # If the tweet that mentions us is a parent tweet
    if parent_tweet_id is None:
        return None

    parent_tweet = api.get_status(parent_tweet_id)
    parent_user = parent_tweet.user
    return parent_user