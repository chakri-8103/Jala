
class ClassOne:
    def __init__(self, name):
        self.name = name
    def display(self):
        print(" Chakradhar,", self.name)
class ClassTwo:
    def __init__(self, age):
        self.age = age
    def show_age(self):
        print("Age", self.age)
ClassOne("Degree Final Year").display()
ClassTwo(21).show_age()