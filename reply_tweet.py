import tweepy
import tweepy.models

def base_comment(api: tweepy.API, status_obj: tweepy.models.Status):
    username = status_obj.user.screen_name
    message = f"@{username} read my docs!"
    api.update_status(status=message, in_reply_to_status_id=status_obj.id)
