def avg(n):
    a=[]
    s=0
    for i in range(1,n+1):
        k=int(input())
        a.append(k)
    for i in a:
        s=s+i
    return s//n
n=int(input('Enter a number of terms:'))
k=avg(n)
print(k)