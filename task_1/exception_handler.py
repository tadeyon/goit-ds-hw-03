from functools import wraps
from pymongo.errors import PyMongoError

def exception_handler(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except IndexError as e:
            return "Index error: Please check your input parameters."
        except ValueError as e:
            return "Value error: age must be an integer."
        except PyMongoError as e:
            return f"Database error: {str(e)}"
        except Exception as e:
            return f"An error occurred: {str(e)}"
    return wrapper