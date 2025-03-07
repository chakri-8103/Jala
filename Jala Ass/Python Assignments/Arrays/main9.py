def res(n):
    a=[]
    for i in range(1,n+1):
        x=int(input())
        a.append(x)
    for i in a:
        print(a[::-1],end=' ')
        break
n=int(input('Enter number of terms:'))
res(n)