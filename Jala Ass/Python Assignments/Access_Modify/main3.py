#3.Cretaing a Public class.

class ceatingPublicClass():
    def __init__(self):
        self.x=3.14
        print(self.x)
        print('its a public class')
obj=ceatingPublicClass()


#3.1Accessing a public class.

from public import ceatingPublicClass
class inAnotherFile():
    acess=ceatingPublicClass()
    print(acess.x)
obj=inAnotherFile()