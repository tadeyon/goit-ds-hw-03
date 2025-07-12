from pymongo import MongoClient, errors as PyMongoError

def get_db():
    try:
        client = MongoClient("mongodb://localhost:27017/", serverSelectionTimeoutMS=1000, connect=True)
        db = client['cats_database']
        cats = db['cats']
        return cats
    except PyMongoError as e:
        print(f"Failed to connect to the database: {str(e)}")

cats = get_db()