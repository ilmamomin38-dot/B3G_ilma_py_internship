class InvalidRangeError(Exception):
    """Custom exception for numbers outside the valid range."""
    pass


while True:
    try:
        number = int(input("Enter a number between 1 and 10: "))

        if number < 1 or number > 10:
            raise InvalidRangeError("Number must be between 1 and 10.")

        print(f"Valid input: {number}")
        break

    except ValueError:
        print("Error: Please enter a valid numeric value.")
    except InvalidRangeError as e:
        print(f"Error: {e}")