def eo(n):
    a=[]
    for i in range(1,n+1):
        x=int(input())
        a.append(x)
    print('The even numbers are:')
    for i in a:
        if i%2==0:
            print(i)
    print('The odd numbers are:')
    for i in a:
        if i%2!=0:
            print(i)
            
n=int(input('Enter number of terms:'))
eo(n)
