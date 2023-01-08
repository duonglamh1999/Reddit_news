import praw
import os
import requests
import datetime
import json
from dotenv import load_dotenv
from datetime import datetime
from pymongo import MongoClient
load_dotenv()

REDDIT_API_SECRET = os.getenv('REDDIT_API_SECRET')
REDDIT_DEV_ID = os.getenv('REDDIT_DEV_ID')
REDDIT_DEV_USERNAME= os.getenv('REDDIT_DEV_USERNAME')
REDDIT_DEV_PASSWORD =os.getenv('REDDIT_DEV_PASSWORD')
reddit = praw.Reddit(
    client_id=REDDIT_DEV_ID,
    client_secret= REDDIT_API_SECRET,
    password=REDDIT_DEV_PASSWORD,
    user_agent="testscript",
    username= REDDIT_DEV_USERNAME,
)
current_date = datetime.now()

submissions = reddit.subreddit("learnpython")
todays_posts = submissions.new()
obj = {}
for post in todays_posts:
  # Check if the post was created today
  if post.created_utc > current_date.timestamp() - 86400 and post.over_18 == False :
    post_dict = {
      "title": post.title,
      "author": post.author.name,
      "url": post.url,
      "created_utc": datetime.utcfromtimestamp(post.created_utc).strftime('%Y-%m-%d %H:%M:%S')
      }
    # Convert the dictionary to a JSON object and print it
    post_json = json.dumps(post_dict, indent=2)
    print(post_json)
  else:
    break
