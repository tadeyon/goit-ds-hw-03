from pymongo import MongoClient
from pymongo.errors import PyMongoError

def get_db():
    try:
        client = MongoClient("mongodb://mongodb-container:27017/", serverSelectionTimeoutMS=1000, connect=True)
        client.server_info()
        db = client['cats_database']
        cats = db['cats']
        return cats
    except PyMongoError as e:
        print(f"Failed to connect to the database: {str(e)}")

cats = get_db()