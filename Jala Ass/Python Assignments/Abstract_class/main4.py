from abc import ABC, abstractmethod
class AbstractClass(ABC):
    @abstractmethod
    def abstract_method(self):
        pass
    def non_abstract_method_1(self):
        return "AbstractClass: Non-abstract method 1"
    def non_abstract_method_2(self):
        return "AbstractClass: Non-abstract method 2"
class ChildClass(AbstractClass):
    def abstract_method(self):
        return "ChildClass: Implementation of abstract_method"
    def non_abstract_methods(self):
        return self.non_abstract_method_1(), self.non_abstract_method_2()
child_instance = ChildClass()
res1, res2 = child_instance.non_abstract_methods()
print(res1)
print(res2)