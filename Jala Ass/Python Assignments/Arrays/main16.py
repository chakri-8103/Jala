def ls(n):
    a=[]
    for i in range(1,n+1):
        x=int(input())
        a.append(x)
    maxx=a[0]
    minn=a[0]
    for i in a:
        if i>maxx:
            maxx=i
        if i<minn:
            minn=i
    print(maxx-minn)
n=int(input('Enter number of terms:'))
ls(n)