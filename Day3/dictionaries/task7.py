inventory={
    "pen":100,
    "notbook":50
}

inventory["pen"]=inventory["pen"]+10
product="notebook" 

if "notebook" in inventory:
    inventory[product]-=2
    print(product,"notebook sold")

else:
    print("notbook not found")
    product="bag"

if product in inventory:
    inventory["bag"]-=1
else:
    print("bag not found")
    print("updated inventory:")
    print(inventory)