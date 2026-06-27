employee={
    "Amit":50000,
    "Riya":75000,
    "Karan":65000,
    "Neha":90000,
    "priya":80000
}

salary_list=list(employee.items())
salary_list.sort(key=lambda x:x[1],reverse=True)



print("Top 3 Highest Paid Employees:")

for A in range(3):
    print(salary_list[A][0],":",salary_list[A][1])

