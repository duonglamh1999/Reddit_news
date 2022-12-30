import praw
import os
import requests
import datetime
import json
from dotenv import load_dotenv
from datetime import datetime
from pymongo import MongoClient
load_dotenv()

CLUSTER = os.getenv('CLUSTER')
client = MongoClient(CLUSTER)

print(client.list_database_names())
db= client.news
print(db.list_collection_names())