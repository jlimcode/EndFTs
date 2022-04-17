import os
import tweepy
import logging
from image_format import image_to_json
from mint import create_nft
from upload_file import send_post
from tokens import *
from grab_pfp import grab_pfp
from username import get_username
from reply_tweet import base_comment, reply_nft

class MyStream(tweepy.Stream):
    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret, api, **kwargs):
        self.api = api
        super().__init__(consumer_key, consumer_secret, access_token, access_token_secret, **kwargs)

    def on_status(self, status):
        logging.info(f"{status.user.screen_name} tweeted: {status.text}")
        parent = get_username(api=self.api, reply_tweet=status)
        
        if parent is None:
            base_comment(self.api, status)
        else:
            logging.info(f"Parent comment is from user {parent.screen_name}.")
            link = grab_pfp(user=parent)
            logging.info(f"{parent.screen_name}'s profile picture: {link}.")
            json_str = image_to_json(link)
            w3_storage_url = send_post(json_str)
            hex_hash = create_nft(w3_storage_url)
            print('nft gen success', hex_hash)
            out = reply_nft(self.api, status)
            print(out)

            
        return super().on_status(status)


def streamTweets(hashtags: list[str]):
    myStreamListener = MyStream(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    myStreamListener.filter(track=hashtags)