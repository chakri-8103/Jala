class Package:
    class ClassOne:
        def __init__(self):
            print("ClassOne Constructor Called")

        def method_one(self):
            print("Method from ClassOne")

    class ClassTwo:
        def __init__(self):
            print("ClassTwo Constructor Called")

        def method_two(self):
            print("Method from ClassTwo")

obj1 = Package.ClassOne()
obj1.method_one()


obj2 = Package.ClassTwo()
obj2.method_two()
