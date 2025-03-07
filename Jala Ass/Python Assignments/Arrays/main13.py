def sm(n):
    a=[]
    for i in range(1,n+1):
        x=int(input())
        a.append(x)
    maxx=a[0]
    for i in a:
        if i>maxx:
            maxx=i
    a.remove(maxx)
    smaxx=a[0]
    for i in a:
        if i>smaxx:
            smaxx=i
    print('Second Largest Number',smaxx)
n=int(input('Enter number of terms:'))
sm(n)