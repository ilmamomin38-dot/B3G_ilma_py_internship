prices={"pen":10,"notbook":40,"bag":500}

for key in prices:
    print(key)

for key, value in prices.items():
    print(key,"costs",value)

for value in prices.values():
    print(value)
      