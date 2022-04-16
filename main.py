import os
import tweepy

<<<<<<< HEAD
KEY = os.getenv("CONSUMER_KEY")
SECRET = os.getenv("CONSUMER_SECRET")
TOKEN = os.getenv("ACCESS_TOKEN")
TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")
 
# Authenticate to Twitter
auth = tweepy.OAuthHandler(KEY, SECRET)
auth.set_access_token(TOKEN, TOKEN_SECRET)
api = tweepy.API(auth)
 
try:
   api.verify_credentials()
   print("Authentication Successful")
except:
   print("Authentication Error")

def main():
    return
=======
logger = logging.getLogger()

def create_api():
    consumer_key = os.getenv("CONSUMER_KEY")
    consumer_secret = os.getenv("CONSUMER_SECRET")
    access_token = os.getenv("ACCESS_TOKEN")
    access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")
    bearer_token = os.getenv("BEARER_TOKEN")

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info("API created")

    stream = tweepy.Stream(consumer_key,consumer_secret,access_token,access_token_secret)
    return api,stream


def main():
    api,stream = create_api()
    #mentions = stream.sample()
    #print(mentions)
    recent_mentions = api.mentions_timeline(count = 3)
    for mention in recent_mentions:
        print(mention)
    


>>>>>>> gaurav
    

if __name__ == "__main__":
    main()