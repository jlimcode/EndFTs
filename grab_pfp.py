import re
import tweepy
import logging
from tokens import *
from imgurpython import ImgurClient

# Note since access tokens expire after an hour, only the refresh token is required (library handles autorefresh)
client = ImgurClient(IMGUR_CLIENTID, IMGUR_SECRET, IMGUR_REFRESH_TOKEN, IMGUR_ACCESS_TOKEN)

def grab_pfp(user: tweepy.User, client: ImgurClient = client):
    pfp_url = user.profile_image_url
    pfp_url = re.sub(r"_normal\.(\w+)$", repl=r"_400x400.\1", string=pfp_url)
    res = client.upload_from_url(url=pfp_url)
    logging.info(f"Response: {res}")
    return res["link"]