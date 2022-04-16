import os
import tweepy
from get_username import get_username
from grab_pfp import grab_pfp

KEY = os.getenv("CONSUMER_KEY")
SECRET = os.getenv("CONSUMER_SECRET")
TOKEN = os.getenv("ACCESS_TOKEN")
TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")

class MyStream(tweepy.Stream):
    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret, api, **kwargs):
        self.api = api
        super().__init__(consumer_key, consumer_secret, access_token, access_token_secret, **kwargs)

    def on_status(self, status):
        # we do our thing here
        print(status.user.screen_name + " tweeted: " + status.text)
        parent = get_username(self.api, reply_tweet=status)
        print(parent)
        link = grab_pfp(user=parent)
        print(link)
        return super().on_status(status)

def streamTweets(hashtags: list[str]):
    myStreamListener = MyStream(KEY, SECRET, TOKEN, TOKEN_SECRET)
    myStreamListener.filter(track=hashtags)