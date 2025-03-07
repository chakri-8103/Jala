def ins(n):
    a=[]
    for i in range(1,n+1):
        k=int(input())
        a.append(k)
    p=int(input('Enter position to insert an element'))
    o=int(input('Enter an element to insert'))
    i=a.insert(p,o)
    for i in a:
        print(i,end=' ')
n=int(input('Enter number of terms:'))
ins(n)
