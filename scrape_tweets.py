import os
import csv
import tweepy

KEY = os.getenv("CONSUMER_KEY")
SECRET = os.getenv("CONSUMER_SECRET")
TOKEN = os.getenv("ACCESS_TOKEN")
TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")


def scrape_tweets(username: str, filename: str):
    # Authenticate to Twitter
    auth = tweepy.OAuthHandler(KEY, SECRET)
    auth.set_access_token(TOKEN, TOKEN_SECRET)
    api = tweepy.API(auth)

    try:
        api.verify_credentials()
        print("Authentication Successful")
    except:
        print("Authentication Error")

    tweets = api.user_timeline(screen_name=username, count=1000, include_rts=False, tweet_mode='extended')
    tweets = [{"tweet": tweet.full_text} for tweet in tweets]  
    # print(tweets)

    with open(filename, 'w', newline='') as f:
        fieldnames = ["tweet"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)  
        writer.writeheader()
        writer.writerows(tweets)