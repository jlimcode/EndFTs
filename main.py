import os
import tweepy
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
        raise e

    stream = tweepy.Stream(consumer_key,consumer_secret,access_token,access_token_secret)
    return api,stream


def main():
    api,stream = create_api()
    check_recent_mentions = {}

    while True:
        recent_mentions = api.mentions_timeline(count = 3)
        for mention in recent_mentions:
            if mention in check_recent_mentions:
                pass
            else:
                check_recent_mentions[mention] = True
                print(mention.text)
            time.sleep(15)
    


    

if __name__ == "__main__":
    main()