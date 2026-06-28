# Decorator to check if all arguments are positive
def require_positive(func):
    def wrapper(*args, **kwargs):
        # Check all positional arguments
        for value in args:
            if value <= 0:
                print("Error: All arguments must be positive numbers.")
                return

        # Check all keyword arguments
        for value in kwargs.values():
            if value <= 0:
                print("Error: All arguments must be positive numbers.")
                return

        # Call the original function if all arguments are positive
        return func(*args, **kwargs)

    return wrapper


@require_positive
def divide(a, b):
    print("Result:", a / b)


# Valid call
divide(10, 2)

# Invalid calls
divide(-10, 2)
divide(10, 0)