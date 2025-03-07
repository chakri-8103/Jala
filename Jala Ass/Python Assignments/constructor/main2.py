class Parent:
    def __init__(self, msg="Default Parent Constructor"):
        print(msg)

class Child(Parent):
    def __init__(self):
        super().__init__("Parent Constructor Called from Child")
        print("Child Constructor Called")

obj = Child()
