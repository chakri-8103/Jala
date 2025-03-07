from abc import ABC, abstractmethod
class AbstractClass(ABC):
    def __init__(self, value):
        self.value = value
    @abstractmethod
    def abstract_method(self):
        pass
    def non_abstract_method(self):
        return f"Value: {self.value}"
class SubClass(AbstractClass):
    def __init__(self, value, extra_value):
        super().__init__(value)
        self.extra_value = extra_value
    def abstract_method(self):
        return f"Abstract method called."
sub_obj= SubClass(10, "extra")
print(sub_obj.non_abstract_method())
print(sub_obj.abstract_method())
try:
    abstract_object = AbstractClass(5)
except TypeError as e:
    print(f"Error: {e}")