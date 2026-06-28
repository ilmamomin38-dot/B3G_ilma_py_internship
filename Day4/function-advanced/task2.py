def apply_discount(price,percent=10):
    discounted_price=price-(price*percent/100)
    print("Original Price:",price)
    print("Discount:",percent,"%")
    print("Final Price:",discounted_price)

apply_discount(1000)
print()

apply_discount(1000,percent=20)
