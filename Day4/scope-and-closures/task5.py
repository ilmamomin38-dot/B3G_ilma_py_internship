mode = "Global Mode"

def outer():
    mode = "Outer Mode"

    def inner():
   
        mode = "Inner Mode"

        print("Inside inner() - Local mode:", mode)

    inner()

    print("Inside outer() - Enclosing mode:", mode)

outer()

print("Global scope mode:", mode)