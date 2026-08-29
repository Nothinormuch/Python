import paramiko
import os

def InstaLoadComment(post_url):
    import instaloader
    Load = instaloader.Instaloader()
    Load.login(os.getenv('InstagramUsername'),os.getenv('InstagramPassword'))
    post = instaloader.Post.from_shortcode(Load.context, post_url.rsplit('/', 2)[1])
    comments = post.get_comments()
    for comment in comments:
        print(f"{comment.owner.username}:\n\t {comment.text}\n\n")