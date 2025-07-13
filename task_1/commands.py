from exception_handler import exception_handler
import argparse
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

def update_command(args):
    parser = argparse.ArgumentParser(prog="update", description="Update a cat")
    parser.add_argument("name", help="Name of the cat to update")
    parser.add_argument("age", type=int, help="New age of the cat")
    parser.add_argument("features", nargs="*", help="List of features")

    try:
        parsed_args = parser.parse_args(args)
    except SystemExit:
        return "Invalid arguments. Usage: update <name> <age> [features ...]"

    kwargs = {"age": parsed_args.age}
    if parsed_args.features:
        kwargs["features"] = parsed_args.features

    return update_cat(name=parsed_args.name, **kwargs)

COMMANDS = {
    "create": lambda args:
    create_cat(args[0], int(args[1]), args[2:])
    if len(args) >= 2 else "Usage: create <name> <age> [features ...]",

    "read": lambda args:
    read_cat(args[0]) if args else "Usage: read <name>",
    
    "read_all": lambda args: read_all(),

    "update": update_command,

    
    "delete": lambda args:
    delete_cat(args[0])
    if args else "Usage: delete <name>",
    
    "delete_all": lambda args: delete_all()
}