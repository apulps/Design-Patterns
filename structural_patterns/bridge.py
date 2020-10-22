"""
Decouple an abstraction from its implementation so that the two can vary independently.
"""


class Abstraction:
    def __init__(self, implementation):
        self._implementation = implementation

    def operation(self):
        return (f'Result from Abstraction: {self._implementation.implemented_operation()}')


class ExtendedAbstraction(Abstraction):
    def operation(self):
        return (f'Result from ExtendedAbstraction: {self._implementation.implemented_operation()}')


class Implementation:
    def implemented_operation(self):
        raise NotImplementedError("Subclass must override implemented_operation()!")


class ConcreteImplementationA(Implementation):
    def implemented_operation(self):
        return 2


class ConcreteImplementationB(Implementation):
    def implemented_operation(self):
        return 3
