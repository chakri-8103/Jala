class MyClass:
    static = 10
    @classmethod
    def modify(cls, new_value):
        cls.static = new_value
print(MyClass.static)  
MyClass.modify(20)
print(MyClass.static)
