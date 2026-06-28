celsius=[0,20,25,30,37,100]

fahrenheit=list(map(lambda c:(c*9/5)+32,celsius))

print("Celsius:",celsius)
print("Fahrenheit:",fahrenheit)