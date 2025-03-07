try:
    a = int(input("Enter a 1st number: "))
    b = int(input("Enter a 2nd number: "))
    res = a//b
    print("Result:", res)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Invalid input! Please enter a valid number.")
finally:
    print("Execution completed.")