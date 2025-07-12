from exception_handler import exception_handler
from db import cats

# creates a new cat with name, age, and features parameters
# if the cat already exists, it will not be inserted again
# inserts a new cat into db
@exception_handler
def create_cat(name: str, age: int, features: list):
    if cats.find_one({"name": name}):
        return f"Cat {name} already exists in the database."
    cats.insert_one({
        "name": name,
        "age": age,
        "features": features
    })
    return f"Cat {name} added to database successfully."

# returns all cats sorted by name with ascending
@exception_handler
def read_all():
    cats_list = cats.find().sort("name", 1)
    return "\n".join(str(cat) for cat in cats_list)

# returns a cat found by name
@exception_handler
def read_cat(name: str):
    return cats.find_one({"name": name})

# updates information of a cat by name
# can accept multiple parameters to update
# uses default python dictionary to update
@exception_handler
def update_cat(name: str, **kwargs):
    update_query={}
    
    if "age" in kwargs:
        update_query.setdefault("$set", {})["age"] = kwargs["age"]

    if "features" in kwargs:
        update_query.setdefault("$set", {})["features"] = kwargs["features"]

    if not update_query:
        return "No fields to update provided."
    
    cats.update_one({"name": name}, update_query)
    return f"Cat {name} updated successfully."

# deletes a cat by name
@exception_handler
def delete_cat(name: str):
    cats.delete_one({"name": name})
    return f"Cat {name} deleted from database."

# deletes all cats from db
@exception_handler
def delete_all():
    cats.delete_many({})
    return "All cats deleted from database."

COMMANDS = {
    "create": lambda args:
    create_cat(args[0], int(args[1]), args[2:])
    if len(args) >= 2 else "Usage: create -name -age -features:[ .. ]",

    "read": lambda args:
    read_cat(args[0]) if args else "Usage: read -name",
    
    "read_all": lambda args: read_all(),

    "update": lambda args:
    update_cat(args[0], args[1], args[2:])
    if len(args) >= 2 else "Usage: update -name -age optional: -features:[ .. ]",
    
    "delete": lambda args:
    delete_cat(args[0])
    if args else "Usage: delete -name",
    
    "delete_all": lambda args: delete_all()
}