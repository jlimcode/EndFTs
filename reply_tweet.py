import tweepy
import tweepy.models

def base_comment(api: tweepy.API, status_obj: tweepy.models.Status):
    username = status_obj.user.screen_name
    message = f"@{username} read my docs!"
    api.update_status(status=message, in_reply_to_status_id=status_obj.id)

def reply_nft(api: tweepy.API, status_obj: tweepy.models.Status):
    status_out = api.get_status(status_obj.in_reply_to_status_id)
    username = status_out.user.screen_name
    link_out = "https://opensea.io/collection/ankrpolygonnft-suvt0ll7od"
    message = f"@{username} we seem to own your NFT: \n {link_out}"
    api.update_status(message, in_reply_to_status_id=status_out.id)
    return "tweeted!"

