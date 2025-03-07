class Example:
    static_var = 40  # Static variable

Example.static_var = 60  # Changing at class level

print(Example.static_var)  # Output: 60
obj1 = Example()
print(obj1.static_var)  # Output: 60 (reflects class-level change)
