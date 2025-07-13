from pymongo import MongoClient
from pymongo.errors import PyMongoError

def get_db():
    try:
        client = MongoClient("mongodb+srv://<username>:<password>@cluster0.wjwul8v.mongodb.net/", serverSelectionTimeoutMS=1000, connect=True)
        db = client['scraped_data_db']
        return db
    except PyMongoError as e:
        print(f"Failed to connect to the database: {str(e)}")

db = get_db()