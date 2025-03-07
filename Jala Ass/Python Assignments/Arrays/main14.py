def sm(n):
    a=[]
    for i in range(1,n+1):
        x=int(input())
        a.append(x)
    minn=a[0]
    for i in a:
        if i<minn:
            minn=i
    a.remove(minn)
    sminn=a[0]
    for i in a:
        if i<sminn:
            sminn=i
    print('Second Largest Number',sminn)            
n=int(input('Enter number of terms:'))
sm(n)