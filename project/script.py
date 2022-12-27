import praw
import os
import requests
import datetime
import json
from dotenv import load_dotenv
load_dotenv()

API_SECRET = os.getenv('API_SECRET')
DEV_ID = os.getenv('DEV_ID')
DEV_USERNAME= os.getenv('DEV_USERNAME')
DEV_PASSWORD =os.getenv('DEV_PASSWORD')
reddit = praw.Reddit(
    client_id=DEV_ID,
    client_secret= API_SECRET,
    password=DEV_PASSWORD,
    user_agent="testscript",
    username= DEV_USERNAME,
)
current_date = datetime.datetime.now()

submissions = reddit.subreddit("learnpython")
todays_posts = submissions.new()
obj = {}
for post in todays_posts:
  # Check if the post was created today
  if post.created_utc > current_date.timestamp() - 86400 and post.over_18 == False :
    post_dict = {
      "title": post.title,
      "author": post.author.name,
      "url": post.url
    }
    # Convert the dictionary to a JSON object and print it
    post_json = json.dumps(post_dict, indent=2)
    print(post_json)
  else:
    break
