def process_order(order):
    try:
        item = order["item"]
        price = order["price"]
    except KeyError as e:
        print(f"Error: Missing required key: {e}")
    else:
        print("Order Details:")
        print(f"Item: {item}")
        print(f"Price: ${price}")
    finally:
        print("Processing complete")

process_order({"item": "Laptop", "price": 999.99})

print()
 
process_order({"item": "Mouse"})