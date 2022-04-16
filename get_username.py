import tweepy

def get_username(client: tweepy.Client, reply_tweet: tweepy.Tweet):
    parent_tweet_id = reply_tweet.conversation_id
    # status = api.get_status(parent_id)
    parent_tweet = tweepy.Tweet(parent_tweet_id)
    parent_user = parent_tweet.author_id
    # parent_user = api.get_user(parent_id)
    return parent_user