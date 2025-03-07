n=int(input())
print('Odd Numbers')
i=1
for i in range(1,n+1):
    if i%2!=0:
        print(i)
print('Even Numbers')
for i in range(n+1):
    if i%2==0:
        print(i)