import os
import tweepy
from stream import MyStream
import time


def create_api():
    consumer_key = os.getenv("CONSUMER_KEY")
    consumer_secret = os.getenv("CONSUMER_SECRET")
    access_token = os.getenv("ACCESS_TOKEN")
    access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")
    bearer_token = os.getenv("BEARER_TOKEN")

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)

    try:
        api.verify_credentials()
    except Exception as e:
        print("authentication error")

    stream = MyStream(consumer_key, consumer_secret,
                      access_token, access_token_secret, api=api)
    return api, stream


def main():
    api, stream = create_api()
    print("tracking! 0")
    stream.filter(track=["@EndFTs"])
    print("tracking!")


if __name__ == "__main__":
    main()
