def fun(n):
    a=[]
    for i in range(1,n+1):
        k=int(input())
        a.append(k)
    m=int(input('Enter a Specific value:'))
    if m in a:
        return True
    else:
        return False
n=int(input('Enter number of terms:'))
k=fun(n)
if k==True:
    print('Has a Specific Value')
else:
    print('Does not contain specific value')