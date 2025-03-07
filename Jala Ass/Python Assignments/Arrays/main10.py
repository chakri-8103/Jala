def dup(n):
    a=[]
    for i in range(1,n+1):
        x=int(input())
        a.append(x)
    for i in a:
        if a.count(i)>1:
            print(i)
            break
n=int(input('Enter number of terms:'))
dup(n)
