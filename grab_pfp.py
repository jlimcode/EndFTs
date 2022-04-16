import os
import re
import tweepy
from imgurpython import ImgurClient

client_id = os.getenv("IMGUR_CLIENTID")
client_secret = os.getenv("IMGUR_SECRET")
access_token = os.getenv("IMGUR_REFRESH_TOKEN")
refresh_token = os.getenv("IMGUR_ACCESS_TOKEN")

# Note since access tokens expire after an hour, only the refresh token is required (library handles autorefresh)
client = ImgurClient(client_id, client_secret, access_token, refresh_token)

def grab_pfp(user: tweepy.User, client: ImgurClient = client):
    pfp_url = user.profile_image_url
    pfp_url = re.sub(r"_normal\.(\w+)$", repl=r"_400x400.\1", string=pfp_url)
    res = client.upload_from_url(url=pfp_url)
    print(res)
    return res["link"]