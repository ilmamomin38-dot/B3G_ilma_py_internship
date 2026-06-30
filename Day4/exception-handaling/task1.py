def safe_division(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "Erro:Division by zero is not allowed."
    except TypeError:
        return "Error Both input must be numbers."

print(safe_division(10,2))
print(safe_division(10,0))
print(safe_division(10,"2"))