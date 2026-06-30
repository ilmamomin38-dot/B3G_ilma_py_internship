def safe_access(lst,index):
    try:
        return lst[index]
    except IndexError:
        return None

number=[10,20,30]

print(safe_access(number,1))
print(safe_access(number,5))
print(safe_access(number,-1))