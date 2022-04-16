import os
import tweepy

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
    

if __name__ == "__main__":
    main()