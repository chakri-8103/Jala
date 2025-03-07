class Parent:
    def __init__(self, a1=None):
        if a1 is None:
            print("Default Parent Constructor")
        else:
            print(f"First Parent Argument: {a1}")
class Child(Parent):
    def __init__(self, a1=None):
        if a1 is None:
            super().__init__()
            print("Default Child Constructor")
        else:
            super().__init__(a1)
            print(f"Child First Argument: {a1}")
obj1 = Child()
obj2 = Child("Welcome")