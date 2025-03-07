def cpy(n):
    a=[]
    b=[]
    for i in range(1,n+1):
        k=list(map(int,input().split()))
        a.append(k)
    for i in a:
        print(i,end=' ')
    print()
    c=a.copy();
    print("The copy array is:",c)
n=int(input('Enter number of terms:'))
cpy(n)