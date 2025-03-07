def com(a,b):
    return list(set(a) & set(b))

a = [1, 2, 3, 4, 5]
b= [3, 4, 5, 6, 7]
print("Common values:",com(a,b))