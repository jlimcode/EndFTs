import tweepy

def get_username(api: tweepy.API, reply_tweet: tweepy.Tweet):
    parent_tweet_id = reply_tweet.conversation_id
    parent_tweet = api.get_status(parent_tweet_id)
    parent_user = parent_tweet.user
    return parent_user