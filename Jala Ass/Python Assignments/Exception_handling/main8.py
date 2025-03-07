a=int(input('Enter a 1st Value:'))
b=int(input('Enter a 2nd Value:'))
if b==0:
    print('ZeroDivisionException')
else:
    res=a//b
    print(res)