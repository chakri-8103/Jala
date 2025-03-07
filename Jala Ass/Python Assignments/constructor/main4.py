class Solution:
    def __init__(self, name, age):  
        self.name = name  
        self.age = age  
    def display(self):  
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
obj = Solution("Prasanna", 20)  
obj.display()  