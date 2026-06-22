subscribers={
    "a@gmail.com",
    "b@gmail.com",
    "c@gmail.com",
    "d@gmail.com"
}

customers={
    "c@gmail.com"
    "d@gmail.com"
    "e@gmail.com"
    "f@gmail.com"

}

never_purchased=subscribers-customers
purchase_not_subscribed=customers-subscribers

print("Subscribers who never purchased:",never_purchased)
print("Customers who purchased but not subscribed:",purchase_not_subscribed)
