from dotenv import load_dotenv
import os
from pymongo import MongoClient

mongo_string = os.getenv('MONGOSTRING')
client = MongoClient(mongo_string)

db = client.todo_db

collection_name = db["todocollection"]