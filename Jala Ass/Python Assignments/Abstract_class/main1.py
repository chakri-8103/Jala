from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    def describe(self):
        print("This is a Square of area:") 
class S(Shape):
    def __init__(self, side):
        self.side = side 

    def area(self):  
        return self.side ** 2 
s = S(5)
s.describe()
print(s.area())