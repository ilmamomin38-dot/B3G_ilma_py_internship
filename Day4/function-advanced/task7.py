import time

# Decorator to measure execution time
def timer(func):
    def wrapper():
        start = time.time()      # Start time
        result = func()          # Call the original function
        end = time.time()        # End time
        print(f"Execution time: {end - start:.6f} seconds")
        return result
    return wrapper


@timer
def calculate_sum():
    total = sum(range(1, 1000001))
    print("Sum:", total)


# Call the decorated function
calculate_sum()