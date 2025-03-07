#1.Creatinga a private fields.

class name():
    def __init__(self):
        self.__nameofst1='I am a Front End Deveoloper'
    def private_c(self):
        print('This is private class')
    def access_private(self):
        print(self.__nameofst1)

class roll(name):
    def rno(self):
        self.rollOfSt="My Name is Chakradhar"
        print(self.rollOfSt)
        self.rollofSt2="I am Studying In Aditya Degree College"
        print(self.rollofSt2)
    def access_parent_class(self):
        try:
            print(self.__nameofst1)
            print(self.__nameofst2)
        except AttributeError:
            print('parent class cannot be accessed')
obj=roll()
obj.rno()
obj.access_private()
obj.access_parent_class()
obj.private_c()