"""
Define the skeleton of an algorithm in an operation, deferring some steps to client subclasses. Template Method lets subclasses redefine certain steps of an algorithm without changing the algorithm's structure.
"""


class AbstractClass:
    def template_method(self):
        result = self.base_operation1()
        result += self.base_operation2()
        result += self.base_operation3()
        result += self.required_operation1()
        result += self.required_operation2()
        self.hook1()
        self.hook2()
        return result

    def base_operation1(self):
        return 1

    def base_operation2(self):
        return 2

    def base_operation3(self):
        return 3

    def required_operation1(self):
        raise NotImplementedError("Subclass must override required_operation1()!")
    
    def required_operation2(self):
        raise NotImplementedError("Subclass must override required_operation2()!")

    def hook1(self):
        pass

    def hook2(self):
        pass


class ConcreteClass1(AbstractClass):
    def required_operation1(self):
        return -1
    
    def required_operation2(self):
        return -2


class ConcreteClass2(AbstractClass):
    def required_operation1(self):
        return 5
    
    def required_operation2(self):
        return 6
    
    def hook1(self):
        print("Implemented Hook 1")
