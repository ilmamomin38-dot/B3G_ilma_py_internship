marks = {"Riya": 88, "Aman": 95, "Sara": 72, "Kabir": 91}

sorted_by_marks = dict(sorted(marks.items(), key=lambda item: item[1], reverse=True))
print(sorted_by_marks)