def arr(n):
    a=[]
    s=0
    for i in range(1,n+1):
        k=int(input())
        a.append(k)
    for i in a:
        s=s+i
    return s
n=int(input('Enter number of terms:'))
k=arr(n)
print(k)