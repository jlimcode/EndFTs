import csv
import tweepy
from tokens import *

def scrape_tweets(username: str, filename: str):
    # Authenticate to Twitter
    auth = tweepy.OAuthHandler(
        consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET,
        access_token=ACCESS_TOKEN, access_token_secret=ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)

    try:
        api.verify_credentials()
    except Exception as e:
        exit(e)

    tweets = api.user_timeline(screen_name=username, count=1000, include_rts=False, tweet_mode='extended')
    tweets = [{"tweet": tweet.full_text} for tweet in tweets]

    with open(filename, 'w', newline='') as f:
        fieldnames = ["tweet"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)  
        writer.writeheader()
        writer.writerows(tweets)