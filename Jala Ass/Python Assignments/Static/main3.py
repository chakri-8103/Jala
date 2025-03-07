class Example:
    a = 30

obj1 = Example()
obj2 = Example()

obj1.static_var = 50
print(obj1.a)
print(obj2.a)
print(Example.a)