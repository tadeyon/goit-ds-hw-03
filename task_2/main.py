import json
from parser import parse_data
from db import db

def dump_data(filename: str, data: dict):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False)

if __name__ == "__main__":
    try:
        quotes_data, authors_data = parse_data()

        db.quotes.create_index("text", unique=True)        
        db.authors.create_index("fullname", unique=True)


        with open("task_2/quotes.json", 'r', encoding='utf-8') as f:
            quotes = json.load(f)
            db.quotes.insert_many(quotes)

        with open("task_2/authors.json", 'r', encoding='utf-8') as f:
            authors = json.load(f)
            db.authors.insert_many(authors)

        print("Data imported successfully.")

    except Exception as e:
        print(f"An error has occured: {e}")