def sum(num):
    if len(num)==1:
        return num[0]
    else:
        return num[0] + sum(num[1:]) #recursion

print(sum([1,2,3,4,5]))