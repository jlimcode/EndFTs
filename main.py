import tweepy
import logging
from tokens import *
from stream import MyStream

def create_api():
    auth = tweepy.OAuthHandler(
        consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET,
        access_token=ACCESS_TOKEN, access_token_secret=ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth, wait_on_rate_limit=True)

    try:
        api.verify_credentials()
    except Exception as e:
        exit(e)

    stream = MyStream(
        consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET,
        access_token=ACCESS_TOKEN, access_token_secret=ACCESS_TOKEN_SECRET, 
        api=api)
    return api, stream


def main():
    logging.basicConfig(filename="EndFTs.log", filemode = 'w', level = logging.INFO)

    api, stream = create_api()
    stream.filter(track=["@EndFTs"])


if __name__ == "__main__":
    main()
