"""
Provide a unified interface to a set of interfaces in a subsystem. Facade defines a higher-level interface that makes the subsystem easier to use.
"""


class Facade:
    def __init__(self):
        self._subsystem_class2 = Class2()
        self._subsystem_class3 = Class3()

    def operation(self):
        result = self._subsystem_class2.method_1()
        result += self._subsystem_class2.method_2()
        result += self._subsystem_class3.method_3()
        return result


class Class1:
    def method_1(self):
        raise NotImplementedError("Subclass must override method_1()!")

    def method_2(self):
        return 2


class Class2(Class1):
    def method_1(self):
        return 1


class Class3:
    def method_3(self):
        return 3
