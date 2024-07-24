from pymongo import MongoClient

client = MongoClient("mongodb+srv://dbUser:dbUser@guidepad.h78otcd.mongodb.net/?retryWrites=true&w=majority&appName=Guidepad")

db = client.todo_db

collection_name = db["todocollection"]