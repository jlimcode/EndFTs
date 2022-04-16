import os
import tweepy

KEY = os.getenv("CONSUMER_KEY")
SECRET = os.getenv("CONSUMER_SECRET")
TOKEN = os.getenv("ACCESS_TOKEN")
TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")

auth = tweepy.OAuthHandler(KEY, SECRET)
auth.set_access_token(TOKEN, TOKEN_SECRET)

# Create API object
api = tweepy.API(auth)

print(api)