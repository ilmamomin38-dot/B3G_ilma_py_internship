students=[
    {"name":"ilma","marks":92},
    {"name":"zeniab","marks":80},
    {"name":"aksha","marks":87},
    {"name":"aiman","marks":85}
]

top_students=students[0]

for student in students:
    if student["marks"] > top_students["marks"]:
        top_students=student

print("student with highest marks:")
print("name:",top_students["name"])
print("marks:",top_students["marks"])
