def rem(n):
    a=[]
    for i in range(1,n+1):
        k=int(input())
        a.append(k)
    m=int(input('Enter a specific element to remove'))
    a.remove(m)
    for i in a:
        print(i,end=' ')
n=int(input('Enter number of terms:'))
rem(n)