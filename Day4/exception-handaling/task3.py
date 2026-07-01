class InvalidAgeError(Exception):
    """Custom exception for invalid age values."""
    pass


def register_user(age):
    if age < 0:
        raise InvalidAgeError("Invalid age: Age cannot be less than 0.")
    elif age > 120:
        raise InvalidAgeError("Invalid age: Age cannot be greater than 120.")
    return "User registered successfully."

try:
    print(register_user(25))
    print(register_user(5))
except InvalidAgeError as e:
    print(e)

try:
    print(register_user(150))
except InvalidAgeError as e:
    print(e)