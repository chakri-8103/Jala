number = int(input("Enter a number: "))
original = number
sum = 0
while number > 0:
    digit = number % 10
    sum += digit ** 3
    number //= 10
if sum == original:
    print(f"{original} is an Armstrong number.")
else:
    print(f"{original} is not an Armstrong number.")
