class MyClass:
    def __init__(self):  
        print("This is a Public Constructor.")
    def pro_con(self):  
        print("This is a Protected Constructor")
    def pri_con(self):  
        print("This is a Private Constructor.")
    def apri_con(self):
        self.pri_con()  
obj = MyClass()
obj.pro_con()  
obj.apri_con()  