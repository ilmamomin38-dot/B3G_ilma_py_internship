price=[10,20,30,40,50,60,70,80,90,100]
avg_price=sum(price)/len(price)
above_price=[p1 for p1 in price if p1>avg_price]

print("list of price",price)
print("Average price:",avg_price)
print("Above price:",above_price)

