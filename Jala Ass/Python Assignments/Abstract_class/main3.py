from abc import ABC, abstractmethod
class AbstractClass(ABC):
    @abstractmethod
    def abstract_method_1(self):
        pass
    @abstractmethod
    def abstract_method_2(self):
        pass

class ChildClass(AbstractClass):
    def abstract_method_1(self):
        return "ChildClass: Implementation of abstract_method_1"
    def abstract_method_2(self):
        return "ChildClass: Implementation of abstract_method_2"
    def call_abstract_methods(self):
        return self.abstract_method_1(), self.abstract_method_2()
child_instance = ChildClass()
res1, res2 = child_instance.call_abstract_methods()
print(res1)
print(res2)