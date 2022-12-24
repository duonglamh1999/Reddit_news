import praw
import os
from dotenv import load_dotenv
load_dotenv()

API_SECRET = os.getenv('API_SECRET')

print(API_SECRET)
# reddit = praw.Reddit(
#     client_id="CLIENT_ID",
#     client_secret="CLIENT_SECRET",
#     password="PASSWORD",
#     user_agent="USERAGENT",
#     username="USERNAME",
# )