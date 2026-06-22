students=[("John", 25), ("Alice", 30), ("Bob", 22), ("Eve", 28)]

sorted_students = sorted(students, key=lambda x: x[1], reverse=True)

print("Students sorted by Marks:")
print(sorted_students)
