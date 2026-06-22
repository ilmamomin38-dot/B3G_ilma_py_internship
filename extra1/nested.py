students = {
    "101": {"name": "Riya", "marks": [85, 90, 78]},
    "102": {"name": "Aman", "marks": [70, 60, 88]},
}

print(students["101"]["name"])
print(students["102"]["marks"][1])

for roll, info in students.items():
    average = sum(info["marks"]) / len(info["marks"])
    print(roll, info["name"], round(average, 2))