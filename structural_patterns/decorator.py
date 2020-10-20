"""
Attach additional responsibilities to an object dynamically. Decorators provide a flexible alternative to subclassing for extending functionality.
"""


class Component:
    def operation(self):
        raise NotImplementedError("Subclass must override operation()!")


class ConcreteComponent(Component):
    def operation(self):
        return 1

    
class Decorator(Component):
    def __init__(self):
        self._component = ConcreteComponent()

    def operation(self):
        return self._component.operation()


class ConcreteDecoratorA(Decorator):
    def operation(self):
        return 2


class ConcreteDecoratorB(Decorator):
    def operation(self):
        result = super().operation()
        result += self.other_operation()
        return result

    def other_operation(self):
        return 3
