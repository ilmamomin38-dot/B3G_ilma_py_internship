def recursive_sum(n):
    if n==1:
        return 1
    return n+recursive_sum(n-1)
num=10
print("Sum=",recursive_sum(num))