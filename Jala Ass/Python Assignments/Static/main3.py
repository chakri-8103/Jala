
class Example:
    static_var = 30  # Static variable

obj1 = Example()
obj2 = Example()

obj1.static_var = 50  # Changing only for obj1

print(obj1.static_var)  # Output: 50 (changed for obj1 only)
print(obj2.static_var)  # Output: 30 (unchanged for obj2)
print(Example.static_var)  # Output: 30 (unchanged for class)
