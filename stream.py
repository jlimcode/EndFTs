import os
import tweepy

KEY = os.getenv("CONSUMER_KEY")
SECRET = os.getenv("CONSUMER_SECRET")
TOKEN = os.getenv("ACCESS_TOKEN")
TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")

class MyStream(tweepy.Stream):
    def on_status(self, status):
        # we do our thing here
        print(status.user.screen_name + " tweeted: " + status.text)
        return super().on_status(status)

def streamTweets(hashtags: list[str]):
    myStreamListener = MyStream(KEY, SECRET, TOKEN, TOKEN_SECRET)
    myStreamListener.filter(track=hashtags)