products={"pen": 10,"notbook":40,"pencil":5,"eraser":2,"bag":600}

expensive_products={products: price 
                    for products, price in products.items()
                    if price>100}

print("original products:",products)
print(products)

print("expensive products:",expensive_products)
print(expensive_products)