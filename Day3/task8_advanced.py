tasks=[]

#Adding tasks
tasks.append("Student Python")
tasks.append("Employee Python")
tasks.append("Numbers Python")
tasks.append("String Python")
tasks.append("List Python")

print("Tasks after adding:")
for task in tasks:
    print("-", task)

#Removing a task
tasks.remove("Numbers Python")
tasks.remove("String Python")

print("\nTasks after removing:")
for task in tasks:
    print("-", task)