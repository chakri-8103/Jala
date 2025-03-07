n=int(input('Enter number of terms:'))
a=[]
p=len(a)
for i in range(n):
    k=int(input())
    a.append(k)
m=int(input('Enter a number to know its index:'))
if m in a:
    print('Element Found',a[m-1])
else:
    print('Element not found')