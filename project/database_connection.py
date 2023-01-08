import praw
import os
import requests
import datetime
import json
from dotenv import load_dotenv
from datetime import datetime
from pymongo import MongoClient
load_dotenv()

MONGO_CLUSTER = os.getenv('MONGO_CLUSTER')
client = MongoClient(MONGO_CLUSTER)

print(client.list_database_names())
db= client.news
print(db.list_collection_names())