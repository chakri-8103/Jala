class MyClass:
    def __init__(self, a1=None, a2=None):
        if a1 is None and a2 is None:
            print("This is a Default Constructor")
        elif a2 is None:
            print(f"First Argument: {a1}")
        else:
            print(f"Second Argument: {a1}, {a2}")

obj1 = MyClass()
obj2 = MyClass("Chakradhar")
obj3 = MyClass("Chakradhar", 21)