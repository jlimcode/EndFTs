import tweepy

def base_comment(api: tweepy.API, status_obj: tweepy.models.Status):
    username = status_obj.user.screen_name
    message = '@{un} touch grass'
    fmt_msg = message.format(un = username)
    api.update_status(status=fmt_msg, in_reply_to_status_id=status_obj.id)
