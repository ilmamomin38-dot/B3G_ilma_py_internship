def bulid_invoice(customer_name,*args,**kwargs):
    print("Customer Name:",customer_name)
    print("Total Item Price:",sum(args))
    print("Extra Details:")

    for key, value in kwargs.items():
     print(f"{key}:{value}")

bulid_invoice(
    "ilma momin",
    250,300,100,
    discount=50,
    tax=25,
    shipping=40
)   